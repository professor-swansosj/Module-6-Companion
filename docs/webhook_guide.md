# Webhook Implementation Guide

## Module 6 - Reverse APIs and Event Driven Automation

This guide provides detailed instructions for implementing and understanding webhooks in the context of network automation.

## Table of Contents

1. [Understanding Webhooks](#understanding-webhooks)
2. [FastAPI Basics](#fastapi-basics)
3. [Implementation Steps](#implementation-steps)
4. [Testing Your Webhooks](#testing-your-webhooks)
5. [Network Integration](#network-integration)
6. [Troubleshooting](#troubleshooting)

## Understanding Webhooks

Webhooks are **HTTP callbacks** that allow applications to provide real-time information to other applications. They are sometimes called "reverse APIs" because instead of your application requesting data from an API, the webhook pushes data to your application when events occur.

### Key Characteristics

- **Event-driven**: Triggered by specific events
- **Push-based**: Data is sent to you, not requested
- **Real-time**: Immediate notification of events
- **HTTP-based**: Uses standard HTTP methods (GET, POST, PUT, DELETE)

### Common Use Cases in Network Automation

- **Device alerts**: Router/switch sends notification when interface goes down
- **Configuration changes**: Automatic backup when configuration is modified
- **Monitoring**: Real-time performance metrics delivery
- **Incident response**: Automatic remediation based on network events

## FastAPI Basics

FastAPI is a modern Python web framework that makes building APIs simple and fast.

### Basic Structure

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### Key Components

1. **Router**: Organizes endpoints into logical groups
2. **Pydantic Models**: Define request/response data structures
3. **Dependency Injection**: Share common functionality
4. **Automatic Documentation**: Generated API docs

## Implementation Steps

### Step 1: Basic Webhook

Start with a simple message-returning webhook:

```python
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/message")
async def simple_webhook():
    return {
        "message": "Hello from webhook!",
        "timestamp": datetime.now().isoformat(),
        "status": "success"
    }
```

### Step 2: Data Processing Webhook

Accept and process incoming data:

```python
from pydantic import BaseModel

class WebhookData(BaseModel):
    event_type: str
    data: dict
    source: str

@router.post("/process-event")
async def process_webhook(webhook_data: WebhookData):
    # Process the incoming data
    processed_data = {
        "received": webhook_data.dict(),
        "processed_at": datetime.now().isoformat(),
        "action_taken": "Data logged and processed"
    }
    return processed_data
```

### Step 3: External API Integration

Make HTTP requests to external services:

```python
import httpx

@router.get("/external-data")
async def fetch_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
        if response.status_code == 200:
            return {
                "external_data": response.json(),
                "fetched_at": datetime.now().isoformat()
            }
        else:
            raise HTTPException(status_code=502, detail="External API error")
```

### Step 4: Network Device Integration

Connect to network devices using Netmiko:

```python
from netmiko import ConnectHandler

@router.post("/network-command")
async def execute_command(device_info: dict, command: str):
    try:
        # In production, use proper error handling and connection management
        connection = ConnectHandler(**device_info)
        output = connection.send_command(command)
        connection.disconnect()
        
        return {
            "device": device_info["host"],
            "command": command,
            "output": output,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Network error: {str(e)}")
```

## Testing Your Webhooks

### Using cURL

Test GET endpoints:

```bash
curl -X GET http://localhost:8000/basic/message
```

Test POST endpoints:

```bash
curl -X POST http://localhost:8000/basic/echo \
     -H "Content-Type: application/json" \
     -d '{"data": {"key": "value"}, "sender": "test"}'
```

### Using Python Requests

```python
import requests

# Test GET endpoint
response = requests.get("http://localhost:8000/basic/message")
print(response.json())

# Test POST endpoint
data = {"data": {"key": "value"}, "sender": "test"}
response = requests.post("http://localhost:8000/basic/echo", json=data)
print(response.json())
```

### Using FastAPI Interactive Docs

1. Start your application: `uvicorn main:app --reload`
2. Open browser to: `http://localhost:8000/docs`
3. Test endpoints directly in the browser

## Network Integration

### RESTCONF Integration

RESTCONF uses HTTP methods to interact with network devices:

```python
@router.get("/interfaces/{device_ip}")
async def get_interfaces(device_ip: str):
    url = f"https://{device_ip}/restconf/data/ietf-interfaces:interfaces"
    headers = {"Accept": "application/yang-data+json"}
    
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(
            url, 
            headers=headers,
            auth=("admin", "admin")
        )
        return response.json()
```

### NETCONF Integration

NETCONF uses XML over SSH:

```python
from ncclient import manager

@router.get("/netconf-config/{device_ip}")
async def get_config(device_ip: str):
    with manager.connect(
        host=device_ip,
        port=830,
        username="admin",
        password="admin",
        hostkey_verify=False
    ) as m:
        config = m.get_config(source="running")
        return {"config": config.data_xml}
```

## Error Handling Best Practices

### 1. Use Appropriate HTTP Status Codes

```python
from fastapi import HTTPException

@router.get("/device/{device_ip}")
async def get_device_status(device_ip: str):
    try:
        # Attempt to connect to device
        status = check_device_status(device_ip)
        return status
    except ConnectionError:
        raise HTTPException(
            status_code=503, 
            detail="Device unreachable"
        )
    except AuthenticationError:
        raise HTTPException(
            status_code=401,
            detail="Authentication failed"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal error: {str(e)}"
        )
```

### 2. Implement Retry Logic

```python
import asyncio
from typing import Optional

async def retry_operation(
    operation, 
    max_attempts: int = 3, 
    delay: float = 1.0
) -> Optional[dict]:
    for attempt in range(max_attempts):
        try:
            result = await operation()
            return result
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            await asyncio.sleep(delay * (2 ** attempt))  # Exponential backoff
    return None
```

### 3. Validate Input Data

```python
from pydantic import BaseModel, validator

class DeviceConfig(BaseModel):
    host: str
    username: str
    password: str
    device_type: str
    
    @validator('host')
    def validate_ip(cls, v):
        # Add IP address validation
        import ipaddress
        try:
            ipaddress.ip_address(v)
        except ValueError:
            raise ValueError('Invalid IP address')
        return v
    
    @validator('device_type')
    def validate_device_type(cls, v):
        allowed_types = ['cisco_ios', 'cisco_xe', 'juniper_junos']
        if v not in allowed_types:
            raise ValueError(f'Device type must be one of: {allowed_types}')
        return v
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Connection Timeout

**Symptom**: Webhook hangs or times out
**Solution**

- Increase timeout values
- Check network connectivity
- Verify device credentials

#### 2. Import Errors

**Symptom**: `ModuleNotFoundError`
**Solution**:

- Ensure virtual environment is activated
- Install missing packages: `pip install -r requirements.txt`

#### 3. JSON Serialization Errors

**Symptom**: `Object of type datetime is not JSON serializable`
**Solution**:

```python
from datetime import datetime
import json

# Use ISO format for dates
data = {
    "timestamp": datetime.now().isoformat(),
    "message": "Success"
}
```

#### 4. CORS Issues (when testing from browser)

**Symptom**: Browser blocks requests
**Solution**:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Debugging Tips

1. **Use logging**:

```python
import logging

logger = logging.getLogger(__name__)

@router.post("/debug-webhook")
async def debug_webhook(data: dict):
    logger.info(f"Received data: {data}")
    # Process data
    logger.info("Processing completed")
    return {"status": "success"}
```

2. **Test incrementally**:
   - Start with simple endpoints
   - Add complexity gradually
   - Test each component independently

3. **Use simulation mode**:
   - Test without real network devices first
   - Use mock responses for external APIs
   - Validate logic before connecting to real systems

## Security Considerations

### 1. Authentication

```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "secret":
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    return credentials.username

@router.get("/secure-endpoint")
async def secure_endpoint(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}!"}
```

### 2. Rate Limiting

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

@router.get("/rate-limited")
@limiter.limit("5/minute")
async def rate_limited_endpoint(request: Request):
    return {"message": "This endpoint is rate limited"}
```

### 3. Input Validation

Always validate and sanitize input data to prevent injection attacks and ensure data integrity.

## Next Steps

After mastering basic webhooks:

1. **Explore async patterns**: Learn about concurrent webhook processing
2. **Add persistence**: Store webhook data in databases
3. **Implement queuing**: Use message queues for reliable processing
4. **Monitor and log**: Add comprehensive logging and monitoring
5. **Scale horizontally**: Deploy multiple webhook instances

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Netmiko Documentation](https://github.com/ktbyers/netmiko)
- [RESTCONF RFC 8040](https://tools.ietf.org/html/rfc8040)
- [NETCONF RFC 6241](https://tools.ietf.org/html/rfc6241)
- [Webhook Best Practices](https://webhooks.fyi/)

Remember: The key to successful webhook implementation is starting simple and building complexity gradually while maintaining robust error handling and testing practices.