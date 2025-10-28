# 03: 🛤️ Multiple Paths & Creative Responses

## 🎯 Mission

Expand your webhook server with multiple endpoints and add some creative flair! You'll learn how to handle different HTTP methods, create various response formats, and yes - even add some ASCII art to make your webhooks more fun!

## 🎖 Goals

By the end of this module, you'll be able to:

- [ ] **Create multiple endpoints** with different URL paths
- [ ] **Handle different HTTP methods** (GET, POST, PUT, DELETE)
- [ ] **Return various response formats** (JSON, text, HTML)
- [ ] **Add creative elements** like ASCII art and dynamic content
- [ ] **Understand path parameters** and query strings
- [ ] **Build webhook endpoints** that feel more professional

## 📖 Understanding FastAPI Routing

FastAPI uses **decorators** to map URLs to functions. Think of each endpoint as a different "door" to your server:

```python
@app.get("/")          # Front door - basic info
@app.post("/webhook")  # Service entrance - receives data  
@app.get("/status")    # Side door - health checks
@app.get("/fun")       # Secret door - surprise content! 
```

### HTTP Methods and Their Purposes

| Method | Purpose | Webhook Use Case |
|--------|---------|------------------|
| **GET** | Retrieve information | Status checks, documentation |
| **POST** | Send data to server | Receive webhook notifications |  
| **PUT** | Update/replace data | Update configuration |
| **DELETE** | Remove data | Clear cache, reset state |

## 🎨 Creative Response Types

FastAPI can return more than just JSON! Let's explore:

### JSON Responses (Default)

```python
@app.get("/json-example")
def json_response():
    return {"type": "json", "message": "This becomes JSON automatically"}
```

### Plain Text Responses  

```python
from fastapi import Response

@app.get("/text-example")
def text_response():
    return Response("This is plain text!", media_type="text/plain")
```

### HTML Responses

```python
from fastapi.responses import HTMLResponse

@app.get("/html-example", response_class=HTMLResponse)
def html_response():
    return "<h1>This is HTML!</h1><p>Great for simple web interfaces.</p>"
```

## 🎭 ASCII Art in Webhooks

ASCII art can make your webhook responses memorable and fun! Here are some ideas:

### Network-Themed ASCII

```python
def get_network_art():
    return """
     🌐 NETWORK WEBHOOK SERVER 🌐
    ================================
         
    [Router] ←→ [Switch] ←→ [Device]
         ↓         ↓         ↓
      [Webhook] [Webhook] [Webhook]
         ↓         ↓         ↓  
    =================================
         YOUR AUTOMATION HUB
    """
```

### Status Indicators

```python
def get_status_art(status):
    if status == "healthy":
        return """
        ✅ SYSTEM HEALTHY ✅
        ==================
        🔋 Power: Good
        📡 Network: Connected  
        💾 Memory: Available
        🖥️  CPU: Normal
        """
    else:
        return """
        ⚠️  SYSTEM ALERT ⚠️
        ================
        🔍 Check required!
        """
```

## 🛠️ Build Your Multi-Endpoint Server

Time to expand your webhook server with multiple paths and creative responses!

### Your Mission: Complete the Paths

In the `paths_server.py` file, you'll find TODO comments guiding you to create:

1. **Root endpoint** - Basic server information
2. **ASCII art endpoint** - Fun network-themed art
3. **Status endpoint** - Server health with visual indicators
4. **Echo endpoint** - Reflects back what you send it
5. **Random response endpoint** - Dynamic content each time

### Path Parameters Example

You can capture values from the URL path:

```python
@app.get("/network/{device_type}")
def get_device_info(device_type: str):
    return {"device": device_type, "status": "active"}
    
# Usage: /network/router returns {"device": "router", "status": "active"}
```

### Query Parameters Example

You can also use query strings for optional parameters:

```python
@app.get("/status")
def get_status(format: str = "json"):
    if format == "ascii":
        return Response(get_ascii_status(), media_type="text/plain")
    return {"status": "healthy"}
    
# Usage: /status?format=ascii returns ASCII art
```

## 🧪 Testing Your Endpoints

### Interactive Documentation

Visit `http://localhost:8000/docs` to see all your endpoints! The documentation updates automatically as you add new paths.

### cURL Examples

```bash
# Test different endpoints
curl http://localhost:8000/
curl http://localhost:8000/ascii  
curl http://localhost:8000/status
curl http://localhost:8000/status?format=ascii

# Test with data
curl -X POST http://localhost:8000/echo \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello webhook!"}'
```

### Browser Testing

GET endpoints work great in browsers:

- `http://localhost:8000/ascii` 
- `http://localhost:8000/status?format=ascii`

## 🎪 Creative Extensions

Want to add more personality? Try these ideas:

### Random Network Facts

```python
import random

network_facts = [
    "The first network message was 'LO' (trying to send 'LOGIN')",
    "Ethernet cables can be up to 100 meters long",
    "The '@' symbol was used in email for the first time in 1971"
]

@app.get("/fact")
def random_fact():
    return {"fact": random.choice(network_facts)}
```

### Dynamic ASCII Art  

```python
from datetime import datetime

@app.get("/time-art")
def time_art():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        return Response("🌅 Good Morning! Server is awake! 🌅", media_type="text/plain")
    elif 12 <= hour < 18:
        return Response("☀️ Good Afternoon! Server is working! ☀️", media_type="text/plain")
    else:
        return Response("🌙 Good Evening! Server is monitoring! 🌙", media_type="text/plain")
```

## ✅ Testing Checklist

Make sure your server has:

- [ ] **Multiple endpoints** with different paths
- [ ] **Different HTTP methods** (GET and POST minimum)
- [ ] **ASCII art endpoint** that returns text/plain
- [ ] **JSON endpoints** with structured data
- [ ] **Query parameter support** (like `?format=ascii`)
- [ ] **Creative responses** that show personality

## 🚨 Troubleshooting

**ASCII art looks weird?**

- Use triple quotes `"""` for multi-line strings
- Set `media_type="text/plain"` for text responses
- Check browser font - monospace fonts work best

**Endpoints not showing in docs?**

- Make sure you're using the right decorators (`@app.get`, `@app.post`)
- Check for syntax errors in your functions
- Restart the server if changes aren't showing

**Query parameters not working?**

```python
# ❌ Wrong
def status(format):  

# ✅ Right  
def status(format: str = "json"):
```

## 🏆 Success Criteria

You've mastered this module when:

- [x] You have at least 4-5 different endpoints
- [x] At least one endpoint returns ASCII art
- [x] You can use query parameters to change response format
- [x] Your endpoints have personality and creative flair
- [x] All endpoints are visible in the interactive docs

## 🚀 Ready for External APIs?

Excellent! Your webhook server now has multiple personalities and creative responses. Time to connect with the outside world!

**Next up:** `04_external_apis/` - Let's call the Dad Jokes API and bring external data into your webhooks! 🌐

---

### 💡 Pro Tips

- **Use descriptive endpoint names** - `/network-status` is clearer than `/status`
- **Add docstrings** to your functions - they appear in the automatic docs
- **Test in different browsers** - ASCII art may render differently  
- **Be creative but professional** - balance fun with functionality

### 🔗 Quick References

- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [ASCII Art Generator](https://www.asciiart.eu/)
- [HTTP Response Types](https://fastapi.tiangolo.com/advanced/response-types/)