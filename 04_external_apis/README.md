# 04: 🌐 External APIs & Data Integration

## 🎯 Mission

Connect your webhook server to the outside world! You'll learn how to make HTTP requests to external APIs, handle responses, and integrate external data into your webhooks. Plus, we'll have some fun with the Dad Jokes API! 

## 🎖 Goals

By the end of this module, you'll be able to:

- [ ] **Make HTTP requests** to external APIs from your FastAPI server
- [ ] **Handle API responses** and error conditions gracefully
- [ ] **Integrate external data** into your webhook responses  
- [ ] **Use the requests library** for API calls
- [ ] **Create composite endpoints** that combine multiple data sources
- [ ] **Understand async vs sync** API calls in FastAPI

## 📖 Why External APIs in Webhooks?

Real-world webhooks often need to:

- **Enrich data** - Get additional context from other services
- **Trigger actions** - Call other APIs when events occur  
- **Validate information** - Check external databases or services
- **Notify systems** - Send alerts to Slack, email, or monitoring tools

### Example Workflow

```bash
Device Alert → Your Webhook → Dad Jokes API → Enhanced Response
     ↓              ↓              ↓              ↓
  "CPU High"  →  Process Alert →  Get Joke   →  "Alert + Joke"
```

This makes alerts more bearable! 😄

## 🔗 Making HTTP Requests in Python

You have two main options for making HTTP requests:

### Option 1: requests library (Synchronous)

```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
```

### Option 2: httpx library (Async/Sync)

```python
import httpx

# Synchronous
response = httpx.get("https://api.example.com/data")
data = response.json()

# Asynchronous (advanced)
async with httpx.AsyncClient() as client:
    response = await client.get("https://api.example.com/data")
    data = response.json()
```

For this module, we'll use `requests` - it's simpler and perfect for learning!

## 😂 Meet the Dad Jokes API

The Dad Jokes API is perfect for learning because:

- **No authentication required** - Easy to get started
- **Simple JSON response** - Easy to parse
- **Reliable and fun** - Makes testing enjoyable

### API Details

- **URL**: `https://icanhazdadjoke.com/`
- **Method**: GET
- **Headers**: `Accept: application/json`
- **Response**: `{"id": "...", "joke": "...", "status": 200}`

### Example Request

```bash
curl -H "Accept: application/json" https://icanhazdadjoke.com/
```

### Example Response

```json
{
  "id": "R7UfaahVfFd",
  "joke": "My dog used to chase people on a bike a lot. It got so bad I had to take his bike away.",
  "status": 200
}
```

## 🛠️ Building API Integration Endpoints

Let's create webhooks that call external APIs!

### Basic Dad Joke Endpoint

```python
import requests

@app.get("/joke")
def get_dad_joke():
    try:
        response = requests.get(
            "https://icanhazdadjoke.com/", 
            headers={"Accept": "application/json"}
        )
        response.raise_for_status()  # Raises exception for bad status codes
        joke_data = response.json()
        
        return {
            "webhook_response": "Dad joke delivered!",
            "joke": joke_data["joke"],
            "joke_id": joke_data["id"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to get joke: {str(e)}"}
```

### Network Alert + Joke Combo

```python
@app.post("/network-alert")
def network_alert_with_joke(alert_data: dict):
    # Process the network alert
    alert_response = {
        "alert_processed": True,
        "severity": alert_data.get("severity", "unknown"),
        "device": alert_data.get("device", "unknown")
    }
    
    # Add a joke to lighten the mood
    try:
        joke_response = requests.get(
            "https://icanhazdadjoke.com/",
            headers={"Accept": "application/json"}
        )
        if joke_response.status_code == 200:
            joke = joke_response.json()["joke"]
            alert_response["mood_booster"] = joke
            alert_response["message"] = "Alert processed! Here's a joke to brighten your day."
    except:
        alert_response["mood_booster"] = "No joke available, but you're doing great!"
    
    return alert_response
```

## 🧰 Error Handling Best Practices

External APIs can fail! Always handle errors gracefully:

### Common Error Scenarios

- **Network timeout** - API server is slow
- **404 Not Found** - Endpoint doesn't exist  
- **500 Server Error** - API server is having problems
- **Connection Error** - No internet connection

### Robust Error Handling

```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def safe_api_call(url, headers=None, timeout=5):
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return {"success": True, "data": response.json()}
    
    except Timeout:
        return {"success": False, "error": "API request timed out"}
    
    except ConnectionError:
        return {"success": False, "error": "Could not connect to API"}
    
    except RequestException as e:
        return {"success": False, "error": f"API request failed: {str(e)}"}
```

## 🎪 Your Mission: Complete the External API Server

In the `external_api_server.py` file, you'll build endpoints that:

1. **Get a simple dad joke** - Basic API integration
2. **Get a joke with custom formatting** - Process API responses
3. **Network alert webhook with joke** - Combine webhook data with external API
4. **Multiple API integration** - Call several APIs in one endpoint
5. **Error handling showcase** - Demonstrate graceful failure handling

## 🧪 Testing Your API Integration

### Test with cURL

```bash
# Test the dad joke endpoint
curl http://localhost:8000/joke

# Test network alert with joke
curl -X POST http://localhost:8000/network-alert \
     -H "Content-Type: application/json" \
     -d '{"severity": "high", "device": "router-01", "message": "High CPU usage"}'
```

### Test Error Handling

You can simulate API failures by:

- Using a fake URL in your code temporarily
- Setting a very short timeout
- Testing with no internet connection

## 🎨 Creative Extensions

### Multi-API Mashup

Combine multiple APIs in one endpoint:

```python
@app.get("/network-mood")  
def network_mood():
    # Get a dad joke
    joke = get_dad_joke_data()
    
    # Get weather data (if you want to try another API)
    # weather = get_weather_data()
    
    # Combine into network mood report
    return {
        "network_status": "All systems operational",
        "team_mood_booster": joke,
        "message": "Network is stable, team morale is high!"
    }
```

### Webhook Chain

Create a webhook that calls another webhook:

```python
@app.post("/webhook-chain")
def webhook_chain(data: dict):
    # Process incoming webhook
    processed = {"received": data, "processed_at": datetime.now()}
    
    # Call your own joke endpoint
    joke_response = requests.get("http://localhost:8000/joke")
    
    # Combine responses  
    return {
        "original_webhook": processed,
        "bonus_content": joke_response.json()
    }
```

## ✅ Testing Checklist

Make sure your endpoints:

- [ ] **Successfully call external APIs** - Dad Jokes API works
- [ ] **Handle API responses properly** - Parse JSON correctly
- [ ] **Include error handling** - Graceful failure when APIs are down
- [ ] **Combine webhook data with API data** - Mix incoming data with external data
- [ ] **Return useful error messages** - Help users understand what went wrong

## 🚨 Troubleshooting

**API calls not working?**

- Check your internet connection
- Verify the API URL is correct
- Make sure you're including required headers
- Check if the API requires authentication

**Getting timeout errors?**

- Increase the timeout value in your requests
- Check if the external API is slow or down
- Consider adding retry logic for production use

**JSON parsing errors?**

- Print the raw response to see what you're getting
- Check if the API returns JSON (some return HTML on errors)
- Verify the API is working by testing with cURL first

## 🏆 Success Criteria

You've mastered this module when:

- [x] You can successfully call the Dad Jokes API
- [x] Your webhooks integrate external data seamlessly
- [x] Error handling prevents crashes when APIs fail
- [x] You understand how to combine multiple data sources
- [x] Your endpoints provide value beyond just echoing data

## 🚀 Ready for Network Automation?

Fantastic! You can now integrate external APIs into your webhooks. Time to connect with real network devices!

**Next up:** `05_network_operations/` - Let's use Netmiko to control network devices via webhooks! 🔌

---

### 💡 Pro Tips

- **Always set timeouts** - Don't let slow APIs hang your server
- **Cache API responses** when appropriate - Avoid unnecessary API calls
- **Log API calls** - Helps with debugging and monitoring
- **Consider rate limits** - Some APIs limit how often you can call them

### 🔗 Quick References

- [Requests Documentation](https://docs.python-requests.org/)
- [Dad Jokes API](https://icanhazdadjoke.com/api)
- [HTTP Status Codes](https://httpstatuses.com/)
- [JSON Handling in Python](https://docs.python.org/3/library/json.html)