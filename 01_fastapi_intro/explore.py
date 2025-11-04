"""
Section 01: FastAPI & Webhooks Exploration

TODO: This module is about understanding concepts, not coding yet!
Your mission: Get familiar with FastAPI documentation and webhook concepts.

Hint: No server code needed here - you're building foundational knowledge.
"""

def explore_fastapi_concepts():
    """
    TODO: Visit https://fastapi.tiangolo.com/ and explore the documentation
    
    Questions to answer while exploring:
    1. What makes FastAPI "fast"?
    2. What is automatic API documentation?
    3. How does FastAPI handle data validation?
    
    Write your findings as comments below!
    """
    
    # TODO: Write what you learned about FastAPI's speed
    # Your answer: 
    
    # TODO: Write what you learned about automatic docs  
    # Your answer:
    
    # TODO: Write what you learned about data validation
    # Your answer:
    
    pass


def webhook_use_case_brainstorm():
    """
    TODO: Think of 3 network automation scenarios where webhooks would be useful
    
    Template: "When [EVENT] happens, webhook triggers [ACTION]"
    """
    
    # TODO: Scenario 1 - Device monitoring
    scenario_1 = "When _____________ happens, webhook triggers _____________"
    
    # TODO: Scenario 2 - Security event  
    scenario_2 = "When _____________ happens, webhook triggers _____________"
    
    # TODO: Scenario 3 - Configuration management
    scenario_3 = "When _____________ happens, webhook triggers _____________"
    
    # Print your scenarios when you're ready!
    print("My Webhook Scenarios:")
    print(f"1. {scenario_1}")
    print(f"2. {scenario_2}")  
    print(f"3. {scenario_3}")


def check_environment():
    """
    TODO: Run this function to verify your setup is ready for the next modules
    
    This should run without errors if your environment is properly set up.
    """
    try:
        import fastapi
        import uvicorn
        import pydantic
        import requests
        
        print("✅ All required packages are installed!")
        print(f"FastAPI version: {fastapi.__version__}")
        print("🚀 Ready to build webhooks!")
        
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("💡 Make sure you've activated your virtual environment and run:")
        print("   pip install -r requirements.txt")


if __name__ == "__main__":
    print("🏁 Module 01: FastAPI & Webhooks Exploration")
    print("=" * 50)
    
    # TODO: Uncomment each function as you complete the tasks
    
    # explore_fastapi_concepts()
    # webhook_use_case_brainstorm() 
    # check_environment()
    
    print("\n🎯 Next: Head to 02_first_server/ when you're ready to code!")
