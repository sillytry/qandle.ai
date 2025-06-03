# Technical Analyst with LangChain

This example demonstrates how to build an AI-powered technical analyst using LangGraph, LangChain, and the Qandle AI API. The application retrieves stock action summaries and provides intelligent analysis through a conversational interface.

## Overview

The technical analyst leverages:
- **LangGraph**: Creates a stateful graph for managing conversation flow and tool invocations
- **LangChain**: Provides the foundation for building language model applications
- **Qandle AI API**: Retrieves real-time stock action summaries with sentiment analysis
- **Ollama**: Powers the language model for processing and generating responses
- **Tool Integration**: Seamlessly combines API calls with LLM reasoning

## Architecture

The application uses a graph-based architecture where the AI assistant can invoke tools when needed:

![LangGraph Architecture](assets/architecture-diagram.png)

*Figure: LangGraph workflow showing the conversation flow from START through the Assistant, Tools Condition decision point, and Tools Node execution.*

### Workflow Description

1. **START**: Conversation begins
2. **Assistant**: LLM processes the user message and system prompt
3. **Tools Condition**: Determines if a tool call is needed
4. **Tools Node**: Executes the `get_stock_summary` function if required
5. **Loop**: Returns to Assistant for response generation
6. **END**: Conversation concludes when no tool calls are needed

## Features

- 🔍 **Stock Analysis**: Retrieve detailed action summaries for any stock symbol
- 📊 **Sentiment Analysis**: Get sentiment indicators for each stock recommendation
- 💬 **Conversational Interface**: Natural language interaction with the AI analyst
- 🔄 **Stateful Management**: Maintains conversation context using LangGraph
- 🛠️ **Tool Integration**: Seamless API integration with function calling

## Prerequisites

- Python 3.8 or higher
- Qandle AI API access (get your API key from [Qandle AI](https://qandle.ai))
- Ollama installed and running locally (or accessible endpoint)

## Setup

1. **Navigate to the example directory**:
   ```bash
   cd examples/technical-analyst-with-langchain/studio
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file or export the following variables:
   ```bash
   export QANDLE_API_KEY="your-qandle-api-key"
   export QANDLE_API_URL="https://api.qandle.ai"  # Optional, defaults to this URL
   export OLLAMA_BASE_URL="http://localhost:11434"  # Optional, adjust for your Ollama setup
   ```

4. **Ensure Ollama is running**:
   ```bash
   # Install and start Ollama if not already done
   ollama serve
   
   # Pull the required model
   ollama pull llama3.2
   ```

## Usage

### Running the Application

```bash
python app.py
```

### Example Interactions

The application creates a graph that you can invoke with messages. Here are some example use cases:

```python
# Example 1: Get stock analysis
messages = [{"role": "user", "content": "What's the current action summary for AAPL?"}]
result = graph.invoke({"messages": messages})

# Example 2: Compare multiple stocks
messages = [{"role": "user", "content": "Can you analyze TSLA and NVDA for me?"}]
result = graph.invoke({"messages": messages})

# Example 3: Ask for investment advice
messages = [{"role": "user", "content": "Should I buy or sell MSFT based on current data?"}]
result = graph.invoke({"messages": messages})
```

### API Response Format

The `get_stock_summary` function returns formatted data including:
- **Name**: Company or analysis name
- **Description**: Detailed analysis description
- **Sentiment**: Current sentiment indicator (Positive/Negative/Neutral)

## Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `QANDLE_API_KEY` | Your Qandle AI API key | - | ✅ |
| `QANDLE_API_URL` | Qandle AI API base URL | `https://api.qandle.ai` | ❌ |
| `OLLAMA_BASE_URL` | Ollama service URL | `http://host.docker.internal:11434` | ❌ |

### Customization

You can customize the system message in `app.py`:

```python
sys_msg = SystemMessage(content="You are a technical analyst. You can get the current action summary for a stock from Qandle AI API.")
```

## File Structure

```
technical-analyst-with-langchain/
├── assets/
│   └── architecture-diagram.png  # LangGraph workflow diagram
├── studio/
│   ├── app.py              # Main application code
│   ├── requirements.txt    # Python dependencies
│   ├── langgraph.json     # LangGraph configuration
│   └── .gitignore         # Git ignore rules
├── agent.ipynb            # Jupyter notebook version
└── README.md              # This file
```

## Dependencies

- **langgraph**: Graph-based workflow orchestration
- **langchain-core**: Core LangChain functionality
- **langchain-community**: Community tools and integrations
- **langchain-ollama**: Ollama integration for LangChain

## Error Handling

The application includes comprehensive error handling for:
- Missing API keys
- Network connectivity issues
- Invalid stock symbols
- API response parsing errors
- Ollama connection problems

## Troubleshooting

### Common Issues

1. **API Key Not Set**:
   ```
   Error: QANDLE_API_KEY environment variable is not set
   ```
   Solution: Set your `QANDLE_API_KEY` environment variable

2. **Ollama Connection Error**:
   ```
   Connection refused to Ollama
   ```
   Solution: Ensure Ollama is running and accessible at the configured URL

3. **Model Not Found**:
   ```
   Model llama3.2 not found
   ```
   Solution: Pull the model with `ollama pull llama3.2`

## Contributing

To contribute to this example:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This example is part of the Qandle AI Academy and is licensed under the MIT License.

## Support

For questions about this example:
- Email: [support@qandle.ai](mailto:support@qandle.ai)
- Documentation: [Qandle AI Docs](https://docs.qandle.ai)

---

**Happy analyzing! 📈**