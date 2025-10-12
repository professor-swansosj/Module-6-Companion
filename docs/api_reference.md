# API Reference Documentation

## Module 6 - Reverse APIs and Event Driven Automation

Complete reference for all webhook endpoints available in this module.

---

## Base URL

```bash
http://localhost:8000
```

## Authentication

Most endpoints in this learning module do not require authentication. In production environments, proper authentication should be implemented.

---

## Basic Webhooks

### GET /basic/message

Returns a simple message to demonstrate basic webhook functionality.

**Response Example:**

```json
{
  "message": "Hello from your first webhook! This is a reverse API in action.",
  "timestamp": "2024-01-15T10:30:00.123456",
  "status": "success"
}
```

### POST /basic/echo

Echoes back the received data to demonstrate POST request handling.

**Request Body:**

```json
{
  "data": {
    "key": "value",
    "number": 42
  },
  "sender": "student"
}
```

**Response Example:**

```json
{
  "received_data": {
    "key": "value",
    "number": 42
  },
  "sender": "student",
  "processed_at": "2024-01-15T10:30:00.123456",
  "echo_message": "Successfully received data from student"
}
```

### GET /basic/info

Returns information about webhook concepts and learning objectives.

### GET /basic/status/{status_code}

Test endpoint for different HTTP status codes (200, 201, 400, 404, 500).

---

## External API Integration

### GET /external/dad-joke

Fetches a random dad joke from an external API.

**Response Example:**

```json
{
  "joke": "Why don't scientists trust atoms? Because they make up everything!",
  "source": "icanhazdadjoke.com",
  "fetched_at": "2024-01-15T10:30:00.123456",
  "webhook_message": "Successfully fetched dad joke via webhook!"
}
```

### GET /external/quote

Fetches an inspirational quote from an external API.

**Response Example:**

```json
{
  "quote": "The only way to do great work is to love what you do.",
  "author": "Steve Jobs",
  "source": "quotable.io",
  "fetched_at": "2024-01-15T10:30:00.123456",
  "webhook_message": "Inspirational quote delivered via webhook!"
}
```

### GET /external/multiple-apis

Demonstrates concurrent calls to multiple external APIs.

### POST /external/webhook-chain

Example of webhook chaining based on incoming data.

**Request Body:**

```json
{
  "trigger": "joke",
  "source": "test-system",
  "priority": "normal"
}
```

---

## Network Operations (Netmiko)

### POST /netmiko/command

Execute commands on network devices using Netmiko (simulated).

**Request Body:**

```json
{
  "device": {
    "host": "192.168.1.1",
    "username": "admin",
    "password": "password",
    "device_type": "cisco_ios"
  },
  "commands": [
    "show version",
    "show ip interface brief"
  ],
  "enable_mode": true
}
```

**Response Example:**

```json
{
  "device_ip": "192.168.1.1",
  "commands_executed": [
    "show version",
    "show ip interface brief"
  ],
  "results": [
    {
      "command": "show version",
      "output": "Cisco IOS Software...",
      "success": true
    }
  ],
  "execution_time_ms": 1250.5,
  "success": true,
  "timestamp": "2024-01-15T10:30:00.123456",
  "webhook_message": "Successfully executed 2 commands via webhook"
}
```

### GET /netmiko/device-status/{device_ip}

Check the status of a network device.

**Response Example:**

```json
{
  "device_ip": "192.168.1.1",
  "status": "online",
  "uptime": "45 days, 2 hours, 30 minutes",
  "version": "Cisco IOS 15.1(4)M4",
  "interfaces_up": 2,
  "last_checked": "2024-01-15T10:30:00.123456"
}
```

### POST /netmiko/bulk-command

Execute commands on multiple devices concurrently.

### POST /netmiko/config-backup

Backup device configuration.

### GET /netmiko/network-topology

Discover network topology using CDP/LLDP.

---

## RESTCONF Operations

### GET /restconf/interfaces/{device_ip}

Get interface information via RESTCONF.

**Query Parameters:**

- `username`: Device username (default: admin)
- `password`: Device password (default: admin)

**Response Example:**

```json
{
  "device_ip": "192.168.1.1",
  "path": "/restconf/data/ietf-interfaces:interfaces",
  "method": "GET",
  "status_code": 200,
  "response_data": {
    "ietf-interfaces:interfaces": {
      "interface": [
        {
          "name": "GigabitEthernet1",
          "description": "LAN Interface",
          "type": "iana-if-type:ethernetCsmacd",
          "enabled": true,
          "oper-status": "up"
        }
      ]
    }
  },
  "timestamp": "2024-01-15T10:30:00.123456",
  "success": true
}
```

### POST /restconf/configure

Configure network devices via RESTCONF.

**Request Body:**

```json
{
  "device": {
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
    "port": 443,
    "use_https": true
  },
  "path": "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1",
  "method": "PUT",
  "data": {
    "ietf-interfaces:interface": {
      "name": "GigabitEthernet1",
      "description": "Updated via RESTCONF webhook",
      "enabled": true
    }
  }
}
```

### GET /restconf/running-config/{device_ip}

Retrieve running configuration via RESTCONF.

### GET /restconf/operational-data/{device_ip}

Get operational data via RESTCONF.

**Query Parameters:**

- `data_type`: Type of data (interfaces, routing, system)

---

## NETCONF Operations

### GET /netconf/config/{device_ip}

Get device configuration via NETCONF.

**Query Parameters:**

- `datastore`: Configuration datastore (running, candidate, startup)
- `username`: Device username
- `password`: Device password

**Response Example:**

```json
{
  "device_ip": "192.168.1.1",
  "operation": "get-config",
  "datastore": "running",
  "success": true,
  "response_xml": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>...",
  "timestamp": "2024-01-15T10:30:00.123456",
  "execution_time_ms": 1500.0
}
```

### POST /netconf/edit-config

Edit device configuration via NETCONF.

**Request Body:**

```json
{
  "device": {
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
    "port": 830
  },
  "operation": "edit-config",
  "datastore": "running",
  "config_xml": "<interface><name>GigabitEthernet1</name><description>Updated via NETCONF</description></interface>"
}
```

### GET /netconf/capabilities/{device_ip}

Get NETCONF capabilities from a device.

### POST /netconf/validate

Validate NETCONF configuration before applying.

### POST /netconf/lock-unlock

Lock or unlock NETCONF datastores.

**Query Parameters:**

- `target`: Target datastore (running, candidate, startup)
- `operation`: Operation type (lock, unlock)

---

## Application Management

### GET /

Welcome page with HTML interface showing available endpoints.

### GET /health

Application health check endpoint.

**Response Example:**

```json
{
  "status": "healthy",
  "message": "Module 6 Webhook Application is running",
  "version": "1.0.0"
}
```

### GET /docs

Interactive API documentation (Swagger UI).

### GET /redoc

Alternative API documentation (ReDoc).

---

## Error Responses

All endpoints may return error responses with appropriate HTTP status codes:

### 400 Bad Request

```json
{
  "detail": "Invalid request format or missing required fields"
}
```

### 401 Unauthorized

```json
{
  "detail": "Authentication credentials invalid"
}
```

### 404 Not Found

```json
{
  "detail": "Endpoint not found"
}
```

### 500 Internal Server Error

```json
{
  "detail": "Internal server error occurred"
}
```

### 502 Bad Gateway

```json
{
  "detail": "External API unavailable"
}
```

### 503 Service Unavailable

```json
{
  "detail": "Service temporarily unavailable"
}
```

---

## Rate Limiting

In production environments, consider implementing rate limiting to prevent abuse:

- Basic endpoints: 100 requests per minute per IP
- Network operations: 10 requests per minute per IP
- External API calls: 5 requests per minute per IP

---

## Response Times

Typical response times for different endpoint categories:

- **Basic webhooks**: < 100ms
- **External API calls**: 1-5 seconds
- **Network operations**: 2-10 seconds (depending on device response)
- **Configuration changes**: 5-15 seconds

---

## Testing

### Using cURL

```bash
# Test basic webhook
curl -X GET http://localhost:8000/basic/message

# Test with JSON data
curl -X POST http://localhost:8000/basic/echo \
     -H "Content-Type: application/json" \
     -d '{"data": {"test": true}, "sender": "api-test"}'
```

### Using Python

```python
import requests

# Test GET endpoint
response = requests.get("http://localhost:8000/basic/message")
print(response.json())

# Test POST endpoint
data = {"data": {"test": True}, "sender": "python-test"}
response = requests.post("http://localhost:8000/basic/echo", json=data)
print(response.json())
```

---

## Notes for Students

1. **Start Simple**: Begin with basic endpoints before moving to network operations
2. **Use Simulation**: All network operations are simulated for learning purposes
3. **Check Logs**: Monitor application logs for debugging information
4. **Test Thoroughly**: Use the provided test scripts to validate your implementation
5. **Explore Documentation**: Use `/docs` endpoint for interactive testing

For additional help and examples, refer to the webhook implementation guide and sample test scripts provided in the repository.