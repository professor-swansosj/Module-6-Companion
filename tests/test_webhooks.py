"""
Test Cases for Module 6 Webhooks
Module 6 - Reverse APIs and Event Driven Automation

This file contains pytest test cases for testing webhook endpoints.
Students can use these tests to validate their webhook implementations.

To run tests:
pytest test_webhooks.py -v
"""

import pytest
import httpx
import asyncio
from datetime import datetime

# Test configuration
BASE_URL = "http://localhost:8000"
TIMEOUT = 30.0

class TestBasicWebhooks:
    """Test basic webhook functionality"""
    
    @pytest.mark.asyncio
    async def test_simple_message_webhook(self):
        """Test the simple message webhook endpoint"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/basic/message", timeout=TIMEOUT)
            
        assert response.status_code == 200
        data = response.json()
        
        assert "message" in data
        assert "timestamp" in data  
        assert "status" in data
        assert data["status"] == "success"
        
        # Validate timestamp format
        timestamp = datetime.fromisoformat(data["timestamp"].replace('Z', '+00:00'))
        assert isinstance(timestamp, datetime)
    
    @pytest.mark.asyncio
    async def test_echo_webhook(self):
        """Test the echo webhook endpoint"""
        test_data = {
            "data": {
                "test_key": "test_value",
                "number": 42,
                "active": True
            },
            "sender": "pytest"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/basic/echo",
                json=test_data,
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "received_data" in data
        assert "sender" in data
        assert "processed_at" in data
        assert "echo_message" in data
        
        assert data["received_data"] == test_data["data"]
        assert data["sender"] == test_data["sender"]
    
    @pytest.mark.asyncio
    async def test_webhook_info(self):
        """Test the webhook info endpoint"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/basic/info", timeout=TIMEOUT)
        
        assert response.status_code == 200
        data = response.json()
        
        required_keys = ["webhook_concept", "event_driven", "benefits", "use_cases"]
        for key in required_keys:
            assert key in data
    
    @pytest.mark.asyncio
    async def test_status_codes(self):
        """Test different HTTP status codes"""
        test_cases = [
            (200, 200),
            (201, 201), 
            (400, 400),
            (404, 404),
            (500, 500)
        ]
        
        async with httpx.AsyncClient() as client:
            for input_code, expected_code in test_cases:
                response = await client.get(
                    f"{BASE_URL}/basic/status/{input_code}",
                    timeout=TIMEOUT
                )
                assert response.status_code == expected_code

class TestExternalAPIWebhooks:
    """Test external API integration webhooks"""
    
    @pytest.mark.asyncio
    async def test_dad_joke_webhook(self):
        """Test the dad joke webhook (may fail if external API is down)"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/external/dad-joke", timeout=TIMEOUT)
        
        # Should succeed or fail gracefully
        assert response.status_code in [200, 502, 503]
        
        if response.status_code == 200:
            data = response.json()
            assert "joke" in data
            assert "source" in data
            assert "fetched_at" in data
    
    @pytest.mark.asyncio 
    async def test_quote_webhook(self):
        """Test the inspirational quote webhook"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/external/quote", timeout=TIMEOUT)
        
        # Should succeed or fail gracefully
        assert response.status_code in [200, 502, 503]
        
        if response.status_code == 200:
            data = response.json()
            assert "quote" in data
            assert "author" in data
            assert "source" in data
    
    @pytest.mark.asyncio
    async def test_multiple_apis_webhook(self):
        """Test the multiple APIs webhook"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/external/multiple-apis", timeout=TIMEOUT)
        
        # Should succeed or fail gracefully
        assert response.status_code in [200, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert "content" in data
            assert "metadata" in data
            assert "webhook_message" in data
    
    @pytest.mark.asyncio
    async def test_webhook_chain(self):
        """Test the webhook chain example"""
        test_data = {
            "trigger": "joke",
            "source": "pytest",
            "priority": "normal"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/external/webhook-chain",
                json=test_data,
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "webhook_chain" in data
        assert "next_actions" in data
        assert data["webhook_chain"]["received_data"] == test_data

class TestNetworkWebhooks:
    """Test network operations webhooks (simulated)"""
    
    @pytest.mark.asyncio
    async def test_netmiko_command_webhook(self):
        """Test Netmiko command execution webhook"""
        test_request = {
            "device": {
                "host": "192.168.1.1",
                "username": "admin",
                "password": "password",
                "device_type": "cisco_ios"
            },
            "commands": ["show version", "show ip interface brief"],
            "enable_mode": True
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/netmiko/command",
                json=test_request,
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "device_ip" in data
        assert "commands_executed" in data
        assert "results" in data
        assert "success" in data
        assert data["success"] is True
        assert len(data["results"]) == len(test_request["commands"])
    
    @pytest.mark.asyncio
    async def test_device_status_webhook(self):
        """Test device status check webhook"""
        device_ip = "192.168.1.1"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/netmiko/device-status/{device_ip}",
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "device_ip" in data
        assert "status" in data
        assert "uptime" in data
        assert "version" in data
        assert data["device_ip"] == device_ip
    
    @pytest.mark.asyncio
    async def test_config_backup_webhook(self):
        """Test configuration backup webhook"""
        test_device = {
            "host": "192.168.1.1",
            "username": "admin",
            "password": "password",
            "device_type": "cisco_ios"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/netmiko/config-backup",
                json=test_device,
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "backup_info" in data
        assert "preview" in data
        assert "webhook_message" in data

class TestRESTCONFWebhooks:
    """Test RESTCONF operations webhooks (simulated)"""
    
    @pytest.mark.asyncio
    async def test_restconf_interfaces(self):
        """Test RESTCONF interfaces retrieval"""
        device_ip = "192.168.1.1"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/restconf/interfaces/{device_ip}",
                params={"username": "admin", "password": "admin"},
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "device_ip" in data
        assert "path" in data
        assert "method" in data
        assert "response_data" in data
        assert "success" in data
        assert data["success"] is True
    
    @pytest.mark.asyncio
    async def test_restconf_configure(self):
        """Test RESTCONF configuration webhook"""
        test_request = {
            "device": {
                "host": "192.168.1.1",
                "username": "admin",
                "password": "admin"
            },
            "path": "/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1",
            "method": "PUT",
            "data": {
                "ietf-interfaces:interface": {
                    "name": "GigabitEthernet1",
                    "description": "Test from pytest",
                    "enabled": True
                }
            }
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/restconf/configure",
                json=test_request,
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "restconf_operation" in data
        assert "configuration" in data
        assert "webhook_message" in data

class TestNETCONFWebhooks:
    """Test NETCONF operations webhooks (simulated)"""
    
    @pytest.mark.asyncio
    async def test_netconf_config_retrieval(self):
        """Test NETCONF configuration retrieval"""
        device_ip = "192.168.1.1"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/netconf/config/{device_ip}",
                params={"datastore": "running", "username": "admin", "password": "admin"},
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "device_ip" in data
        assert "operation" in data
        assert "datastore" in data
        assert "response_xml" in data
        assert "success" in data
        assert data["success"] is True
    
    @pytest.mark.asyncio
    async def test_netconf_capabilities(self):
        """Test NETCONF capabilities retrieval"""
        device_ip = "192.168.1.1"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/netconf/capabilities/{device_ip}",
                timeout=TIMEOUT
            )
        
        assert response.status_code == 200
        data = response.json()
        
        assert "capabilities" in data
        assert "webhook_message" in data
        
        caps_data = data["capabilities"]
        assert "device_ip" in caps_data
        assert "capabilities" in caps_data
        assert "yang_models" in caps_data

class TestApplicationHealth:
    """Test application health and status"""
    
    @pytest.mark.asyncio
    async def test_root_endpoint(self):
        """Test the root endpoint returns HTML"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/", timeout=TIMEOUT)
        
        assert response.status_code == 200
        assert "text/html" in response.headers.get("content-type", "")
        assert "Module 6" in response.text
    
    @pytest.mark.asyncio
    async def test_health_check(self):
        """Test the health check endpoint"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BASE_URL}/health", timeout=TIMEOUT)
        
        assert response.status_code == 200
        data = response.json()
        
        assert "status" in data
        assert "message" in data
        assert "version" in data
        assert data["status"] == "healthy"

# Test configuration for pytest
@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

if __name__ == "__main__":
    # Run tests if this file is executed directly
    import subprocess
    subprocess.run(["pytest", __file__, "-v"])