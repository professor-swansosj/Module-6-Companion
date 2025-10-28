"""
Module 05: Network Operations via Webhooks

TODO: Build webhooks that connect to real network devices using Netmiko!
This is where your webhook server becomes a true network automation platform.

IMPORTANT: Use DevNet Sandbox devices for safe testing - never production devices!

Hint: Always handle network connection failures gracefully!
"""

# TODO: Import required modules for network operations
# Hint: from fastapi import FastAPI, HTTPException
# Hint: from netmiko import ConnectHandler
# TODO: Import any other modules (os for env vars, yaml for config, etc.)

# TODO: Create your FastAPI application
# Hint: Add a title about network automation capabilities


# DevNet Always-On Sandbox Device (safe to use!)
DEVNET_DEVICE = {
    'device_type': 'cisco_ios_xe',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    # TODO: Add any additional connection parameters you might need
    # Hint: 'timeout': 30, 'session_timeout': 60
}

# TODO: Alternative device for testing (comment out if not available)
# DEVNET_IOS_XR = {
#     'device_type': 'cisco_iosxr', 
#     'host': 'sandbox-iosxr-1.cisco.com',
#     'username': 'admin',
#     'password': 'C1sco12345',
# }


# TODO: Create a basic device information endpoint
# Hint: @app.get("/device/info")
def get_device_info():
    """
    TODO: Connect to DevNet device and get basic information
    
    Execute 'show version' command and return formatted response.
    This endpoint demonstrates basic Netmiko integration.
    """
    
    try:
        # TODO: Connect to device using Netmiko
        # Hint: with ConnectHandler(**DEVNET_DEVICE) as net_connect:
        
        # TODO: Execute 'show version' command
        # Hint: version_output = net_connect.send_command('show version')
        
        # TODO: Return formatted webhook response
        return {
            "webhook": "Device Information Retrieved",
            "device_host": "TODO: Get from DEVNET_DEVICE",
            "command_executed": "show version",
            "device_output": "TODO: Return version_output", 
            "status": "success",
            "timestamp": "TODO: Add current timestamp if desired"
        }
        
    except Exception as e:
        # TODO: Handle connection failures gracefully
        # Hint: Use HTTPException for proper HTTP error responses
        return {
            "error": f"Device connection failed: {str(e)}",
            "device_host": DEVNET_DEVICE['host'],
            "status": "failed",
            "troubleshooting": "Check device connectivity and credentials"
        }


# TODO: Create an interface status endpoint  
# Hint: @app.get("/device/interfaces")
def get_interface_status():
    """
    TODO: Get interface status from network device
    
    Execute 'show ip interface brief' and return interface information.
    Consider parsing the output into structured data.
    """
    
    try:
        # TODO: Connect to device
        
        # TODO: Execute 'show ip interface brief' 
        # Hint: interface_output = net_connect.send_command('show ip interface brief')
        
        # TODO: Optional - Parse output into structured format
        # For now, just return the raw output, but consider parsing later!
        
        return {
            "webhook": "Interface Status Retrieved",
            "command": "show ip interface brief",
            "interfaces": "TODO: Return interface_output or parsed data",
            "device": DEVNET_DEVICE['host'],
            "status": "success"
        }
        
    except Exception as e:
        return {
            "error": f"Failed to get interface status: {str(e)}",
            "status": "failed"
        }


# TODO: Create a custom command endpoint
# Hint: @app.post("/device/command")  
def execute_custom_command(command_data: dict):
    """
    TODO: Execute any show command via webhook parameter
    
    Expected input:
    {
        "command": "show ip route",
        "device": "optional-device-override"
    }
    
    SECURITY NOTE: Only allow 'show' commands for safety!
    """
    
    # TODO: Extract command from request data
    command = "TODO: Get command from command_data"
    
    # TODO: Validate command is safe (starts with 'show')
    if not command.lower().startswith('show'):
        return {
            "error": "Only 'show' commands are allowed for security",
            "command_received": command,
            "status": "rejected"
        }
    
    try:
        # TODO: Connect and execute the command
        # TODO: Return formatted response with command output
        
        return {
            "webhook": "Custom Command Executed",
            "command": command,
            "output": "TODO: Return command output",
            "device": DEVNET_DEVICE['host'],
            "status": "success"
        }
        
    except Exception as e:
        return {
            "error": f"Command execution failed: {str(e)}",
            "command": command,
            "status": "failed"
        }


# TODO: Create a network diagnostics webhook
# Hint: @app.post("/network/diagnose")
def network_diagnostics(issue_data: dict):
    """
    TODO: Run comprehensive diagnostics based on issue type
    
    Expected input:
    {
        "issue_type": "connectivity|performance|interface",
        "description": "Description of the issue", 
        "affected_interface": "optional interface name"
    }
    
    Run different commands based on issue_type!
    """
    
    issue_type = "TODO: Get from issue_data"
    description = "TODO: Get from issue_data"
    
    # TODO: Define diagnostic commands based on issue type
    if issue_type == "connectivity":
        commands = [
            "show ip interface brief",
            "show ip route", 
            "show arp"
        ]
    elif issue_type == "performance":
        commands = [
            "show processes cpu",
            "show memory statistics",
            "show interfaces"
        ]
    elif issue_type == "interface":
        commands = [
            "show ip interface brief",
            "show interfaces status",
            "show interfaces description"
        ]
    else:
        commands = ["show version"]  # Default command
    
    # TODO: Execute diagnostic commands
    diagnostic_results = []
    
    try:
        # TODO: Connect to device
        # TODO: Execute each command in the commands list
        # TODO: Collect results
        
        # For each command:
        #   output = net_connect.send_command(command)
        #   diagnostic_results.append({"command": command, "output": output})
        
        return {
            "webhook": "Network Diagnostics Completed",
            "issue_type": issue_type,
            "issue_description": description,
            "diagnostics_run": len(commands),
            "results": "TODO: Return diagnostic_results",
            "device": DEVNET_DEVICE['host'],
            "status": "success"
        }
        
    except Exception as e:
        return {
            "error": f"Diagnostics failed: {str(e)}",
            "issue_type": issue_type,
            "status": "failed"
        }


# TODO: Create a device health check endpoint
# Hint: @app.get("/device/health")
def device_health_check():
    """
    TODO: Run multiple commands to assess overall device health
    
    Check:
    - CPU utilization
    - Memory usage  
    - Interface status
    - Basic connectivity
    
    Return a health summary!
    """
    
    health_commands = {
        "cpu": "show processes cpu",
        "memory": "show memory statistics", 
        "interfaces": "show ip interface brief",
        "version": "show version"
    }
    
    health_report = {
        "webhook": "Device Health Check",
        "device": DEVNET_DEVICE['host'],
        "timestamp": "TODO: Add timestamp",
        "overall_status": "unknown",
        "checks": {}
    }
    
    try:
        # TODO: Connect to device
        # TODO: Execute each health command
        # TODO: Collect results for each check
        
        # For each command in health_commands:
        #   output = net_connect.send_command(command)
        #   health_report["checks"][check_name] = {"command": command, "output": output, "status": "success"}
        
        # TODO: Determine overall health status
        health_report["overall_status"] = "healthy"  # Simplify for now
        health_report["summary"] = "All health checks completed successfully"
        
        return health_report
        
    except Exception as e:
        health_report["overall_status"] = "unhealthy"
        health_report["error"] = f"Health check failed: {str(e)}"
        return health_report


# TODO (Optional): Create additional network operation endpoints
# Ideas:
# - @app.get("/device/routing") - Show routing table
# - @app.get("/device/arp") - Show ARP table  
# - @app.post("/device/ping") - Execute ping from device
# - @app.get("/device/logs") - Show recent logs


# TODO: Helper function for parsing interface output (Advanced)
def parse_interface_brief(output):
    """
    TODO: Parse 'show ip interface brief' output into structured data
    
    Convert raw text output into JSON format for easier consumption.
    This is optional but makes your webhook responses much more useful!
    """
    # TODO: Split output into lines
    # TODO: Parse each line into interface data
    # TODO: Return list of interface dictionaries
    
    interfaces = []
    # lines = output.split('\n')[1:]  # Skip header
    # for line in lines:
    #     if line.strip():
    #         # Parse interface data from line
    #         # Add to interfaces list
    
    return interfaces


if __name__ == "__main__":
    print("🔌 Network Operations via Webhooks Server")
    print("=" * 50) 
    print("To run this server:")
    print("1. Complete all TODO items above")
    print("2. Ensure DevNet sandbox is accessible")
    print("3. Run: uvicorn network_ops_server:app --reload --host 0.0.0.0 --port 8000")
    print("4. Visit: http://localhost:8000/docs")
    print()
    print("Available network operations:")
    print("  GET  /device/info        - Basic device information")
    print("  GET  /device/interfaces  - Interface status")
    print("  POST /device/command     - Execute custom show command")
    print("  POST /network/diagnose   - Run network diagnostics")
    print("  GET  /device/health      - Comprehensive health check")
    print()
    print("🏗️  DevNet Sandbox Device:")
    print(f"   Host: {DEVNET_DEVICE['host']}")
    print(f"   Type: {DEVNET_DEVICE['device_type']}")
    print()
    print("💡 Test with: curl http://localhost:8000/device/info")
    print("⚠️  Remember: Only use sandbox devices for testing!")
    print("🔒 Security: Only 'show' commands are allowed")