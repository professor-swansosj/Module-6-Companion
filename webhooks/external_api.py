"""
External API Integration Webhooks
Module 6 - Reverse APIs and Event Driven Automation

This module demonstrates integrating external APIs within webhook endpoints.
Students will learn to make HTTP requests to external services.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
from datetime import datetime
import asyncio

router = APIRouter()

class JokeResponse(BaseModel):
    """Response model for dad joke"""
    joke: str
    source: str
    fetched_at: str
    webhook_message: str

class WeatherRequest(BaseModel):
    """Request model for weather webhook (example external API)"""
    city: str
    country_code: str = "US"

class APIResponse(BaseModel):
    """Generic API response model"""
    data: dict
    source_api: str
    success: bool
    timestamp: str
    processing_time_ms: float

@router.get("/dad-joke", response_model=JokeResponse)
async def fetch_dad_joke():
    """
    Webhook that fetches a random dad joke from an external API.
    
    This demonstrates:
    - Making HTTP requests to external APIs
    - Handling API responses
    - Error handling for external services
    - Combining external data with webhook responses
    
    Test with:
    curl -X GET http://localhost:8000/external/dad-joke
    """
    start_time = datetime.now()
    
    try:
        async with httpx.AsyncClient() as client:
            # Dad Jokes API - free and no auth required
            response = await client.get(
                "https://icanhazdadjoke.com/",
                headers={"Accept": "application/json"}
            )
            
            if response.status_code == 200:
                joke_data = response.json()
                return JokeResponse(
                    joke=joke_data["joke"],
                    source="icanhazdadjoke.com",
                    fetched_at=datetime.now().isoformat(),
                    webhook_message="Successfully fetched dad joke via webhook!"
                )
            else:
                raise HTTPException(
                    status_code=502, 
                    detail="Failed to fetch joke from external API"
                )
                
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Error connecting to joke API: {str(e)}"
        )

@router.get("/quote")
async def fetch_inspirational_quote():
    """
    Webhook that fetches an inspirational quote.
    
    Alternative external API example for students to explore.
    """
    try:
        async with httpx.AsyncClient() as client:
            # Quotable API - free quotes API
            response = await client.get("https://api.quotable.io/random")
            
            if response.status_code == 200:
                quote_data = response.json()
                return {
                    "quote": quote_data["content"],
                    "author": quote_data["author"],
                    "source": "quotable.io",
                    "fetched_at": datetime.now().isoformat(),
                    "webhook_message": "Inspirational quote delivered via webhook!"
                }
            else:
                raise HTTPException(
                    status_code=502,
                    detail="Failed to fetch quote from external API"
                )
                
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Error connecting to quote API: {str(e)}"
        )

@router.get("/multiple-apis")
async def fetch_multiple_apis():
    """
    Webhook that demonstrates calling multiple external APIs concurrently.
    
    This shows advanced concepts:
    - Concurrent API calls
    - Combining multiple data sources
    - Performance optimization with async/await
    """
    async def fetch_joke():
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://icanhazdadjoke.com/",
                headers={"Accept": "application/json"}
            )
            return response.json() if response.status_code == 200 else None

    async def fetch_quote():
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.quotable.io/random")
            return response.json() if response.status_code == 200 else None

    async def fetch_fact():
        async with httpx.AsyncClient() as client:
            response = await client.get("https://uselessfacts.jsph.pl/random.json?language=en")
            return response.json() if response.status_code == 200 else None

    # Fetch all APIs concurrently
    start_time = datetime.now()
    
    try:
        joke_task = asyncio.create_task(fetch_joke())
        quote_task = asyncio.create_task(fetch_quote())
        fact_task = asyncio.create_task(fetch_fact())
        
        joke, quote, fact = await asyncio.gather(joke_task, quote_task, fact_task)
        
        end_time = datetime.now()
        processing_time = (end_time - start_time).total_seconds() * 1000
        
        return {
            "content": {
                "joke": joke.get("joke") if joke else "Could not fetch joke",
                "quote": {
                    "text": quote.get("content") if quote else "Could not fetch quote",
                    "author": quote.get("author") if quote else "Unknown"
                },
                "fact": fact.get("text") if fact else "Could not fetch fact"
            },
            "metadata": {
                "sources": ["icanhazdadjoke.com", "quotable.io", "uselessfacts.jsph.pl"],
                "processing_time_ms": round(processing_time, 2),
                "fetched_at": end_time.isoformat(),
                "concurrent_requests": True
            },
            "webhook_message": "Multiple APIs called concurrently via webhook!"
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error in concurrent API calls: {str(e)}"
        )

@router.post("/webhook-chain")
async def webhook_chain_example(data: dict):
    """
    Example of webhook chaining - this webhook could trigger other webhooks.
    
    This demonstrates:
    - Processing incoming webhook data
    - Making decisions based on data
    - Potentially triggering other webhooks (chain reaction)
    """
    
    # Simulate processing the incoming data
    await asyncio.sleep(0.1)  # Simulate processing time
    
    # Based on the data, we might call different external APIs
    trigger_type = data.get("trigger", "default")
    
    if trigger_type == "joke":
        # Chain to joke API
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://icanhazdadjoke.com/",
                headers={"Accept": "application/json"}
            )
            external_data = response.json() if response.status_code == 200 else {}
    
    elif trigger_type == "quote":
        # Chain to quote API
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.quotable.io/random")
            external_data = response.json() if response.status_code == 200 else {}
    
    else:
        external_data = {"message": "No external API called"}
    
    return {
        "webhook_chain": {
            "received_data": data,
            "trigger_type": trigger_type,
            "external_response": external_data,
            "processed_at": datetime.now().isoformat()
        },
        "next_actions": [
            "Could trigger another webhook",
            "Could send notifications", 
            "Could update database",
            "Could perform network operations"
        ]
    }