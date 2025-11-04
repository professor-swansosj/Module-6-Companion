"""
Section 03: Multiple Paths & Creative Responses

TODO: Build a webhook server with multiple creative endpoints!
This module focuses on different paths, response types, and adding personality.

Hint: Start with simple endpoints, then make them more creative!
"""

# TODO: Import FastAPI and response types
# Hint: from fastapi import FastAPI, Response
# Hint: from fastapi.responses import HTMLResponse
# TODO: Import any other modules you need (random, datetime, etc.)

# TODO: Create your FastAPI application instance
# Hint: Add a title and description to make it professional


# TODO: Create a root endpoint that returns server information
# Hint: @app.get("/")
def root():
    """
    TODO: Return basic information about your webhook server
    
    Include:
    - Server name/title
    - Available endpoints  
    - Instructions for getting started
    
    Make it welcoming and informative!
    """
    return {
        "server": "TODO: Add server name",
        "message": "TODO: Add welcome message",
        "endpoints": "TODO: List your available endpoints"
    }


# TODO: Create an ASCII art endpoint
# Hint: @app.get("/ascii") 
def ascii_art():
    """
    TODO: Return fun ASCII art related to networking or webhooks
    
    Use Response(content, media_type="text/plain") for proper text display
    
    Ideas for ASCII art:
    - Network diagram
    - Webhook flow
    - Server status
    - Router/switch representation
    """
    
    # TODO: Create your ASCII art (use triple quotes for multi-line)
    art = """
    TODO: Add your creative ASCII art here!
    
    Ideas:
    🌐 Network diagram
    📡 Webhook flow  
    🖥️  Server status
    """
    
    # TODO: Return as plain text response
    # Hint: return Response(art, media_type="text/plain")
    pass


# TODO: Create a status endpoint with query parameter support
# Hint: @app.get("/status")
def get_status(format: str = "json"):
    """
    TODO: Return server status in different formats
    
    Support query parameters:
    - /status (default JSON)
    - /status?format=json (JSON format)
    - /status?format=ascii (ASCII art format)
    - /status?format=html (HTML format)
    """
    
    if format == "ascii":
        # TODO: Return ASCII status art
        ascii_status = """
        TODO: Create ASCII status display
        
        Example:
        ✅ SERVER STATUS ✅
        ==================
        🔋 Power: Good
        📡 Network: Connected
        💾 Memory: Available
        """
        # TODO: Return as plain text
        pass
        
    elif format == "html":
        # TODO: Return HTML status page
        html_content = """
        <h1>🚀 Webhook Server Status</h1>
        <p>TODO: Add HTML status information</p>
        <ul>
            <li>Status: Healthy</li>
            <li>Uptime: Running</li>
            <li>Endpoints: Active</li>
        </ul>
        """
        # TODO: Return as HTML response
        pass
        
    else:
        # TODO: Return JSON status (default)
        return {
            "status": "TODO: Add status",
            "server": "webhook-server",
            "endpoints_active": "TODO: Count or list active endpoints"
        }


# TODO: Create an echo endpoint that reflects back what you send
# Hint: @app.post("/echo")
def echo_webhook(data: dict):
    """
    TODO: Create an echo webhook that returns what you send it
    
    This is useful for testing webhook payloads.
    Return the received data along with some metadata.
    """
    # TODO: Import datetime if you want timestamps
    # from datetime import datetime
    
    return {
        "echo": "TODO: Return the received data",
        "received_at": "TODO: Add timestamp",
        "message": "Echo webhook received your data!"
    }


# TODO: Create a random response endpoint  
# Hint: @app.get("/random")
def random_response():
    """
    TODO: Return a different response each time it's called
    
    Ideas:
    - Random network facts
    - Random motivational messages
    - Random ASCII art
    - Random status messages
    """
    
    # TODO: Import random module if needed
    # import random
    
    # TODO: Create lists of random content
    responses = [
        "TODO: Add random response 1",
        "TODO: Add random response 2", 
        "TODO: Add random response 3"
    ]
    
    # TODO: Return a random choice
    return {"message": "TODO: Return random.choice(responses)"}


# TODO: Create a path parameter endpoint
# Hint: @app.get("/device/{device_type}")
def device_info(device_type: str):
    """
    TODO: Return information based on the device type in the URL
    
    Examples:
    - /device/router
    - /device/switch
    - /device/firewall
    
    Return different information for each device type.
    """
    
    # TODO: Create device information based on device_type
    device_data = {
        "router": "TODO: Add router info",
        "switch": "TODO: Add switch info", 
        "firewall": "TODO: Add firewall info"
    }
    
    # TODO: Return appropriate device information
    return {
        "device_type": device_type,
        "info": "TODO: Get info from device_data or default message"
    }


# TODO (Optional): Add any creative endpoints you want!
# Ideas:
# - Network joke endpoint
# - Current time in different formats
# - Simple calculator for network subnets
# - Server statistics
# - Fun facts about networking

# TODO: @app.get("/joke") - Network jokes
# TODO: @app.get("/time") - Current time with ASCII art
# TODO: @app.get("/calc/{subnet}") - Simple subnet info


if __name__ == "__main__":
    print("🛤️  Multiple Paths & Creative Responses Server")
    print("=" * 50)
    print("To run this server:")
    print("1. Complete all TODO items above")
    print("2. Run: uvicorn paths_server:app --reload --host 0.0.0.0 --port 8000")
    print("3. Visit: http://localhost:8000/docs")
    print()
    print("Planned endpoints:")
    print("  GET  /              - Server information")
    print("  GET  /ascii         - ASCII art display")
    print("  GET  /status        - Status (supports ?format=ascii/html/json)")
    print("  POST /echo          - Echo webhook")
    print("  GET  /random        - Random responses")
    print("  GET  /device/{type} - Device information")
    print()
    print("💡 Try different formats: /status?format=ascii")
    print("🎨 Make it creative and fun!")
