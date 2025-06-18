---
icon: "material/run-fast"
---

# Quickstart

Learn how to use Qandle AI and effortlessly integrate financial intelligence into your AI application.

---

## :material-rocket-launch: Getting Started Guide

Qandle AI is designed for builders! Follow these steps to get up and running:

### :material-numeric-1-circle: Create Account & Generate API Key

!!! info "Step 1: Account Setup"
    Get your API credentials to start using Qandle AI

**Tasks to complete:**

:material-numeric-1: Visit [qandle.ai](https://www.qandle.ai) to create your account

:material-numeric-2: Sign in using Google, or your email

:material-numeric-3: Copy your new API key using the copy button

!!! warning "Important"
    Keep your API key secure and never share it publicly. Store it safely as you'll need it for authentication.

---

### :material-numeric-2-circle: Choose Your Integration Method

!!! info "Step 2: Installation"
    Choose your preferred integration method based on your use case

=== "Python"

    **For Python developers building AI applications**
    
    ```bash
    pip install qandle-ai
    ```

=== "Node.js"

    **For JavaScript/Node.js developers**
    
    ```bash
    npm install qandle-ai
    ```

=== "MCP Server"

    **For AI assistants (Claude Desktop, Cursor IDE, etc.)**
    
    No installation required! Use Qandle AI directly in your favorite AI applications.
    
    !!! tip "Quick Setup"
        **[→ Follow the MCP Server setup guide](../integration/mcp-server.md)**

---

### :material-numeric-3-circle: Initialize the Client

!!! info "Step 3: Setup"
    Import and configure the Qandle AI client with your API key

#### :material-cog: Configuration 

!!! tip "Environment Variables"
    Set up environment variable for secure configuration:
    
    - `QANDLE_API_KEY`: Your Qandle AI API key (required)

=== "Python"
    ```python
    from qandle_ai import QandleClient
    
    # Initialize the client (automatically uses environment variables)
    client = QandleClient()
    ```
    

=== "Node.js"

    ```javascript
    const QandleClient = require('qandle-ai');
    
    // Initialize the client (automatically uses environment variables)
    const client = new QandleClient();
    
    ```

=== "MCP Server"

    ```json
    {
      "mcpServers": {
        "Qandle AI": {
          "command": "npx",
          "args": [
            "mcp-remote",
            "https://mcp.qandle.ai/mcp",
            "--header",
            "Authorization: Bearer <YOUR_API_KEY>"
          ]
        }
      }
    }
    ```
    
    !!! info "Platform-specific setup"
        **[→ See detailed MCP configuration guide](../integration/mcp-server.md)**

---

### :material-numeric-4-circle: Make Your First Request

!!! example "Step 4: Test Drive"
    Try your first API call to get financial data

=== "Python"

    ```python
    # Get stock summary
    summary = client.get("AAPL")
    print(summary)
    ```
=== "Node.js"

    ```javascript
    // Get stock summary
    client.get('AAPL').then(summary => {
        console.log(summary);
    });
    ```

=== "MCP Server"

    Simply ask your AI assistant:
    
    ```
    Can you get me a financial summary for Apple (AAPL)?
    ```
    
    The AI will automatically use Qandle AI's MCP server to retrieve the data!

---

## :material-arrow-right: What's Next?

!!! success "Congratulations! 🎉"
    You've successfully set up Qandle AI. Here's what you can explore next:
    
    - **[Integrate Qandle AI with LangChain and Langgraph](../tutorials/langchain.md)** - Build intelligent financial agents with pre-computed data
    - **[Deploy in Claude, Cursor, etc](../integration/mcp-server.md)** - Zero-code integration with AI assistants and tools
    - **[API Reference](../api/get-symbol.md)** - Explore available endpoints