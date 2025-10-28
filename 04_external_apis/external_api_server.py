"""
Module 04: External APIs & Data Integration

TODO: Build webhook endpoints that integrate with external APIs!
Focus on the Dad Jokes API, error handling, and combining data sources.

Hint: Always handle API failures gracefully - external services can be unreliable!
"""

# TODO: Import required modules
# Hint: from fastapi import FastAPI, HTTPException
# Hint: import requests (for making HTTP requests)
# TODO: Import any other modules you might need (datetime, json, etc.)

# TODO: Create your FastAPI application
# Hint: Add a good title and description about API integration


# TODO: Create a simple dad joke endpoint
# Hint: @app.get("/joke")
def get_dad_joke():
    """
    TODO: Call the Dad Jokes API and return a joke
    
    API Details:
    - URL: https://icanhazdadjoke.com/
    - Method: GET  
    - Headers: {"Accept": "application/json"}
    - Response: {"id": "...", "joke": "...", "status": 200}
    
    Return the joke in a nice format with your own message!
    """
    
    try:
        # TODO: Make request to Dad Jokes API
        # Hint: response = requests.get("URL", headers={"Accept": "application/json"})
        
        # TODO: Check if request was successful
        # Hint: response.raise_for_status() or check response.status_code
        
        # TODO: Parse the JSON response
        # Hint: joke_data = response.json()
        
        # TODO: Return formatted response
        return {
            "webhook": "Dad Joke API Integration",
            "joke": "TODO: Get joke from joke_data",
            "joke_id": "TODO: Get id from joke_data", 
            "message": "Hope this brightens your day! 😄"
        }
        
    except Exception as e:
        # TODO: Handle errors gracefully
        return {
            "error": f"Failed to get joke: {str(e)}",
            "fallback_joke": "Why don't network engineers tell dad jokes? Because they prefer TCP jokes - they're more reliable!"
        }


# TODO: Create a formatted joke endpoint with query parameters
# Hint: @app.get("/joke/formatted")
def get_formatted_joke(format_style: str = "standard"):
    """
    TODO: Get a dad joke and format it based on query parameter
    
    Support different formats:
    - /joke/formatted?format_style=standard (default)
    - /joke/formatted?format_style=ascii
    - /joke/formatted?format_style=network
    
    Make each format unique and fun!
    """
    
    # TODO: Get joke from API (reuse logic from above)
    try:
        # TODO: Make API call
        pass
        
        if format_style == "ascii":
            # TODO: Return joke with ASCII art frame
            formatted_joke = f"""
            ╔══════════════════════════════════════╗
            ║           DAD JOKE ALERT!            ║
            ╠══════════════════════════════════════╣
            ║ TODO: Insert joke here               ║
            ╚══════════════════════════════════════╝
            """
            # TODO: Return as plain text or structured response
            
        elif format_style == "network":
            # TODO: Return joke with network-themed formatting
            return {
                "packet_type": "JOKE_FRAME",
                "source": "Dad Jokes API",
                "destination": "Your Funny Bone",
                "payload": "TODO: Insert joke here",
                "checksum": "😄 VALID",
                "ttl": "Until next reboot"
            }
            
        else:  # standard format
            # TODO: Return standard formatted joke
            return {
                "joke": "TODO: Insert joke here",
                "format": "standard",
                "api_source": "icanhazdadjoke.com"
            }
            
    except Exception as e:
        return {"error": f"Joke formatting failed: {str(e)}"}


# TODO: Create a network alert webhook that includes a mood booster
# Hint: @app.post("/network-alert")
def network_alert_with_mood_booster(alert_data: dict):
    """
    TODO: Process network alerts and add a dad joke to boost team morale
    
    Expected alert_data format:
    {
        "device": "router-01",
        "severity": "high|medium|low", 
        "message": "Description of the alert",
        "timestamp": "optional timestamp"
    }
    
    Combine the alert processing with a dad joke API call!
    """
    
    # TODO: Process the network alert
    alert_response = {
        "alert_processed": True,
        "device": "TODO: Get from alert_data",
        "severity": "TODO: Get from alert_data", 
        "status": "Alert received and logged",
        "processed_at": "TODO: Add current timestamp"
    }
    
    # TODO: Add team morale booster (dad joke)
    try:
        # TODO: Call dad jokes API
        # TODO: Add joke to alert_response
        alert_response["team_morale_booster"] = "TODO: Add joke here"
        alert_response["morale_message"] = "Alert handled! Here's something to smile about:"
        
    except Exception as e:
        # TODO: Fallback if jokes API fails
        alert_response["team_morale_booster"] = "No joke available, but you're handling this alert like a pro! 🚀"
        alert_response["morale_message"] = "Keep up the great work!"
    
    return alert_response


# TODO: Create a multi-API endpoint (advanced)
# Hint: @app.get("/network-status-deluxe")
def deluxe_network_status():
    """
    TODO: Create an endpoint that combines multiple data sources
    
    Ideas to combine:
    1. Your server status
    2. Dad joke for team morale
    3. Current timestamp
    4. Maybe weather API if you're feeling adventurous
    
    This shows how webhooks can enrich data from multiple sources!
    """
    
    # TODO: Collect local server info
    server_info = {
        "server_name": "Webhook Server Deluxe",
        "status": "operational", 
        "endpoints_active": "TODO: Count your endpoints"
    }
    
    # TODO: Get external data (dad joke)
    try:
        # TODO: Call dad jokes API
        mood_booster = "TODO: Get joke from API"
    except:
        mood_booster = "API unavailable, but your network skills are still amazing!"
    
    # TODO: Combine everything into a deluxe response
    return {
        "network_overview": server_info,
        "team_mood_boost": mood_booster,
        "status_summary": "All systems nominal, team morale high!",
        "generated_at": "TODO: Add timestamp"
    }


# TODO: Create an API health check endpoint
# Hint: @app.get("/api-health")
def check_api_health():
    """
    TODO: Check if external APIs are reachable
    
    Test connectivity to Dad Jokes API and report status.
    This is useful for monitoring your webhook dependencies.
    """
    
    health_report = {
        "webhook_server": "healthy",
        "external_apis": {}
    }
    
    # TODO: Test Dad Jokes API
    try:
        # TODO: Make a quick test request
        # Hint: Set a short timeout for fast health checks
        # response = requests.get("URL", timeout=3)
        
        health_report["external_apis"]["dad_jokes"] = {
            "status": "TODO: healthy or unhealthy",
            "response_time": "TODO: Measure if you want",
            "last_checked": "TODO: Current timestamp"
        }
        
    except Exception as e:
        health_report["external_apis"]["dad_jokes"] = {
            "status": "unhealthy",
            "error": str(e),
            "last_checked": "TODO: Current timestamp"
        }
    
    return health_report


# TODO (Optional): Add your own creative API integration!
# Ideas:
# - Weather API integration for location-based responses  
# - Random quote API for inspiration
# - Network status from a fake monitoring API
# - Combine multiple joke APIs for variety


if __name__ == "__main__":
    print("🌐 External APIs & Data Integration Server")
    print("=" * 50)
    print("To run this server:")
    print("1. Complete all TODO items above")
    print("2. Run: uvicorn external_api_server:app --reload --host 0.0.0.0 --port 8000")
    print("3. Visit: http://localhost:8000/docs")
    print()
    print("Planned endpoints:")
    print("  GET  /joke                    - Simple dad joke")
    print("  GET  /joke/formatted         - Formatted joke (supports ?format_style=)")
    print("  POST /network-alert          - Network alert with morale booster")
    print("  GET  /network-status-deluxe  - Multi-API integration")
    print("  GET  /api-health             - Check external API status")
    print()
    print("💡 Test API integration:")
    print("   curl http://localhost:8000/joke")
    print("🎨 Remember: Always handle API failures gracefully!")
    print("😄 Dad Jokes API: https://icanhazdadjoke.com/")