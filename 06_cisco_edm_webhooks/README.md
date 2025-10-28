# 06: ⚡ Cisco EDM Applets & Real Event-Driven Automation

## 🎯 Mission

Complete the webhook automation loop! You'll configure Cisco devices to automatically trigger your webhooks when network events occur. This is true event-driven automation - your network will "call home" when something interesting happens!

## 🎖 Goals

By the end of this module, you'll be able to:

- [ ] **Understand Cisco EDM** (Embedded Device Manager) applets
- [ ] **Configure event triggers** on Cisco devices
- [ ] **Set up HTTP POST actions** to call your webhooks
- [ ] **Test event-driven workflows** end-to-end
- [ ] **Troubleshoot EDM configurations** and webhook calls
- [ ] **Design real-world automation scenarios** using webhooks

## 📖 What is Cisco EDM?

**EDM (Embedded Device Manager)** applets are mini-programs that run on Cisco devices to monitor events and trigger actions automatically.

### Key Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Event** | What triggers the applet | Interface goes down, CPU > 80% |
| **Action** | What happens when triggered | Send HTTP POST, execute command |
| **Conditional** | Optional logic/filtering | Only during business hours |

### Real-World EDM Use Cases

- 🚨 **Interface failure** → HTTP POST to webhook → Create support ticket
- 📊 **High CPU usage** → HTTP POST to webhook → Trigger diagnostics  
- 🔧 **Configuration change** → HTTP POST to webhook → Log to SIEM
- ⚠️ **Error rate spike** → HTTP POST to webhook → Alert team

## 🛠️ EDM Applet Syntax

EDM applets use a simple configuration syntax:

### Basic Applet Structure

```bash
event manager applet WEBHOOK_TEST
 event syslog pattern "Interface.*down"
 action 1.0 cli command "show interfaces"
 action 2.0 info type routername
 action 3.0 mail server "192.168.1.100" to "admin@company.com" from "router@company.com" subject "Interface Down" body "Interface failure detected"
```

### HTTP POST Action (The Magic!)

```bash
event manager applet WEBHOOK_ALERT
 event syslog pattern ".*LINK-3-UPDOWN.*"
 action 1.0 cli command "show ip interface brief"
 action 2.0 cli command "show version"
 action 3.0 set webhook_url "http://your-webhook-server.com:8000/network-alert"
 action 4.0 set json_data "{'event':'interface_change','device':'$_info_routername','timestamp':'$_event_pub_time'}"
 action 5.0 cli command "curl -X POST -H 'Content-Type: application/json' -d '$json_data' $webhook_url"
```

## 🎪 Your Webhook-Ready EDM Applets

Let's create EDM applets that talk to your FastAPI webhook server!

### Interface Status Change Webhook

```bash
! EDM Applet: Interface Status Change
event manager applet INTERFACE_WEBHOOK
 event syslog pattern ".*LINK-.*UPDOWN.*"
 action 1.0 info type routername
 action 2.0 cli command "show ip interface brief"
 action 3.0 set webhook_url "http://192.168.1.100:8000/network-alert"
 action 4.0 set device_name "$_info_routername"
 action 5.0 set event_time "$_event_pub_time" 
 action 6.0 set json_payload "{'event_type':'interface_change','device':'$device_name','timestamp':'$event_time'}"
 action 7.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$json_payload\" $webhook_url"
```

### High CPU Alert Webhook

```bash
! EDM Applet: CPU Monitoring  
event manager applet CPU_WEBHOOK
 event snmp oid 1.3.6.1.4.1.9.9.109.1.1.1.1.7.1 get-type exact entry-op gt entry-val 80 poll-interval 60
 action 1.0 info type routername
 action 2.0 cli command "show processes cpu sorted"
 action 3.0 set webhook_url "http://192.168.1.100:8000/cpu-alert"
 action 4.0 set device_name "$_info_routername"
 action 5.0 set cpu_value "$_snmp_oid_val"
 action 6.0 set json_data "{'event_type':'high_cpu','device':'$device_name','cpu_percent':'$cpu_value'}"
 action 7.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$json_data\" $webhook_url"
```

## 🔧 Configuration Steps

### Step 1: Prepare Your Webhook Server

Make sure your FastAPI server has endpoints ready to receive EDM webhooks:

```python
@app.post("/network-alert")
def handle_network_alert(alert_data: dict):
    """Handle alerts from Cisco EDM applets"""
    print(f"🔔 Network Alert Received: {alert_data}")  # Print to terminal!
    return {
        "webhook": "Network alert received from EDM",
        "device": alert_data.get("device", "unknown"),
        "event_type": alert_data.get("event_type", "unknown"),
        "timestamp": alert_data.get("timestamp", "unknown"),
        "status": "processed"
    }

@app.post("/cpu-alert")  
def handle_cpu_alert(cpu_data: dict):
    """Handle CPU alerts from EDM monitoring"""
    print(f"🚨 CPU Alert Received: {cpu_data}")  # Print to terminal!
    return {
        "webhook": "CPU alert received",
        "device": cpu_data.get("device", "unknown"), 
        "cpu_percent": cpu_data.get("cpu_percent", "unknown"),
        "action": "Diagnostics triggered",
        "status": "processed"
    }
```

### Step 1.5: 🌐 Expose Your Server with VS Code Dev Tunnels

**Problem**: Your webhook server runs on `localhost`, but Cisco devices can't reach it from the internet!

**Solution**: VS Code Dev Tunnels create a secure tunnel from your local server to a public URL that Cisco devices can access.

#### Quick Dev Tunnel Setup

1. **Open VS Code Command Palette**: `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)

2. **Search for "Dev Tunnels"**: Type `>Ports: Focus on Ports View`

3. **Start Your Webhook Server First**:

   ```bash
   uvicorn edm_webhook_server:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Create the Tunnel**:
   - In VS Code, go to the **PORTS** tab (bottom panel)
   - Find your port `8000` in the list
   - Right-click on port `8000` → **Port Visibility** → **Public**
   - Right-click again → **Forward Port** → **8000**

5. **Get Your Public URL**:
   - Look in the PORTS tab for something like: `https://abc123-8000.preview.app.github.dev`
   - **Copy this URL!** This is your webhook endpoint that Cisco devices can reach

#### Alternative: Command Line Dev Tunnel

```bash
# Install GitHub CLI if not already installed
# Then create a tunnel
gh auth login
gh codespace ports forward 8000 --visibility public
```

#### Update EDM Applet URLs

Replace your local URLs with the Dev Tunnel URL:

**Before (localhost - won't work from Cisco device):**

```bash
action 3.0 set webhook_url "http://192.168.1.100:8000/network-alert"
```

**After (Dev Tunnel - accessible from internet):**

```bash
action 3.0 set webhook_url "https://abc123-8000.preview.app.github.dev/network-alert"
```

#### Verify Your Tunnel

Test your public webhook URL:

```bash
# Test from anywhere on the internet
curl -X POST https://your-tunnel-url.preview.app.github.dev/network-alert \
  -H "Content-Type: application/json" \
  -d '{"test": "webhook", "device": "test-device"}'
```

You should see the webhook data printed in your VS Code terminal! 🎉

#### Dev Tunnel Pro Tips

- **Tunnel stays active** as long as VS Code is running
- **URL changes** when you restart - update EDM applets accordingly  
- **Free tier limits** - GitHub provides reasonable limits for learning
- **Security**: Only share tunnel URLs with trusted devices/people
- **Alternative tools**: `ngrok`, `localtunnel`, or cloud deployment

### Step 2: Configure HTTP Client on Cisco Device

Enable HTTP client functionality:

```bash
! Enable IP HTTP client for curl commands
ip http client source-interface GigabitEthernet0/0/1
```

### Step 3: Deploy EDM Applets

Copy the EDM configurations to your Cisco device:

1. **Connect to device** (SSH/Console)
2. **Enter configuration mode**: `configure terminal`
3. **Paste EDM applet configuration**
4. **Save configuration**: `write memory`

### Step 4: Test Your Automation

Trigger events to test the webhook flow:

```bash
! Manually trigger interface event (for testing)
interface GigabitEthernet0/0/2
 shutdown
 no shutdown

! Check if applet triggered
show event manager history events
```

## 🧪 Testing Your Event-Driven Setup

### End-to-End Testing Workflow

1. **Start your webhook server**: `uvicorn your_server:app --reload`
2. **Configure EDM applet** on Cisco device
3. **Trigger a test event** (shutdown/no shutdown interface)
4. **Check webhook logs** for incoming requests
5. **Verify device logs**: `show event manager history events`

### Debugging EDM Applets

```cisco
! Check applet status
show event manager policy registered

! View applet configuration  
show running-config | section event manager

! See execution history
show event manager history events

! Debug applet execution (use carefully!)
debug event manager action cli
```

## 🎨 Advanced EDM Scenarios

### Conditional Logic

```bash
event manager applet BUSINESS_HOURS_ONLY
 event syslog pattern ".*ERROR.*"
 action 1.0 cli command "show clock"
 action 2.0 regexp "([0-9]+):([0-9]+)" "$_cli_result" match hour minute
 action 3.0 if $hour ge 9
 action 4.0  if $hour le 17
 action 5.0   set webhook_url "http://192.168.1.100:8000/business-alert"
 action 6.0   cli command "curl -X POST $webhook_url"
 action 7.0  end
 action 8.0 end
```

### Multiple Action Sequences

```bash
event manager applet COMPREHENSIVE_ALERT
 event syslog pattern ".*CRITICAL.*"
 action 1.0 cli command "show version"
 action 2.0 cli command "show processes cpu"
 action 3.0 cli command "show memory statistics"
 action 4.0 set webhook_url "http://192.168.1.100:8000/critical-alert"
 action 5.0 cli command "curl -X POST -d '{\"severity\":\"critical\"}' $webhook_url"
 action 6.0 syslog msg "Critical alert webhook sent"
```

## 🏗️ Your Mission: Complete Webhook Automation

In this final module, create:

1. **Webhook endpoints** that handle EDM-generated alerts
2. **EDM applet configurations** for common network events  
3. **Test procedures** to verify end-to-end automation
4. **Documentation** of your complete webhook automation system

### Example Configuration File

Create `edm_configs.txt` with your EDM applet configurations ready to copy-paste to devices.

## ✅ Testing Checklist

Verify your complete automation setup:

- [ ] **Webhook server responds** to EDM-style POST requests
- [ ] **EDM applets are configured** correctly on test device
- [ ] **HTTP client is enabled** on Cisco device
- [ ] **Network connectivity** exists between device and webhook server
- [ ] **Events trigger webhooks** successfully
- [ ] **Webhook responses are logged** and visible

## 🚨 Troubleshooting

**Webhooks not triggered?**

- Check `show event manager policy registered`
- Verify event pattern matches actual log messages
- Test with `test event manager applet APPLET_NAME`

**HTTP requests failing?**

- Verify `ip http client` is configured
- Check network connectivity with `ping webhook-server`
- Test curl manually: `curl -X POST http://server:8000/test`

**JSON formatting issues?**

- Use single quotes around JSON in EDM actions
- Escape double quotes properly
- Test JSON format with online validators

## 🏆 Success Criteria

You've mastered event-driven automation when:

- [x] Your network devices automatically call your webhooks
- [x] Webhook server processes EDM-generated alerts correctly  
- [x] You can trace events from device trigger to webhook response
- [x] Your automation responds to real network events
- [x] You understand the complete event-driven workflow

## 🎉 Congratulations

You've built a complete event-driven network automation system! Your devices now proactively communicate with your applications when events occur. This is the foundation of modern, responsive network operations.

## 🚀 What's Next?

You've completed the webhook automation journey! Consider exploring:

- **Production deployment** - Secure, scalable webhook infrastructure
- **Advanced monitoring** - Webhook analytics and performance tracking  
- **Integration platforms** - Connect with SIEM, ticketing, chat systems
- **Database persistence** - Store and analyze webhook event history
- **Authentication/security** - Secure your webhook endpoints

---

### 💡 Pro Tips

- **Start with simple events** - Interface up/down are easy to test
- **Use descriptive applet names** - Makes troubleshooting easier
- **Log everything** - Both on device and webhook server
- **Test thoroughly** - Automation failures can be worse than no automation
- **Document your patterns** - Create a library of useful EDM applets

### 🔗 Quick References

- [Cisco EDM Configuration Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/eem/configuration/xe-16/eem-xe-16-book.html)
- [EDM Action Types](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/eem/command/eem-cr-book.html)
- [Webhook Security Best Practices](https://webhooks.fyi/)
- [FastAPI Production Deployment](https://fastapi.tiangolo.com/deployment/)