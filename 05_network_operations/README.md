# 05: 🔌 Network Operations via Webhooks

## 🎯 Mission

Transform your webhook server into a real network automation powerhouse! You'll use Netmiko to connect to network devices and execute commands through webhook triggers. This is where automation gets exciting - your webhooks will actually control network infrastructure!

## 🎖 Goals

By the end of this module, you'll be able to:

- [ ] **Connect to network devices** using Netmiko through webhooks
- [ ] **Execute show commands** and return formatted output
- [ ] **Handle device credentials** securely
- [ ] **Process device responses** and format them for webhook consumers
- [ ] **Create device-specific endpoints** for different network operations
- [ ] **Implement error handling** for network connectivity issues

## 📖 Why Network Operations in Webhooks?

Webhooks + Network Automation = **Powerful Event-Driven Infrastructure**

### Real-World Scenarios

| Trigger Event | Webhook Action | Network Result |
|---------------|----------------|----------------|
| 🚨 Device Alert | Execute diagnostic commands | Get interface status, CPU info |
| 📊 Performance Issue | Check device health | Collect statistics, logs |
| 🔧 Change Request | Deploy configuration | Update ACLs, VLANs, routing |
| 🔍 Security Event | Gather forensics | Show ARP tables, connections |

Your webhooks become the **bridge** between monitoring systems and network devices!

## 🔗 Netmiko Basics

Netmiko is a Python library that simplifies SSH connections to network devices.

### Simple Connection Example

```python
from netmiko import ConnectHandler

# Device connection parameters
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

# Connect and execute command
with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command('show version')
    print(output)
```

### Supported Device Types

- `cisco_ios` - Cisco IOS devices
- `cisco_ios_xe` - Cisco IOS-XE devices  
- `cisco_nxos` - Cisco Nexus switches
- `arista_eos` - Arista switches
- `juniper_junos` - Juniper devices
- And many more!

## 🛡️ Security Considerations

**Never hardcode credentials in your webhook code!** Use environment variables or configuration files.

### Using Environment Variables

```python
import os
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': os.getenv('DEVICE_HOST'),
    'username': os.getenv('DEVICE_USER'),
    'password': os.getenv('DEVICE_PASS'),
}
```

### Using Configuration Files

```python
import yaml

# Load from config file (not in git!)
with open('device_config.yaml', 'r') as file:
    device_config = yaml.safe_load(file)

device = device_config['sandbox_device']
```

## 🎭 DevNet Sandbox Integration

For this module, you'll use **Cisco DevNet Always-On Sandbox** devices:

### Always-On IOS XE Device

- **Host**: `sandbox-iosxe-latest-1.cisco.com`  
- **SSH Port**: 22
- **Username**: `developer`
- **Password**: `C1sco12345`
- **Device Type**: `cisco_ios_xe`

### Always-On IOS XR Device  

- **Host**: `sandbox-iosxr-1.cisco.com`
- **SSH Port**: 22
- **Username**: `admin`
- **Password**: `C1sco12345`
- **Device Type**: `cisco_iosxr`

These are **real devices** you can practice with safely!

## 🛠️ Building Network Operation Endpoints

Let's create webhooks that perform real network operations!

### Basic Device Info Endpoint

```python
from netmiko import ConnectHandler
from fastapi import HTTPException

@app.get("/device/info")
def get_device_info():
    device = {
        'device_type': 'cisco_ios_xe',
        'host': 'sandbox-iosxe-latest-1.cisco.com',
        'username': 'developer', 
        'password': 'C1sco12345',
    }
    
    try:
        with ConnectHandler(**device) as net_connect:
            version_output = net_connect.send_command('show version')
            
        return {
            "webhook": "Device info retrieved",
            "device": device['host'],
            "command": "show version",
            "output": version_output,
            "status": "success"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Device connection failed: {str(e)}")
```

### Interface Status Webhook

```python
@app.get("/device/interfaces")
def get_interface_status():
    # Execute 'show ip interface brief'
    # Return formatted interface information
    # Include interface names, IPs, status
```

## 📊 Formatting Network Output

Raw device output can be messy. Let's make it webhook-friendly!

### Parsing Show Commands

```python
def parse_interface_brief(output):
    """Parse 'show ip interface brief' output into structured data"""
    interfaces = []
    lines = output.split('\n')[1:]  # Skip header
    
    for line in lines:
        if line.strip():
            parts = line.split()
            if len(parts) >= 6:
                interface = {
                    'name': parts[0],
                    'ip_address': parts[1],
                    'ok': parts[2],
                    'method': parts[3],
                    'status': parts[4],
                    'protocol': parts[5]
                }
                interfaces.append(interface)
    
    return interfaces
```

### Using TextFSM (Advanced)

```python
import textfsm

# TextFSM templates parse command output into structured data
# Great for complex parsing tasks
# Templates available in ntc-templates library
```

## 🎪 Your Mission: Build Network Operation Webhooks

In the `network_ops_server.py` file, create endpoints that:

1. **Device Information** - Get basic device details (`show version`)
2. **Interface Status** - Check interface health (`show ip interface brief`)
3. **Custom Command** - Execute any show command via webhook parameter
4. **Device Health Check** - Multiple commands for comprehensive status
5. **Webhook-Triggered Diagnostics** - Respond to alerts with network diagnostics

### Example Endpoint Structure

```python
@app.post("/network/diagnose")
def diagnose_network_issue(issue_data: dict):
    """
    Receive network issue webhook and run diagnostics
    
    Expected payload:
    {
        "issue_type": "connectivity|performance|security",
        "device": "device-hostname-or-ip",
        "description": "Issue description"
    }
    """
    # Based on issue_type, run appropriate diagnostic commands
    # Return results in structured format
```

## 🧪 Testing Your Network Operations

### Testing with cURL

```bash
# Test device info
curl http://localhost:8000/device/info

# Test interface status  
curl http://localhost:8000/device/interfaces

# Test custom command
curl -X POST http://localhost:8000/device/command \
     -H "Content-Type: application/json" \
     -d '{"command": "show ip route"}'

# Test network diagnostics
curl -X POST http://localhost:8000/network/diagnose \
     -H "Content-Type: application/json" \
     -d '{"issue_type": "connectivity", "device": "router-01", "description": "Interface down"}'
```

### DevNet Sandbox Access

1. **Visit**: [DevNet Sandbox](https://devnetsandbox.cisco.com/)
2. **Find**: Always-On devices
3. **Test connection** with SSH client first
4. **Use in your webhooks** once verified

## 🔧 Advanced Network Operations

### Configuration Changes (Be Careful!)

```python
# Only on lab/sandbox devices!
def configure_device(config_commands):
    with ConnectHandler(**device) as net_connect:
        # Enter configuration mode
        net_connect.config_mode()
        
        # Send configuration commands
        output = net_connect.send_config_set(config_commands)
        
        # Save configuration
        net_connect.save_config()
        
        return output
```

### Bulk Operations

```python
def check_multiple_devices(device_list):
    results = []
    for device in device_list:
        try:
            # Connect to each device
            # Collect information
            results.append({"device": device, "status": "success", "data": "..."})
        except:
            results.append({"device": device, "status": "failed", "error": "..."})
    
    return results
```

## ✅ Testing Checklist

Verify your network operation endpoints:

- [ ] **Successfully connect** to DevNet sandbox devices
- [ ] **Execute show commands** and return output
- [ ] **Handle connection failures** gracefully
- [ ] **Parse command output** into structured data
- [ ] **Secure credential handling** (no hardcoded passwords)
- [ ] **Proper error responses** for network issues

## 🚨 Troubleshooting

**Connection timeout?**

- Check if the sandbox device is reachable
- Verify credentials are correct
- Ensure device_type matches the actual device

**Authentication failed?**

- Double-check username and password
- Some devices require enable password
- Try connecting manually with SSH first

**Command not recognized?**

- Different devices have different command syntax
- Use `show ?` to see available commands
- Check device_type is correct for your target

**Slow responses?**

- Network devices can be slow
- Increase timeout in ConnectHandler parameters  
- Consider async operations for better performance

## 🏆 Success Criteria

You've mastered this module when:

- [x] Your webhooks successfully connect to real network devices
- [x] You can execute show commands via webhook triggers
- [x] Device output is formatted for webhook consumers
- [x] Error handling prevents crashes from network issues
- [x] You understand the security implications of network automation

## 🚀 Ready for Real Event-Driven Automation?

Outstanding! Your webhooks now control actual network devices. Time for the final piece - configuring devices to send webhooks when events occur!

**Next up:** `06_cisco_edm_webhooks/` - Configure Cisco EDM applets to trigger your webhooks! ⚡

---

### 💡 Pro Tips

- **Always test in sandbox first** - Never experiment on production devices
- **Use connection pooling** for frequent operations - Reuse connections when possible
- **Log all network operations** - Important for auditing and debugging
- **Implement rate limiting** - Protect devices from excessive connections
- **Consider async operations** - For better performance with multiple devices

### 🔗 Quick References

- [Netmiko Documentation](https://github.com/ktbyers/netmiko)
- [DevNet Sandbox](https://devnetsandbox.cisco.com/)
- [Cisco Command References](https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/13769-5.html)
- [TextFSM Templates](https://github.com/networktocode/ntc-templates)