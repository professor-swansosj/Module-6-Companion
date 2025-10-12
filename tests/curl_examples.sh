#!/bin/bash

# Module 6 - cURL Testing Examples
# Reverse APIs and Event Driven Automation
# 
# This script contains cURL examples for testing all webhook endpoints
# Students can use these examples to test their FastAPI application

echo "======================================="
echo "Module 6 - Webhook Testing with cURL"
echo "======================================="
echo ""

# Set the base URL (change if running on different host/port)
BASE_URL="http://localhost:8000"

echo "Testing Basic Webhooks..."
echo "--------------------------"

echo "1. Testing simple message webhook:"
curl -X GET "$BASE_URL/basic/message" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "2. Testing echo webhook:"
curl -X POST "$BASE_URL/basic/echo" \
     -H "Content-Type: application/json" \
     -d '{
       "data": {
         "message": "Hello from cURL!",
         "number": 42,
         "active": true
       },
       "sender": "test-student"
     }' | jq '.'
echo ""

echo "3. Testing webhook info:"
curl -X GET "$BASE_URL/basic/info" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "4. Testing status codes:"
curl -X GET "$BASE_URL/basic/status/200" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "External API Integration..."
echo "---------------------------"

echo "5. Testing dad joke webhook:"
curl -X GET "$BASE_URL/external/dad-joke" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "6. Testing inspirational quote webhook:"
curl -X GET "$BASE_URL/external/quote" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "7. Testing multiple APIs webhook:"
curl -X GET "$BASE_URL/external/multiple-apis" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "8. Testing webhook chain:"
curl -X POST "$BASE_URL/external/webhook-chain" \
     -H "Content-Type: application/json" \
     -d '{
       "trigger": "joke",
       "source": "cURL-test",
       "priority": "normal"
     }' | jq '.'
echo ""

echo "Network Operations (Netmiko)..."
echo "-------------------------------"

echo "9. Testing Netmiko command execution:"
curl -X POST "$BASE_URL/netmiko/command" \
     -H "Content-Type: application/json" \
     -d '{
       "device": {
         "host": "192.168.1.1",
         "username": "admin",
         "password": "password",
         "device_type": "cisco_ios"
       },
       "commands": [
         "show version",
         "show ip interface brief",
         "show running-config | include hostname"
       ],
       "enable_mode": true
     }' | jq '.'
echo ""

echo "10. Testing device status check:"
curl -X GET "$BASE_URL/netmiko/device-status/192.168.1.1" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "11. Testing configuration backup:"
curl -X POST "$BASE_URL/netmiko/config-backup" \
     -H "Content-Type: application/json" \
     -d '{
       "host": "192.168.1.1",
       "username": "admin",
       "password": "password",
       "device_type": "cisco_ios"
     }' | jq '.'
echo ""

echo "12. Testing network topology discovery:"
curl -X GET "$BASE_URL/netmiko/network-topology" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "RESTCONF Operations..."
echo "----------------------"

echo "13. Testing RESTCONF interface retrieval:"
curl -X GET "$BASE_URL/restconf/interfaces/192.168.1.1?username=admin&password=admin" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "14. Testing RESTCONF configuration:"
curl -X POST "$BASE_URL/restconf/configure" \
     -H "Content-Type: application/json" \
     -d '{
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
           "description": "Updated via RESTCONF webhook from cURL",
           "enabled": true
         }
       }
     }' | jq '.'
echo ""

echo "15. Testing RESTCONF running config retrieval:"
curl -X GET "$BASE_URL/restconf/running-config/192.168.1.1" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "16. Testing RESTCONF operational data:"
curl -X GET "$BASE_URL/restconf/operational-data/192.168.1.1?data_type=interfaces" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "NETCONF Operations..."
echo "---------------------"

echo "17. Testing NETCONF configuration retrieval:"
curl -X GET "$BASE_URL/netconf/config/192.168.1.1?datastore=running&username=admin&password=admin" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "18. Testing NETCONF configuration edit:"
curl -X POST "$BASE_URL/netconf/edit-config" \
     -H "Content-Type: application/json" \
     -d '{
       "device": {
         "host": "192.168.1.1",
         "username": "admin",
         "password": "admin",
         "port": 830
       },
       "operation": "edit-config",
       "datastore": "running",
       "config_xml": "<interfaces xmlns=\"urn:ietf:params:xml:ns:yang:ietf-interfaces\"><interface><name>GigabitEthernet1</name><description>Updated via NETCONF webhook from cURL</description></interface></interfaces>"
     }' | jq '.'
echo ""

echo "19. Testing NETCONF capabilities:"
curl -X GET "$BASE_URL/netconf/capabilities/192.168.1.1" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "20. Testing NETCONF validation:"
curl -X POST "$BASE_URL/netconf/validate" \
     -H "Content-Type: application/json" \
     -d '{
       "device": {
         "host": "192.168.1.1",
         "username": "admin",
         "password": "admin"
       },
       "operation": "validate",
       "datastore": "candidate",
       "config_xml": "<interface><name>GigabitEthernet1</name><description>Test validation</description></interface>"
     }' | jq '.'
echo ""

echo "Health Check..."
echo "---------------"

echo "21. Testing application health:"
curl -X GET "$BASE_URL/health" \
     -H "Accept: application/json" | jq '.'
echo ""

echo "======================================="
echo "All tests completed!"
echo "Check the responses above for any errors."
echo "======================================="