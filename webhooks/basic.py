"""
Basic Webhook Endpoints
Module 6 - Reverse APIs and Event Driven Automation

This module contains simple webhook endpoints for learning basic concepts.
Students will start here to understand how webhooks work.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any

router = APIRouter()

class MessageResponse(BaseModel):
    """Response model for simple messages"""
    message: str
    timestamp: str
    status: str

class EchoRequest(BaseModel):
    """Request model for echo endpoint"""
    data: Dict[str, Any]
    sender: str = "unknown"

class EchoResponse(BaseModel):
    """Response model for echo endpoint"""
    received_data: Dict[str, Any]
    sender: str
    processed_at: str
    echo_message: str

@router.get("/message", response_model=MessageResponse)
async def simple_message():
    """
    Simple webhook that returns a message.
    
    This is the first webhook students will create. It demonstrates:
    - Basic FastAPI endpoint structure
    - Response models with Pydantic
    - JSON response formatting
    
    Test with:
    curl -X GET http://localhost:8000/basic/message
    """
    return MessageResponse(
        message="Hello from your first webhook! This is a reverse API in action.",
        timestamp=datetime.now().isoformat(),
        status="success"
    )

@router.post("/echo", response_model=EchoResponse)
async def echo_webhook(request: EchoRequest):
    """
    Echo webhook that returns the received data.
    
    This webhook demonstrates:
    - Receiving POST data
    - Request/Response models
    - Data validation with Pydantic
    - Processing incoming webhook data
    
    Test with:
    curl -X POST http://localhost:8000/basic/echo \\
         -H "Content-Type: application/json" \\
         -d '{"data": {"key": "value", "number": 42}, "sender": "student"}'
    """
    return EchoResponse(
        received_data=request.data,
        sender=request.sender,
        processed_at=datetime.now().isoformat(),
        echo_message=f"Successfully received data from {request.sender}"
    )

@router.get("/info")
async def webhook_info():
    """
    Information about basic webhooks.
    
    This endpoint provides educational content about webhook concepts.
    """
    return {
        "webhook_concept": "Reverse APIs that receive HTTP requests",
        "event_driven": "Triggered by external events or requests",
        "benefits": [
            "Real-time data processing",
            "Reduced polling overhead", 
            "Immediate response to events",
            "Scalable architecture"
        ],
        "use_cases": [
            "Payment processing notifications",
            "Git repository events",
            "IoT sensor data collection",
            "Network device status updates",
            "Automated incident response"
        ],
        "module_learning_objectives": [
            "Understand webhook architecture",
            "Build FastAPI endpoints",
            "Handle HTTP requests and responses",
            "Integrate with external systems",
            "Implement network automation triggers"
        ]
    }

@router.get("/status/{status_code}")
async def test_status_codes(status_code: int):
    """
    Test different HTTP status codes.
    
    This endpoint helps students understand HTTP status codes in webhooks.
    
    Test with:
    curl -X GET http://localhost:8000/basic/status/200
    curl -X GET http://localhost:8000/basic/status/404
    """
    if status_code == 200:
        return {"message": "Success!", "code": 200}
    elif status_code == 201:
        return {"message": "Created!", "code": 201}
    elif status_code == 400:
        raise HTTPException(status_code=400, detail="Bad Request Example")
    elif status_code == 404:
        raise HTTPException(status_code=404, detail="Not Found Example")
    elif status_code == 500:
        raise HTTPException(status_code=500, detail="Internal Server Error Example")
    else:
        raise HTTPException(status_code=status_code, detail=f"Custom status code: {status_code}")