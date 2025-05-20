from typing import TypedDict, Literal, Dict, List, Any
from pydantic import BaseModel, Field
import json
import subprocess
import pandas as pd
import os

from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode

# Define the financial data retrieval tool
class FinancialDataInput(TypedDict):
    """Tool to retrieve financial data for a specific symbol"""
    symbol: str

def get_financial_data(symbol: str) -> Dict[str, Any]:
    """Fetches financial market data analysis from Qandle AI API.
    
    Args:
        symbol: The trading symbol (e.g., 'AAPL')
    
    Returns:
        Dictionary containing the symbol and analysis data
    """
    try:
        # API endpoint and key
        api_endpoint = os.getenv("QANDLE_API")
        api_key = os.getenv("QANDLEAI_API_KEY")
        # Build the curl command
        curl_command = [
            "curl", 
            "-H", f"x-api-key: {api_key}",
            f"{api_endpoint}/observe?symbol={symbol}"
        ]
        # Execute the curl command
        result = subprocess.run(curl_command, capture_output=True, text=True)
        
        # Parse the JSON response
        response = json.loads(result.stdout)
        
        return {
            "symbol": symbol,
            "analysis": response.get("message", "No analysis available"),
        }
    except Exception as e:
        return {
            "symbol": symbol,
            "error": str(e),
            "analysis": "Failed to retrieve data"
        }

# Initialize the model using Ollama
model = ChatOllama(model="llama3.2", base_url="http://localhost:11434")

# System message to guide the agent
SYSTEM_PROMPT = """You are a dark humour specialist that makes jokes about the user's question.
"""

# Bind tools to the model
tools = [get_financial_data]
llm_with_tools = model.bind_tools(tools)

# Define the assistant node
def assistant(state: MessagesState):
    """Node that processes user input and either responds or calls tools"""
    return {"messages": [llm_with_tools.invoke([SystemMessage(content=SYSTEM_PROMPT)] + state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    tools_condition,
)
builder.add_edge("tools", "assistant")

# Compile graph
graph = builder.compile() 