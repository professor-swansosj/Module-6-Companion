# Module 6 Companion - Reverse APIs and Event Driven Automation

**Course**: Software Defined Networking (Network Automation)  
**Module**: 6 - Reverse APIs and Event Driven Automation  
**Level**: Senior Level (Second Python Course)  
**Prerequisites**: Linux+, Introduction to Python, Cisco 1,2,3

## Table of Contents

1. [Introduction to Webhooks](#introduction-to-webhooks)
2. [Introduction to FastAPI](#introduction-to-fastapi)
3. [Develop a Simple Webhook to Return a Message](#develop-a-simple-webhook-to-return-a-message)
4. [Test via cURL](#test-via-curl)
5. [Develop Another Path that Calls Dad Jokes API](#develop-another-path-that-calls-dad-jokes-api)
6. [Test via cURL](#test-via-curl-1)
7. [Develop Another Path that Runs a Command via Netmiko](#develop-another-path-that-runs-a-command-via-netmiko)
8. [Test via cURL](#test-via-curl-2)
9. [Develop Another Path that Performs a RESTCONF Request](#develop-another-path-that-performs-a-restconf-request)
10. [Test via cURL](#test-via-curl-3)
11. [Develop Another Path that Performs a NETCONF Request](#develop-another-path-that-performs-a-netconf-request)
12. [Test via cURL](#test-via-curl-4)

## Overview

This module introduces students to **Reverse APIs** (Webhooks) and **Event Driven Automation** using FastAPI. Students will learn to create webhook endpoints that can receive HTTP requests and trigger automated network operations.

### Key Learning Objectives

- Understand the concept and implementation of webhooks/reverse APIs
- Build RESTful APIs using FastAPI framework
- Integrate external APIs (Dad Jokes API example)
- Implement network automation using Netmiko
- Perform RESTCONF and NETCONF operations via webhooks
- Test API endpoints using cURL commands

## Prerequisites Setup

Before starting this module, ensure you have:

1. **Python 3.8+** installed
2. **Git** for version control
3. **cURL** or **Postman** for API testing
4. **Network device access** (physical or simulated)

## Quick Start

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd Module-6-Companion
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI application**:

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the interactive API documentation**:
   - Open your browser to: `http://localhost:8000/docs`
   - Alternative ReDoc documentation: `http://localhost:8000/redoc`

## Project Structure

```
Module-6-Companion/
├── README.md                 # This file
├── LICENSE                   # License information
├── requirements.txt          # Python dependencies
├── main.py                   # Main FastAPI application
├── config/                   # Configuration files
│   ├── devices.yaml         # Network device configurations
│   └── settings.py          # Application settings
├── webhooks/                 # Webhook implementation modules
│   ├── __init__.py
│   ├── basic.py            # Simple webhook endpoints
│   ├── external_api.py     # External API integrations
│   ├── netmiko_ops.py      # Netmiko network operations
│   ├── restconf_ops.py     # RESTCONF operations
│   └── netconf_ops.py      # NETCONF operations
├── data/                    # Sample data files
│   ├── sample_config.json  # JSON configuration example
│   ├── network_inventory.yaml # YAML network inventory
│   ├── device_template.xml # XML device template
│   └── network_data.csv    # CSV network data
├── tests/                   # Test scripts and examples
│   ├── curl_examples.sh    # cURL test commands
│   └── test_webhooks.py    # Python test cases
└── docs/                    # Documentation
    ├── webhook_guide.md    # Webhook implementation guide
    └── api_reference.md    # API endpoint reference
```

## Introduction to Webhooks

Webhooks, also known as "Reverse APIs," are HTTP callbacks that allow applications to provide real-time information to other applications. Instead of continuously polling an API for changes, webhooks push data to your application when events occur.

### Key Concepts

- **Event-driven**: Triggered by specific events
- **Real-time**: Immediate data delivery
- **Efficient**: Reduces unnecessary API calls
- **Scalable**: Can handle multiple simultaneous events

## Introduction to FastAPI

FastAPI is a modern, high-performance web framework for building APIs with Python. It's particularly well-suited for creating webhooks due to its:

- **Fast performance**: Built on Starlette and Pydantic
- **Type hints**: Automatic data validation and serialization
- **Interactive documentation**: Automatic API docs generation
- **Standards-based**: OpenAPI and JSON Schema compliance

## Module Activities

Follow along with the instructional video and use this repository to practice each concept. The activities are designed to build progressively from simple webhooks to complex network automation scenarios.

### Activity Flow

1. Start with basic message return webhooks
2. Integrate external APIs for data enrichment
3. Add network device operations using Netmiko
4. Implement RESTCONF operations for modern network management
5. Add NETCONF support for legacy device management

## Testing Your Implementation

Each webhook endpoint can be tested using cURL commands. Examples are provided in the `tests/curl_examples.sh` file. Always test your endpoints thoroughly before moving to the next activity.

## Troubleshooting

Common issues and solutions:

1. **Port already in use**: Change the port in the uvicorn command
2. **Module not found**: Ensure virtual environment is activated
3. **Network device unreachable**: Check device configurations in `config/devices.yaml`
4. **API authentication errors**: Verify credentials and API keys

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Netmiko Documentation](https://github.com/ktbyers/netmiko)
- [RESTCONF RFC](https://tools.ietf.org/html/rfc8040)
- [NETCONF RFC](https://tools.ietf.org/html/rfc6241)

## Support

If you encounter issues while working through this module, please:

1. Check the troubleshooting section above
2. Review the code comments and documentation
3. Consult with your instructor during class or office hours

---

**Happy Learning!** 🚀
