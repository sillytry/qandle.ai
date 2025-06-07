from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
import os

from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode

# Import the Qandle AI client
from qandle_ai import QandleClient

# Static variable for Ollama configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Initialize Qandle AI client
qandle_client = QandleClient()

def get_stock_summary(symbol: str) -> str:
    """Retrieve the current action summary for a stock using the Qandle AI API.

    Args:
        symbol (str): The stock symbol for which to obtain the current action summary.
    """
    return qandle_client.get(symbol)

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