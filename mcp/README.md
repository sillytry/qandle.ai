# Qandle AI MCP Server

A Model Context Protocol (MCP) server that provides stock market analysis and summaries using the Qandle AI service.

## Installation

1. Install dependencies:
```bash
npm install
```

2. Build the TypeScript code:
```bash
npm run build
```

3. Set up your environment variables:
```bash
cp env.example .env
```
Then edit the `.env` file and replace `your_api_key_here` with your actual Qandle AI API key.

## Integration with Claude Desktop

To use this server with Claude Desktop, add the following to your `claude_desktop_config.json`:

**macOS/Linux:**
```json
{
  "mcpServers": {
    "qandle-ai": {
      "command": "node",
      "args": ["/ABSOLUTE/PATH/TO/qandle.ai/mcp/build/index.js"]
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "qandle-ai": {
      "command": "node",
      "args": ["C:\\ABSOLUTE\\PATH\\TO\\qandle.ai\\mcp\\dist\\index.js"]
    }
  }
}
```

## Available Tools

#### `get_stock_summary`
Get comprehensive stock summary and analysis for one or multiple symbol(s).

**Parameters:**
- `symbol` (string): A comma-separated list of of stock symbol(s) to get summary for (e.g., AAPL, GOOGL, TSLA)

**Example:**
```json
{
  "symbol": "AAPL, MSFT, NVDA"
}
```