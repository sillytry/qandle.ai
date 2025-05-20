import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from financial_agent import graph

# Load environment variables
load_dotenv()

# Override Ollama URL if present in environment
if os.getenv("OLLAMA_BASE_URL"):
    from financial_agent import model
    model.base_url = os.getenv("OLLAMA_BASE_URL")

def test_financial_agent():
    """Simple test function to run the financial agent."""
    # Create test config
    config = {"configurable": {"user_id": "test_user"}}
    
    # Example test messages
    test_messages = [
        "Can you explain what P/E ratio means in simple terms?",
        "What is the current market outlook for AAPL stock?",
        "What factors should I consider when investing in bonds versus stocks?"
    ]
    
    # Run the first test message
    print("Running financial agent test...\n")
    input_message = HumanMessage(content=test_messages[0])
    
    print(f"User Message: {input_message.content}\n")
    print("Agent Response:")
    
    # Execute the graph with the test message
    result = graph.invoke({"messages": [input_message]}, config)
    
    # Print the response messages
    for message in result["messages"]:
        if message.type == "ai":
            print(f"\nAI: {message.content}")
        elif message.type == "tool":
            print(f"\nTool ({message.tool_call_id}): {message.content}")

if __name__ == "__main__":
    test_financial_agent() 