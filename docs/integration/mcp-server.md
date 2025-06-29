---
icon: "material/robot-love-outline"
---

# Using Qandle AI's MCP Server

Model Context Protocol (MCP) is a standardized way for AI applications like Claude, Cursor and ChatGPT to interact with web apps like Qandle AI.

By connecting to Qandle AI's MCP server, you can automatically integrate factual and contextual financial data with your AI application or AI agents and benefit from ready-made prompts to automate daily routine tasks to manage your investments.

## Quick Setup

!!! tip "No-code integration coming soon!"
    We are actively working on making Qandle AI's MCP server even easier to integrate with your favorite AI applications. With the integration in place, it will be possible to integrate with Qandle AI's MCP server following the AI application authentication flow directly. Join our [Discord](https://discord.gg/hcMZuuaVtq) to be the first to know when our OAuth 2.1 authentication mechanism following MCP's latest standard will be available!

### Claude Desktop

1. Create `~/Library/Application\ Support/Claude/claude_desktop_config.json`
2. Add this configuration:

```json
{
  "mcpServers": {
    "Qandle AI": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.qandle.ai/mcp",
        "--header",
        "Authorization: Bearer <API KEY>"
      ]
    }
  }
}
```

### Cursor IDE

For tools that you want to use across all projects, create a `~/.cursor/mcp.json` file in your home directory. This makes MCP servers available in all your Cursor workspaces.

#### Global Setup (All Projects)

1. Create `~/.cursor/mcp.json` in your home directory
2. Use the same JSON configuration as above

#### Project-Specific Setup

1. Create `.cursor/mcp.json` in your project root
2. Use the same JSON configuration as above
3. The server will only be available in that project

### Other AI Applications

Most AI applications that support MCP will have a similar setup process. Look for MCP or "Tools" settings and configure the integration with Qandle AI's MCP server following a process similar to Claude and Cursor IDE.

---

## Available Capabilities

The Qandle AI MCP server provides the following tools and prompts to AI applications:

#### Tools    

- **get-asset-summary**: Retrieve a factual and contextual summary of the latest action for a ccomma-separated list of symbols.


#### Prompts

- **Do-I-own-winners**: A portfolio benchmark comparison prompt that retrieves comprehensive data for both the stocks and their matching industry ETF benchmarks, displays the information side-by-side in a detailed table for comparison whilst providing factual data presentation without analysis, allowing users to evaluate their portfolio holdings against industry benchmarks.

