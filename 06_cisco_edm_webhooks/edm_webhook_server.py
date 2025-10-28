"""
Module 06: Cisco EDM Webhook Handler Server

TODO: Create webhook endpoints that receive and process alerts from Cisco EDM applets!
This server completes the event-driven automation loop.

Hint: EDM applets send JSON data - make sure your endpoints can handle the expected formats!
"""

# TODO: Import required modules for webhook handling
# Hint: from fastapi import FastAPI, Request
# TODO: Import any other modules (datetime, logging, etc.)

# TODO: Create your FastAPI application for EDM webhook handling
# Hint: Add a title about EDM webhook processing


# TODO: Create a basic test webhook endpoint for EDM testing
# Hint: @app.post("/test-webhook")
def handle_test_webhook(webhook_data: dict):
    """
    TODO: Handle test webhooks from EDM applets
    
    This endpoint receives manual test triggers from your EDM_WEBHOOK_TEST applet.
    Use this to verify your EDM-to-webhook communication is working.
    """
    
    # TODO: Process the test webhook data
    return {
        "webhook_handler": "EDM Test Webhook Received",
        "received_data": "TODO: Return webhook_data", 
        "device_source": "TODO: Extract device name from webhook_data",
        "event_type": "test_event",
        "status": "success",
        "message": "EDM webhook communication verified! 🎉"
    }


# TODO: Create interface alert webhook handler
# Hint: @app.post("/interface-alert")
def handle_interface_alert(interface_data: dict):
    """
    TODO: Handle interface status change alerts from EDM
    
    Expected data from INTERFACE_STATUS_WEBHOOK applet:
    {
        "event_type": "interface_change",
        "device": "device-name",
        "interface": "GigabitEthernet0/0/1", 
        "timestamp": "event-timestamp",
        "raw_message": "syslog-message"
    }
    
    Process the interface change and take appropriate action!
    """
    
    # TODO: Extract interface information
    device_name = "TODO: Get from interface_data"
    interface_name = "TODO: Get from interface_data" 
    event_timestamp = "TODO: Get from interface_data"
    
    # TODO: Determine interface status from raw message
    raw_message = interface_data.get("raw_message", "")
    if "down" in raw_message.lower():
        interface_status = "DOWN"
        severity = "HIGH"
        action_needed = "Investigate interface failure immediately"
    elif "up" in raw_message.lower():
        interface_status = "UP" 
        severity = "INFO"
        action_needed = "Interface recovery - monitor for stability"
    else:
        interface_status = "UNKNOWN"
        severity = "MEDIUM"
        action_needed = "Review interface status"
    
    # TODO: Return processed alert information
    return {
        "webhook_handler": "Interface Alert Processed",
        "device": device_name,
        "interface": interface_name,
        "status": interface_status,
        "severity": severity,
        "timestamp": event_timestamp,
        "recommended_action": action_needed,
        "alert_processed": True,
        "next_steps": "Alert logged and team notified"
    }


# TODO: Create CPU alert webhook handler 
# Hint: @app.post("/cpu-alert")
def handle_cpu_alert(cpu_data: dict):
    """
    TODO: Handle high CPU utilization alerts from EDM
    
    Expected data from CPU_HIGH_WEBHOOK applet:
    {
        "event_type": "high_cpu",
        "device": "device-name",
        "cpu_percent": "85",
        "timestamp": "event-timestamp", 
        "threshold": "80"
    }
    """
    
    # TODO: Extract CPU information
    device_name = "TODO: Get from cpu_data"
    cpu_percent = "TODO: Get from cpu_data"
    threshold = cpu_data.get("threshold", "80")
    
    # TODO: Determine severity based on CPU level
    cpu_value = float(cpu_percent) if cpu_percent else 0
    
    if cpu_value >= 95:
        severity = "CRITICAL" 
        action = "Immediate investigation required - potential service impact"
    elif cpu_value >= 85:
        severity = "HIGH"
        action = "Schedule maintenance window to investigate CPU usage"
    else:
        severity = "MEDIUM"
        action = "Monitor CPU trends - consider preventive maintenance"
    
    return {
        "webhook_handler": "CPU Alert Processed",
        "device": device_name,
        "cpu_utilization": f"{cpu_percent}%",
        "threshold_exceeded": f"{threshold}%",
        "severity": severity,
        "recommended_action": action,
        "alert_id": f"CPU-{device_name}-{cpu_percent}",
        "status": "processed"
    }


# TODO: Create memory alert webhook handler
# Hint: @app.post("/memory-alert") 
def handle_memory_alert(memory_data: dict):
    """
    TODO: Handle low memory alerts from EDM
    
    Expected data from MEMORY_WARNING_WEBHOOK applet:
    {
        "event_type": "low_memory",
        "device": "device-name",
        "memory_free_percent": "15",
        "timestamp": "event-timestamp"
    }
    """
    
    # TODO: Process memory alert data
    device_name = "TODO: Get from memory_data"
    memory_free = memory_data.get("memory_free_percent", "unknown")
    
    # TODO: Determine appropriate response
    return {
        "webhook_handler": "Memory Alert Processed", 
        "device": device_name,
        "memory_free": f"{memory_free}%",
        "status": "low_memory_detected",
        "recommended_action": "Review memory-intensive processes and consider cleanup",
        "alert_processed": True
    }


# TODO: Create configuration change webhook handler
# Hint: @app.post("/config-change")
def handle_config_change(config_data: dict):
    """
    TODO: Handle configuration change notifications from EDM
    
    Log configuration changes for audit and compliance purposes.
    """
    
    # TODO: Extract configuration change information
    device_name = "TODO: Get from config_data"
    change_timestamp = config_data.get("timestamp", "unknown")
    syslog_message = config_data.get("syslog_message", "")
    
    return {
        "webhook_handler": "Configuration Change Logged",
        "device": device_name,
        "change_time": change_timestamp,
        "change_details": syslog_message,
        "compliance_logged": True,
        "audit_trail": "Configuration change recorded for compliance review"
    }


# TODO: Create error pattern webhook handler
# Hint: @app.post("/error-alert")
def handle_error_alert(error_data: dict):
    """
    TODO: Handle critical error pattern alerts from EDM
    
    Process error/critical/alert syslog messages caught by EDM pattern matching.
    """
    
    # TODO: Process error alert
    device_name = "TODO: Get from error_data"
    error_message = error_data.get("error_message", "")
    error_timestamp = error_data.get("timestamp", "")
    
    return {
        "webhook_handler": "Error Alert Processed",
        "device": device_name,
        "error_detected": error_message,
        "timestamp": error_timestamp,
        "severity": "HIGH",
        "action_taken": "Error logged and escalated to operations team",
        "ticket_created": "AUTO-ERROR-" + device_name + "-" + error_timestamp[:10]
    }


# TODO: Create business hours alert handler
# Hint: @app.post("/business-alert")
def handle_business_hours_alert(business_data: dict):
    """
    TODO: Handle alerts that only trigger during business hours
    
    These are high-priority alerts that need immediate attention during work hours.
    """
    
    # TODO: Process business hours alert
    device_name = "TODO: Get from business_data"
    alert_hour = business_data.get("hour", "unknown")
    
    return {
        "webhook_handler": "Business Hours Alert",
        "device": device_name, 
        "alert_time": f"{alert_hour}:xx (business hours)",
        "priority": "IMMEDIATE",
        "escalation": "Alert sent to on-call engineer",
        "business_impact": "Potential impact during business hours - immediate response required"
    }


# TODO: Create health check webhook handler
# Hint: @app.post("/health-check")
def handle_health_check(health_data: dict):
    """
    TODO: Handle periodic health check webhooks from EDM
    
    Process regular health status reports from devices.
    """
    
    # TODO: Process health check data
    device_name = "TODO: Get from health_data"
    check_timestamp = health_data.get("timestamp", "")
    
    return {
        "webhook_handler": "Health Check Received",
        "device": device_name,
        "check_time": check_timestamp,
        "health_status": "received",
        "monitoring": "Device health data logged for trend analysis",
        "next_check": "Scheduled automatically by EDM applet"
    }


# TODO: Create a comprehensive webhook status endpoint
# Hint: @app.get("/webhook-status")
def get_webhook_status():
    """
    TODO: Provide status of your webhook handling system
    
    Show which EDM webhook endpoints are available and their purposes.
    """
    
    webhook_endpoints = {
        "test-webhook": "Manual EDM applet testing", 
        "interface-alert": "Interface status change notifications",
        "cpu-alert": "High CPU utilization alerts", 
        "memory-alert": "Low memory warnings",
        "config-change": "Configuration change audit logging",
        "error-alert": "Critical error pattern detection",
        "business-alert": "Business hours priority alerts",
        "health-check": "Periodic device health monitoring"
    }
    
    return {
        "webhook_server": "EDM Alert Handler",
        "status": "operational", 
        "available_endpoints": webhook_endpoints,
        "total_endpoints": len(webhook_endpoints),
        "edm_integration": "Ready to receive Cisco EDM applet webhooks",
        "documentation": "See edm_configurations.md for applet configurations"
    }


# TODO (Optional): Add logging and monitoring for webhook activities
# Ideas:
# - Log all incoming webhooks to a file
# - Count webhook types received 
# - Track device activity patterns
# - Store webhook history for analysis


if __name__ == "__main__":
    print("⚡ Cisco EDM Webhook Handler Server")
    print("=" * 50)
    print("To run this server:")
    print("1. Complete all TODO items above") 
    print("2. Run: uvicorn edm_webhook_server:app --reload --host 0.0.0.0 --port 8000")
    print("3. Configure EDM applets to point to this server")
    print("4. Visit: http://localhost:8000/docs")
    print()
    print("EDM Webhook Endpoints:")
    print("  POST /test-webhook      - EDM applet testing")
    print("  POST /interface-alert   - Interface status changes")
    print("  POST /cpu-alert        - CPU utilization alerts") 
    print("  POST /memory-alert     - Memory warnings")
    print("  POST /config-change    - Configuration change logs")
    print("  POST /error-alert      - Error pattern alerts")
    print("  POST /business-alert   - Business hours alerts")
    print("  POST /health-check     - Periodic health monitoring")
    print("  GET  /webhook-status   - Webhook system status")
    print()
    print("📋 Next Steps:")
    print("1. Deploy EDM applets from edm_configurations.md")
    print("2. Update webhook URLs in applet configurations") 
    print("3. Test with: event manager run WEBHOOK_TEST")
    print("4. Monitor webhook activity in server logs")
    print()
    print("🎉 Complete Event-Driven Automation Ready!")