# Financial Assistant

A LangGraph application that provides financial information and data analysis using Ollama for LLM capabilities.

## Project Structure

- `financial_agent.py`: Main agent implementation
- `configuration.py`: Configuration utilities
- `langgraph.json`: LangGraph configuration file
- `requirements.txt`: Project dependencies
- `env_example`: Example environment file (rename to `.env` and add your configuration)

## Prerequisites

1. Install [Ollama](https://ollama.ai/) on your machine
2. Pull the llama3.2 model with: `ollama pull llama3.2`
3. Make sure Ollama is running before starting the application

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your configuration:

```bash
cp env_example .env
```

3. Edit the `.env` file if needed (default Ollama settings should work if running locally)

## Running with LangGraph Studio

1. Make sure you have Docker Desktop and LangGraph Studio installed.

2. Ensure Ollama is running on your machine.

3. Open LangGraph Studio and load the project.

4. The agent will be available as "financial_agent" in the Studio UI.

## Example Usage

You can interact with the agent with various financial questions:

- "Can you explain what P/E ratio means?"
- "What is the current market sentiment for AAPL stock?"
- "What factors should I consider when building a retirement portfolio?"
- "Can you provide information about the recent performance of TSLA?"

## Extending the Agent

You can extend this agent by:

1. Adding more financial analysis tools in `financial_agent.py`
2. Customizing the system prompt for different financial use cases
3. Implementing additional data sources and APIs
4. Trying different Ollama models (e.g., llama3, mistral, codellama) 