# 02: 🖥️ Your First FastAPI Webhook Server

## 🎯 Mission

Build and run your very first FastAPI webhook server! You'll create a simple endpoint, start the server, and see the magic of automatic API documentation in action.

## 🎖 Goals

By the end of this module, you'll have:

- [ ] **Created** a minimal FastAPI application
- [ ] **Started** your webhook server using Uvicorn
- [ ] **Accessed** the automatic interactive documentation  
- [ ] **Tested** your endpoint using the built-in interface
- [ ] **Understanding** of how FastAPI apps are structured

## 📖 FastAPI Application Basics

Every FastAPI app follows this pattern:

1. **Import FastAPI** - Get the framework
2. **Create app instance** - Your server object  
3. **Define endpoints** - Functions that handle requests
4. **Run the server** - Make it accessible to the world

### Minimal Example Structure

```python
from fastapi import FastAPI

app = FastAPI()  # This is your server!

@app.get("/")   # This handles GET requests to "/"
def root():
    return {"message": "Hello World"}
```

That's it! Three lines of actual code for a working web server! 🤯

## 🚀 Key Concepts

### The App Instance

```python
app = FastAPI()
```
This creates your server. Think of it as your "webhook command center" where all requests will be handled.

### Decorators Define Routes

```python
@app.get("/endpoint-name")
def my_function():
    return {"data": "response"}
```

The **decorator** (`@app.get`) tells FastAPI:

- **What HTTP method** to use (GET, POST, PUT, DELETE)
- **What URL path** triggers this function ("/endpoint-name")

### Return Values Become JSON

FastAPI automatically converts Python dictionaries and lists to JSON responses. Super convenient!

## 🛠️ Build Your First Server

Let's create a webhook server that can receive simple notifications!

### Step 1: Understanding the Starter Code

Look at the `server.py` file in this directory. You'll see:

- Basic FastAPI setup with TODO comments
- A root endpoint that needs completion
- A webhook endpoint structure waiting for your code

### Step 2: Complete the TODOs

The starter file has guided TODO items that will walk you through:

1. Creating the FastAPI instance
2. Adding a basic greeting endpoint
3. Creating your first webhook endpoint
4. Adding some personality to your responses

### Step 3: Start Your Server

Once you've completed the TODOs:

```bash
# Make sure you're in the 02_first_server/ directory
cd 02_first_server/

# Run your server (this starts it on localhost:8000)
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

**Command breakdown:**

- `server:app` - Import `app` from `server.py`
- `--reload` - Restart automatically when you change code
- `--host 0.0.0.0` - Accept connections from any IP
- `--port 8000` - Use port 8000

## 🎪 The Magic: Interactive Documentation

Once your server is running, FastAPI automatically creates documentation for you!

### Visit These URLs:

1. **Swagger UI (Interactive)**: `http://localhost:8000/docs`
   - Click on endpoints to expand them
   - Try out requests directly in the browser
   - See response formats and status codes

2. **ReDoc (Alternative)**: `http://localhost:8000/redoc`  
   - Different style, same information
   - Great for sharing with team members

3. **Your actual endpoints**: `http://localhost:8000/` and `http://localhost:8000/webhook`

## 🧪 Testing Your Server

### Method 1: Browser (for GET requests)

Just visit `http://localhost:8000/` in your browser!

### Method 2: Interactive Docs  

1. Go to `http://localhost:8000/docs`
2. Click on your endpoint
3. Click "Try it out" 
4. Click "Execute"
5. See the response!

### Method 3: cURL (command line)

```bash
# Test your root endpoint
curl http://localhost:8000/

# Test your webhook endpoint  
curl -X POST http://localhost:8000/webhook \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello webhook!"}'
```

## 🎨 Make It Your Own

Want to add some personality? Try these extensions:

### Add Fun Responses

```python
import random

responses = [
    "Webhook received loud and clear! 📡",
    "Got your message! Processing... 🤖", 
    "Webhook magic happening! ✨"
]

return {"response": random.choice(responses)}
```

### Add Timestamp

```python
from datetime import datetime

return {
    "message": "Webhook received!",
    "timestamp": datetime.now().isoformat()
}
```

## ✅ Check Yourself

Before moving on, make sure you can:

1. **Start your server** without errors
2. **Access the docs** at `/docs` and see your endpoints
3. **Send a request** through the interactive interface  
4. **Get a JSON response** back from your webhook
5. **Understand** what each part of your FastAPI code does

## 🚨 Troubleshooting

**Port already in use?**

```bash
# Try a different port
uvicorn server:app --reload --port 8001
```

**Module not found?**

```bash  
# Make sure you're in the right directory and virtual environment
pwd  # Should show the 02_first_server/ directory
python -c "import fastapi"  # Should not error
```

**Can't access from browser?**

- Check the terminal for error messages
- Make sure you see "Uvicorn running on http://0.0.0.0:8000" 
- Try `http://localhost:8000` and `http://127.0.0.1:8000`

## 🏆 Success Criteria

You've mastered this module when:

- [x] Your server starts and shows "Uvicorn running on..."
- [x] You can visit `/docs` and see interactive documentation
- [x] Your endpoints return JSON responses
- [x] You understand the basic FastAPI application structure

## 🚀 Ready for More Paths?

Excellent! You've built your first webhook server. Now let's make it more interesting with multiple endpoints and fun responses!

**Next up:** `03_paths_responses/` - Time to create multiple webhook endpoints! 🛤️

---

### 💡 Pro Tips

- **Keep the server running** while you code - use `--reload` to see changes instantly
- **Always check the terminal** for error messages - they're usually helpful
- **Experiment** with different return values - FastAPI handles most Python data types
- **Use the interactive docs** - they're your best friend for testing

### 🔗 Quick References

- [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Uvicorn Documentation](https://www.uvicorn.org/)  
- [HTTP Status Codes](https://httpstatuses.com/)