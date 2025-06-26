# qandle.ai

**AI-Optimized Technical Indicators API** - Get pre-computed, AI-ready financial data in a single API call.

No complex calculations, no scattered data sources—just clean financial intelligence formatted specifically for AI applications and LLMs.

🌐 **[Qandle AI Website](https://www.qandle.ai)** | 📖 **[Full Documentation](https://docs.qandle.ai)** | 💬 **[Discord Community](https://discord.gg/hcMZuuaVtq)**

## Quick Setup

### 1. Get API Key
Visit [qandle.ai](https://www.qandle.ai) to create your account and copy your API key.

### 2. Install

**Python:**
```bash
pip install qandle-ai
```

**Node.js:**
```bash
npm install qandle-ai
```

**MCP Server (Claude Desktop, Cursor IDE):**
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

### 3. Use

**Python:**
```python
from qandle_ai import QandleClient
client = QandleClient()  # Uses QANDLE_API_KEY env var
summary = client.get("AAPL")
```

**Node.js:**
```javascript
const QandleClient = require('qandle-ai');
const client = new QandleClient();  // Uses QANDLE_API_KEY env var
client.get('AAPL').then(summary => console.log(summary));
```

**MCP Server:**
Ask your AI assistant: "Get me a financial summary for Apple (AAPL)"

## Documentation

Full documentation available at [docs.qandle.ai](https://docs.qandle.ai)

## Community

Join our [Discord](https://discord.gg/hcMZuuaVtq) for support and discussions!