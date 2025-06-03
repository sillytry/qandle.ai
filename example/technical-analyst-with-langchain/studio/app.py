from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
import requests
import json
import os

from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode

# Static variables for Qandle AI API configuration
QANDLE_API_URL = os.getenv("QANDLE_API_URL", "https://api.qandle.ai")
QANDLE_API_KEY = os.getenv("QANDLE_API_KEY")

# Static variable for Ollama configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

def get_stock_summary(symbol: str) -> str:
    """Retrieve the current action summary for a stock using the Qandle AI API.

    Args:
        symbol (str): The stock symbol for which to obtain the current action summary.
    """
    if not QANDLE_API_KEY:
        return f"Error: QANDLE_API_KEY environment variable is not set"
    
    try:
        # Make API call to Qandle AI
        url = f"{QANDLE_API_URL}/asset?symbol={symbol}"
        headers = {
            "x-api-key": QANDLE_API_KEY
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract name, description, and sentiment from each message
        result_lines = []
        if "message" in data and isinstance(data["message"], list):
            for message in data["message"]:
                name = message.get("name", "")
                description = message.get("description", "")
                sentiment = message.get("sentiment", "")
                
                # Create formatted line for each message
                line = f"Name: {name}\nDescription: {description}\nSentiment: {sentiment}"
                result_lines.append(line)
        
        # Join all lines with double newlines for separation
        return "\n\n".join(result_lines) if result_lines else f"No data available for {symbol}"
        
    except requests.RequestException as e:
        return f"Error fetching data for {symbol}: {str(e)}"
    except json.JSONDecodeError as e:
        return f"Error parsing response for {symbol}: {str(e)}"
    except Exception as e:
        return f"Unexpected error for {symbol}: {str(e)}"

tools = [get_stock_summary]

# Define LLM with bound tools
llm = ChatOllama(model="llama3.2", base_url=OLLAMA_BASE_URL)
llm_with_tools = llm.bind_tools(tools)

# System message
sys_msg = SystemMessage(content="You are a technical analyst. You can get the current action summary for a stock from Qandle AI API.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")

# Compile graph
graph = builder.compile()

#graph.get_graph().draw_mermaid_png(output_file_path="technical_analyst_graph.png")