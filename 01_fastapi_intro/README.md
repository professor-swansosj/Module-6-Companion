# 01: 🏁 FastAPI & Webhooks Introduction

## 🎯 Mission

Discover what webhooks are and why they're game-changers for network automation. You'll explore the FastAPI framework and understand how "reverse APIs" can make networks respond to events automatically!

## 🎖 Goals

By the end of this module, you'll be able to:

- [ ] **Explain** what webhooks are and how they differ from traditional APIs
- [ ] **Understand** FastAPI's role in creating webhook servers  
- [ ] **Identify** real-world use cases for event-driven automation
- [ ] **Set up** your development environment properly
- [ ] **Navigate** FastAPI's automatic documentation

## 📖 What Are Webhooks?

Think of webhooks as the **"phone calls"** of the internet, while regular APIs are like **"going to the store"**.

### Traditional API (You call them):

```bash
You → "Hey, do you have any new data?" → API
You ← "Nope, same as before" ← API
You → "How about now?" → API  
You ← "Still nothing..." ← API
```

### Webhooks (They call you):

```bash
Event happens → "Hey! Something changed!" → Your webhook server
Your server ← New data automatically ← External system
```

**Key Insight:** Webhooks push data to you when events occur, eliminating constant polling!

## 🌐 Real-World Examples

**Network Automation Scenarios:**

- 🚨 **Device goes offline** → Webhook triggered → Auto-create support ticket
- 📊 **High CPU usage detected** → Webhook triggered → Rebalance traffic automatically  
- 🔧 **Configuration change needed** → Webhook triggered → Deploy update across fleet
- ⚡ **Interface flaps** → Webhook triggered → Run diagnostics and notify team

## 🚀 Why FastAPI?

FastAPI makes building webhooks **fast** and **fun**:

### Speed & Performance

- Built on modern async Python
- Automatic data validation
- High performance out of the box

### Developer Experience  

- **Interactive docs** at `/docs` - test endpoints in your browser!
- **Type hints** - Python tells you when something's wrong
- **Minimal code** - Focus on logic, not boilerplate

### Example: Traditional vs FastAPI

**Traditional Flask approach:**

```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Manual validation needed
    if not data or 'message' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    return jsonify({'received': data['message']})
```

**FastAPI approach:**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WebhookData(BaseModel):
    message: str

@app.post("/webhook")
def webhook(data: WebhookData):
    return {"received": data.message}
    # Automatic validation & docs generation!
```

## 💡 Key Terms

| Term | Definition | Example |
|------|------------|---------|
| **Webhook** | HTTP callback that delivers data when events occur | Device sends alert to your server |
| **Endpoint** | A specific URL path that handles requests | `/network-alert` or `/device-status` |
| **FastAPI** | Modern Python web framework for building APIs | The tool we'll use to create webhooks |
| **Event-driven** | Actions triggered by specific events vs. scheduled polling | React to problems vs. constantly checking |
| **Payload** | The data sent in a webhook request | JSON with device info, alerts, etc. |

## 🔧 Environment Setup

Let's get your webhook development environment ready!

### Step 1: Verify Your Setup

```bash
# Check Python version (need 3.8+)
python --version

# Check if pip is working
pip --version
```

### Step 2: Explore FastAPI Installation

Look at your `requirements.txt` in the root directory:

```bash
fastapi==0.104.1      # The main framework
uvicorn[standard]==0.24.0  # ASGI server to run your app
pydantic==2.5.0       # Data validation (built into FastAPI)
```

### Step 3: Test Your Installation

```bash
# Make sure you're in your virtual environment!
# Then test FastAPI import:
python -c "import fastapi; print('FastAPI ready!')"
```

## 🎪 Try It: Explore FastAPI Documentation

Since we haven't built our server yet, let's explore what we're about to create:

1. **Visit the FastAPI homepage**: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

2. **Check out the interactive demo**: Look for the "Interactive API docs" section

3. **Imagine your use cases**: Think of 3 network scenarios where webhooks would be helpful

## ✅ Check Yourself

Before moving to the next module, make sure you can answer:

1. **What's the main difference between webhooks and regular API calls?**
2. **Name two benefits of using FastAPI over other frameworks**  
3. **What happens at the `/docs` endpoint of a FastAPI application?**
4. **Give an example of when a network device might send a webhook**
5. **What Python version is required for FastAPI?**

## 🚀 Ready for More?

Great! You understand the foundation. Now let's build your first FastAPI server in the next module!

**Next up:** `02_first_server/` - Time to see your webhook server come to life! 🎉

---

### 💡 Pro Tips

- **Bookmark** the [FastAPI docs](https://fastapi.tiangolo.com/) - you'll reference them often
- **Think event-driven** - What network events would you want to respond to automatically?
- **Start simple** - We'll build complexity gradually across the modules

### 🔗 Quick References

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Models](https://docs.pydantic.dev/latest/)
- [HTTP Status Codes](https://httpstatuses.com/)