"""
Module 6 - Reverse APIs and Event Driven Automation
FastAPI Webhook Application

This is the main application file that brings together all webhook endpoints
for the Software Defined Networking course Module 6.

Author: Course Instructor
Course: Software Defined Networking (Network Automation)
Module: 6 - Reverse APIs and Event Driven Automation
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import uvicorn

# Import webhook modules
from webhooks.basic import router as basic_router
from webhooks.external_api import router as external_api_router
from webhooks.netmiko_ops import router as netmiko_router
from webhooks.restconf_ops import router as restconf_router
from webhooks.netconf_ops import router as netconf_router

# Create FastAPI application instance
app = FastAPI(
    title="Module 6 - Webhook & Event Driven Automation",
    description="Companion repository for SDN Module 6 - Reverse APIs and Event Driven Automation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include routers from different webhook modules
app.include_router(basic_router, prefix="/basic", tags=["Basic Webhooks"])
app.include_router(external_api_router, prefix="/external", tags=["External APIs"])
app.include_router(netmiko_router, prefix="/netmiko", tags=["Netmiko Operations"])
app.include_router(restconf_router, prefix="/restconf", tags=["RESTCONF Operations"])
app.include_router(netconf_router, prefix="/netconf", tags=["NETCONF Operations"])

@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Welcome page for the Module 6 Webhook Application
    """
    return """
    <html>
        <head>
            <title>Module 6 - Webhook & Event Driven Automation</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .header { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
                .section { margin: 20px 0; }
                .endpoint { background-color: #ecf0f1; padding: 10px; margin: 5px 0; border-radius: 5px; }
                .method { font-weight: bold; color: #27ae60; }
                a { color: #3498db; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Module 6 - Reverse APIs and Event Driven Automation</h1>
                <p><strong>Course:</strong> Software Defined Networking (Network Automation)</p>
            </div>
            
            <div class="section">
                <h2>Welcome!</h2>
                <p>This is your FastAPI webhook application for Module 6. Use this application to practice building reverse APIs and event-driven automation.</p>
            </div>
            
            <div class="section">
                <h2>Available Endpoints</h2>
                
                <h3>Basic Webhooks</h3>
                <div class="endpoint">
                    <span class="method">GET</span> /basic/message - Simple message return webhook
                </div>
                <div class="endpoint">
                    <span class="method">POST</span> /basic/echo - Echo back received data
                </div>
                
                <h3>External API Integration</h3>
                <div class="endpoint">
                    <span class="method">GET</span> /external/dad-joke - Fetch a random dad joke
                </div>
                
                <h3>Network Operations</h3>
                <div class="endpoint">
                    <span class="method">POST</span> /netmiko/command - Execute command via Netmiko
                </div>
                <div class="endpoint">
                    <span class="method">GET</span> /restconf/interfaces - Get interfaces via RESTCONF
                </div>
                <div class="endpoint">
                    <span class="method">GET</span> /netconf/config - Get configuration via NETCONF
                </div>
            </div>
            
            <div class="section">
                <h2>Documentation</h2>
                <p>📚 <a href="/docs">Interactive API Documentation (Swagger UI)</a></p>
                <p>📖 <a href="/redoc">Alternative API Documentation (ReDoc)</a></p>
            </div>
            
            <div class="section">
                <h2>Testing</h2>
                <p>Test your webhooks using:</p>
                <ul>
                    <li><strong>cURL:</strong> Check the <code>tests/curl_examples.sh</code> file</li>
                    <li><strong>Browser:</strong> Visit the endpoints directly for GET requests</li>
                    <li><strong>Postman:</strong> Import the API documentation</li>
                    <li><strong>Interactive Docs:</strong> Use the /docs page for testing</li>
                </ul>
            </div>
        </body>
    </html>
    """

@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring the application status
    """
    return {
        "status": "healthy",
        "message": "Module 6 Webhook Application is running",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    # Run the application directly if this file is executed
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )