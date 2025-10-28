"""
Module 02: Your First FastAPI Webhook Server

TODO: Complete this file to create a working FastAPI webhook server!
Follow the TODO comments to build your server step by step.

Hint: Start simple - just get a basic endpoint working, then add more!
"""

# TODO: Import FastAPI framework
# Hint: from fastapi import FastAPI

# TODO: Import any other modules you might need
# Consider: What if you want to include timestamps or random responses?

# TODO: Create your FastAPI application instance
# Hint: app = FastAPI(title="Your Webhook Server", version="1.0.0")


# TODO: Create a root endpoint that responds to GET requests at "/"
# Hint: Use @app.get("/") decorator
def read_root():
    """
    TODO: Return a simple greeting message as a dictionary
    
    This endpoint will be available at: http://localhost:8000/
    
    Example return: {"message": "Welcome to my webhook server!"}
    """
    # TODO: Replace this with your own greeting
    return {"message": "TODO: Add your greeting here"}


# TODO: Create a webhook endpoint that responds to POST requests
# Hint: Use @app.post("/webhook") decorator  
def receive_webhook():
    """
    TODO: Create your first webhook endpoint!
    
    This endpoint will be available at: http://localhost:8000/webhook
    
    For now, just return a simple confirmation message.
    Later modules will show you how to accept and process data.
    
    Example return: {"status": "received", "message": "Webhook processed successfully"}
    """
    # TODO: Return a dictionary confirming the webhook was received
    return {"status": "TODO", "message": "TODO: Add your webhook response"}


# TODO (Optional): Add a fun endpoint that returns something interesting
# Ideas: Random network fact, ASCII art, current timestamp, etc.
# Hint: Use @app.get("/fun") decorator
def fun_endpoint():
    """
    TODO: Make this endpoint return something fun!
    
    Ideas:
    - Random networking joke or fact
    - ASCII art  
    - Current timestamp
    - Server status information
    - Anything that shows personality!
    """
    # TODO: Make this fun and unique to you!
    return {"message": "TODO: Add something fun here!"}


# TODO: Add a status/health check endpoint
# Hint: Use @app.get("/health") decorator
def health_check():
    """
    TODO: Create a health check endpoint
    
    This is useful for monitoring tools to verify your webhook server is running.
    Should return simple status information.
    
    Example return: {"status": "healthy", "service": "webhook-server"}
    """
    # TODO: Return health status information
    return {"status": "TODO", "service": "webhook-server"}


if __name__ == "__main__":
    # TODO: Add instructions for running the server
    print("🚀 FastAPI Webhook Server")
    print("=" * 40)
    print("To run this server:")
    print("1. Make sure you're in the 02_first_server/ directory")  
    print("2. Run: uvicorn server:app --reload --host 0.0.0.0 --port 8000")
    print("3. Visit: http://localhost:8000/docs")
    print()
    print("Available endpoints after completing TODOs:")
    print("  GET  /          - Root greeting")
    print("  POST /webhook   - Webhook receiver") 
    print("  GET  /fun       - Fun endpoint")
    print("  GET  /health    - Health check")
    print() 
    print("💡 Tip: Use --reload to automatically restart when you edit this file!")