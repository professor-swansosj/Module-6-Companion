"""
Application Settings
Module 6 - Reverse APIs and Event Driven Automation

This module contains application configuration settings.
Students can modify these settings to customize their webhook application.
"""

import os
from typing import List, Dict, Any
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Application settings using Pydantic BaseSettings for environment variable support"""
    
    # FastAPI Application Settings
    app_title: str = "Module 6 - Webhook & Event Driven Automation"
    app_description: str = "Companion repository for SDN Module 6 - Reverse APIs and Event Driven Automation"
    app_version: str = "1.0.0"
    
    # Server Settings
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    log_level: str = "info"
    
    # Development Settings
    debug: bool = True
    simulation_mode: bool = True  # Use simulated responses for learning
    
    # CORS Settings (for development)
    cors_enabled: bool = True
    allowed_origins: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000", 
        "http://localhost:8080",
        "http://127.0.0.1:8080"
    ]
    
    # External API Settings
    external_api_timeout: int = 10
    dad_jokes_api: str = "https://icanhazdadjoke.com/"
    quotes_api: str = "https://api.quotable.io/random"
    facts_api: str = "https://uselessfacts.jsph.pl/random.json"
    
    # Network Operation Settings
    network_timeout: int = 30
    max_concurrent_connections: int = 10
    retry_attempts: int = 3
    retry_delay: int = 1
    
    # Netmiko Settings
    netmiko_global_delay_factor: int = 1
    netmiko_banner_timeout: int = 15
    netmiko_auth_timeout: int = 10
    
    # RESTCONF Settings
    restconf_verify_ssl: bool = False
    restconf_timeout: int = 30
    
    # NETCONF Settings
    netconf_timeout: int = 30
    netconf_hostkey_verify: bool = False
    
    # Default Device Credentials (for simulation)
    default_username: str = "admin"
    default_password: str = "password"
    default_enable_secret: str = "enable123"
    
    # Security Settings (for production reference)
    api_key_required: bool = False
    rate_limiting: bool = False
    request_size_limit: str = "10MB"
    
    class Config:
        """Pydantic configuration"""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

# Global settings instance
settings = Settings()

# Device configurations for different scenarios
DEVICE_CONFIGS = {
    "routers": {
        "router1": {
            "hostname": "Router1",
            "management_ip": "192.168.1.1",
            "device_type": "cisco_ios",
            "credentials": {
                "username": settings.default_username,
                "password": settings.default_password,
                "enable_secret": settings.default_enable_secret
            },
            "protocols": {
                "ssh": True,
                "netconf": True,
                "restconf": True
            }
        },
        "router2": {
            "hostname": "Router2", 
            "management_ip": "192.168.2.1",
            "device_type": "cisco_ios",
            "credentials": {
                "username": settings.default_username,
                "password": settings.default_password,
                "enable_secret": settings.default_enable_secret
            },
            "protocols": {
                "ssh": True,
                "netconf": True,
                "restconf": True
            }
        }
    },
    "switches": {
        "switch1": {
            "hostname": "Switch1",
            "management_ip": "192.168.1.2",
            "device_type": "cisco_ios",
            "credentials": {
                "username": settings.default_username,
                "password": settings.default_password,
                "enable_secret": settings.default_enable_secret
            },
            "protocols": {
                "ssh": True,
                "netconf": False,  # May not be supported
                "restconf": False  # May not be supported
            }
        }
    }
}

# Webhook endpoint configurations
WEBHOOK_ENDPOINTS = {
    "basic": [
        {
            "name": "Simple Message",
            "path": "/basic/message",
            "method": "GET",
            "description": "Returns a simple message"
        },
        {
            "name": "Echo Data",
            "path": "/basic/echo", 
            "method": "POST",
            "description": "Echoes received data back"
        }
    ],
    "external": [
        {
            "name": "Dad Joke",
            "path": "/external/dad-joke",
            "method": "GET",
            "description": "Fetches a random dad joke"
        },
        {
            "name": "Inspirational Quote",
            "path": "/external/quote",
            "method": "GET", 
            "description": "Fetches an inspirational quote"
        }
    ],
    "network": [
        {
            "name": "Netmiko Command",
            "path": "/netmiko/command",
            "method": "POST",
            "description": "Executes commands via Netmiko"
        },
        {
            "name": "RESTCONF Interfaces",
            "path": "/restconf/interfaces/{device_ip}",
            "method": "GET",
            "description": "Gets interfaces via RESTCONF"
        },
        {
            "name": "NETCONF Config",
            "path": "/netconf/config/{device_ip}",
            "method": "GET", 
            "description": "Gets configuration via NETCONF"
        }
    ]
}

# Logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "formatter": "detailed",
            "class": "logging.FileHandler",
            "filename": "webhook_app.log",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["default"],
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False,
        },
        "webhook_app": {
            "handlers": ["default", "file"],
            "level": "DEBUG" if settings.debug else "INFO",
            "propagate": False,
        },
    },
}

def get_device_config(device_type: str, device_name: str) -> Dict[str, Any]:
    """Get configuration for a specific device"""
    if device_type in DEVICE_CONFIGS and device_name in DEVICE_CONFIGS[device_type]:
        return DEVICE_CONFIGS[device_type][device_name]
    return None

def get_all_devices() -> Dict[str, Any]:
    """Get all device configurations"""
    return DEVICE_CONFIGS

def is_simulation_mode() -> bool:
    """Check if application is running in simulation mode"""
    return settings.simulation_mode