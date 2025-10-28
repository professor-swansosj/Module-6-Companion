# Cisco EDM Applet Configurations for Webhook Integration

This file contains ready-to-use EDM applet configurations that will trigger your FastAPI webhook server when network events occur.

## Prerequisites

Before using these configurations:

1. **Webhook server running** on accessible IP/port
2. **HTTP client enabled** on Cisco device: `ip http client source-interface <interface>`
3. **Network connectivity** between device and webhook server
4. **Appropriate event patterns** configured for your environment

## Basic Webhook Test Applet

```cisco
! Test applet - manually triggerable for testing
event manager applet WEBHOOK_TEST
 description "Basic webhook test - trigger manually"
 event none
 action 1.0 info type routername  
 action 2.0 set webhook_url "http://192.168.1.100:8000/test-webhook"
 action 3.0 set device_name "$_info_routername"
 action 4.0 set test_data "{'event':'manual_test','device':'$device_name','message':'EDM webhook test successful'}"
 action 5.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$test_data\" $webhook_url"
 action 6.0 syslog msg "Webhook test completed - check server logs"

! To manually trigger: event manager run WEBHOOK_TEST
```

## Interface Status Change Webhook

```cisco
! Monitor interface up/down events
event manager applet INTERFACE_STATUS_WEBHOOK
 description "Trigger webhook on interface state changes"
 event syslog pattern ".*LINK-.*UPDOWN.*"
 action 1.0 info type routername
 action 2.0 info type interface_name
 action 3.0 cli command "show ip interface brief"
 action 4.0 set webhook_url "http://192.168.1.100:8000/interface-alert"
 action 5.0 set device_name "$_info_routername"  
 action 6.0 set interface_name "$_info_interface_name"
 action 7.0 set timestamp "$_event_pub_time"
 action 8.0 set interface_data "{'event_type':'interface_change','device':'$device_name','interface':'$interface_name','timestamp':'$timestamp','raw_message':'$_syslog_msg'}"
 action 9.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$interface_data\" $webhook_url"
 action 10.0 syslog msg "Interface change webhook sent for $interface_name"
```

## High CPU Utilization Alert

```cisco
! Monitor CPU usage and alert via webhook
event manager applet CPU_HIGH_WEBHOOK
 description "Webhook alert for high CPU utilization"
 event snmp oid 1.3.6.1.4.1.9.9.109.1.1.1.1.7.1 get-type exact entry-op gt entry-val 80 poll-interval 60
 action 1.0 info type routername
 action 2.0 cli command "show processes cpu sorted | include CPU"
 action 3.0 set webhook_url "http://192.168.1.100:8000/cpu-alert"
 action 4.0 set device_name "$_info_routername"
 action 5.0 set cpu_percent "$_snmp_oid_val"
 action 6.0 set timestamp "$_event_pub_time"
 action 7.0 set cpu_data "{'event_type':'high_cpu','device':'$device_name','cpu_percent':'$cpu_percent','timestamp':'$timestamp','threshold':'80'}"
 action 8.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$cpu_data\" $webhook_url"
 action 9.0 syslog msg "High CPU webhook sent - CPU at $cpu_percent%"
```

## Memory Utilization Warning

```cisco
! Monitor memory usage
event manager applet MEMORY_WARNING_WEBHOOK  
 description "Webhook for memory utilization warnings"
 event snmp oid 1.3.6.1.4.1.9.9.48.1.1.1.6.1 get-type exact entry-op lt entry-val 20 poll-interval 300
 action 1.0 info type routername
 action 2.0 cli command "show memory statistics"
 action 3.0 set webhook_url "http://192.168.1.100:8000/memory-alert"
 action 4.0 set device_name "$_info_routername"
 action 5.0 set memory_free "$_snmp_oid_val"
 action 6.0 set memory_data "{'event_type':'low_memory','device':'$device_name','memory_free_percent':'$memory_free','timestamp':'$_event_pub_time'}"
 action 7.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$memory_data\" $webhook_url"
 action 8.0 syslog msg "Low memory webhook sent - $memory_free% free"
```

## Configuration Change Detection

```cisco
! Detect configuration changes and log via webhook
event manager applet CONFIG_CHANGE_WEBHOOK
 description "Webhook notification for configuration changes" 
 event syslog pattern ".*PARSER-5-CFGLOG_LOGGEDCMD.*"
 action 1.0 info type routername
 action 2.0 set webhook_url "http://192.168.1.100:8000/config-change"
 action 3.0 set device_name "$_info_routername" 
 action 4.0 set change_time "$_event_pub_time"
 action 5.0 set config_data "{'event_type':'config_change','device':'$device_name','timestamp':'$change_time','syslog_message':'$_syslog_msg'}"
 action 6.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$config_data\" $webhook_url"
 action 7.0 syslog msg "Configuration change webhook notification sent"
```

## Error Rate Monitoring

```cisco
! Monitor for error patterns in syslogs
event manager applet ERROR_PATTERN_WEBHOOK
 description "Webhook for critical error patterns"
 event syslog pattern ".*ERROR.*|.*CRITICAL.*|.*ALERT.*"
 action 1.0 info type routername
 action 2.0 set webhook_url "http://192.168.1.100:8000/error-alert"
 action 3.0 set device_name "$_info_routername"
 action 4.0 set error_time "$_event_pub_time"
 action 5.0 set error_msg "$_syslog_msg"
 action 6.0 set error_data "{'event_type':'error_detected','device':'$device_name','timestamp':'$error_time','error_message':'$error_msg','severity':'high'}"
 action 7.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$error_data\" $webhook_url"
 action 8.0 syslog msg "Error pattern webhook sent for: $error_msg"
```

## Business Hours Only Alert

```cisco
! Only send webhooks during business hours (9 AM - 5 PM)
event manager applet BUSINESS_HOURS_WEBHOOK
 description "Webhook alerts only during business hours"
 event syslog pattern ".*CRITICAL.*"
 action 1.0 cli command "show clock"
 action 2.0 regexp "([0-9]+):([0-9]+)" "$_cli_result" match hour minute
 action 3.0 if $hour ge 9
 action 4.0  if $hour le 17
 action 5.0   info type routername
 action 6.0   set webhook_url "http://192.168.1.100:8000/business-alert"
 action 7.0   set device_name "$_info_routername"
 action 8.0   set business_data "{'event_type':'business_hours_alert','device':'$device_name','hour':'$hour','message':'Critical alert during business hours'}"
 action 9.0   cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$business_data\" $webhook_url"
 action 10.0  syslog msg "Business hours webhook sent"
 action 11.0 else
 action 12.0  syslog msg "Critical alert outside business hours - webhook skipped"
 action 13.0 end
 action 14.0 end
```

## Comprehensive Health Check Webhook

```cisco
! Periodic comprehensive health check webhook  
event manager applet HEALTH_CHECK_WEBHOOK
 description "Periodic health status webhook"
 event timer cron cron-entry "0 */4 * * *"
 action 1.0 info type routername
 action 2.0 cli command "show processes cpu | include CPU"
 action 3.0 cli command "show memory statistics | include Total"  
 action 4.0 cli command "show ip interface brief | count Up"
 action 5.0 set webhook_url "http://192.168.1.100:8000/health-check"
 action 6.0 set device_name "$_info_routername"
 action 7.0 set check_time "$_event_pub_time"
 action 8.0 set health_data "{'event_type':'health_check','device':'$device_name','timestamp':'$check_time','status':'periodic_check','frequency':'every_4_hours'}"
 action 9.0 cli command "curl -X POST -H \"Content-Type: application/json\" -d \"$health_data\" $webhook_url"
 action 10.0 syslog msg "Periodic health check webhook sent"
```

## Usage Instructions

### 1. Customize Webhook URLs
Replace `192.168.1.100:8000` with your actual webhook server IP and port.

### 2. Deploy Configurations
```cisco
! Connect to your Cisco device
configure terminal

! Copy and paste the desired applet configuration
! Example:
event manager applet WEBHOOK_TEST
 description "Basic webhook test"
 event none
 action 1.0 info type routername
 ! ... rest of configuration

! Save configuration
write memory
```

### 3. Enable HTTP Client
```cisco
! Enable HTTP client functionality
configure terminal
ip http client source-interface GigabitEthernet0/0/1
exit
```

### 4. Test Your Configuration
```cisco
! Manually trigger test applet
event manager run WEBHOOK_TEST

! Check applet status
show event manager policy registered

! View execution history  
show event manager history events
```

### 5. Monitor and Debug
```cisco
! View running applets
show running-config | section event manager

! Check for errors
show logging | include EEM

! Debug applet execution (use carefully!)
debug event manager action cli
```

## Security Notes

- **Never include real production credentials** in these examples
- **Use HTTPS** for production webhook URLs when possible  
- **Implement authentication** on your webhook endpoints
- **Validate webhook sources** to prevent unauthorized triggers
- **Rate limit** your webhooks to prevent DoS scenarios

## Troubleshooting Tips

1. **Test curl manually** on the device first
2. **Check network connectivity** between device and webhook server
3. **Verify JSON formatting** - use single quotes in EDM actions
4. **Monitor both device and server logs** during testing
5. **Start with simple test applets** before complex ones

## Compatible Webhook Endpoints

These configurations are designed to work with the FastAPI endpoints you built in previous modules:

- `/test-webhook` - Basic webhook testing
- `/interface-alert` - Interface status changes  
- `/cpu-alert` - CPU utilization alerts
- `/memory-alert` - Memory warnings
- `/config-change` - Configuration change logs
- `/error-alert` - Error pattern detection  
- `/business-alert` - Business hours notifications
- `/health-check` - Periodic health status

Remember to ensure your FastAPI server has these endpoints configured to handle the JSON payloads sent by these EDM applets!