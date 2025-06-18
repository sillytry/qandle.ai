#!/usr/bin/env node

import { config } from "dotenv";
import { fileURLToPath } from "url";
import { dirname, join } from "path";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { QandleClient } from "qandle-ai";
import { z } from "zod";

// Get the directory of the current module
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Load environment variables from .env file in the project root
const envPath = join(__dirname, '..', '.env');
config({ path: envPath });

// Initialize Qandle client
let qandleClient: QandleClient;
try {
  qandleClient = new QandleClient();
} catch (error) {
  console.error("Failed to initialize QandleClient:", error);
  throw new Error("QandleClient initialization failed");
}

// Create server instance
const server = new McpServer({
  name: "qandle-mcp-server",
  version: "1.0.0",
});

// Register stock summary tool
server.tool(
  "get_stock_summary",
  "Get comprehensive stock summary and analysis for one or multiple symbols using Qandle AI",
  {
    symbol: z.array(z.string().min(1).max(5)).describe("Stock symbol to get summary for (e.g., AAPL, GOOGL, TSLA)"),
  },
  async ({ symbol }) => {
    try {
      const results: { symbol: string; data?: string; error?: string }[] = [];
      
      // Process each symbol in the array
      for (const sym of symbol) {
        try {
          // Validate symbol format (basic validation)
          const upperSymbol = sym.toUpperCase().trim();
          if (!/^[A-Z]{1,5}$/.test(upperSymbol)) {
            results.push({
              symbol: upperSymbol,
              error: "Invalid symbol format. Please provide a valid stock symbol (e.g., AAPL, GOOGL)"
            });
            continue;
          }

          const result = await qandleClient.get(upperSymbol);
          results.push({
            symbol: upperSymbol,
            data: result
          });
        } catch (error) {
          const errorMessage = error instanceof Error ? error.message : "Unknown error occurred";
          console.error(`Error retrieving stock summary for ${sym}:`, errorMessage);
          
          results.push({
            symbol: sym.toUpperCase().trim(),
            error: "Not found or data unavailable"
          });
        }
      }

      // Consolidate results into a single response
      let consolidatedText = "";
      const foundSymbols: string[] = [];
      const notFoundSymbols: string[] = [];

      for (const result of results) {
        if (result.data) {
          foundSymbols.push(result.symbol);
          consolidatedText += `Stock Summary for ${result.symbol}:\n\n${result.data}\n\n${"=".repeat(50)}\n\n`;
        } else {
          notFoundSymbols.push(result.symbol);
        }
      }

      // Add summary of not found symbols if any
      if (notFoundSymbols.length > 0) {
        consolidatedText += `Symbols not found or unavailable: ${notFoundSymbols.join(", ")}\n\n`;
      }

      // Add final summary
      if (foundSymbols.length > 0) {
        consolidatedText += `Successfully retrieved data for: ${foundSymbols.join(", ")}`;
      }

      if (foundSymbols.length === 0) {
        consolidatedText = `No data could be retrieved for the requested symbols: ${notFoundSymbols.join(", ")}`;
      }

      return {
        content: [
          {
            type: "text",
            text: consolidatedText.trim(),
          },
        ],
      };
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : "Unknown error occurred";
      console.error("Error in get_stock_summary tool:", errorMessage);
      
      return {
        content: [
          {
            type: "text",
            text: "Error retrieving stock summaries. Please try again.",
          },
        ],
        isError: true,
      };
    }
  }
);

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Qandle MCP server running on stdio");
}

main().catch((error) => {
  console.error("Fatal error in main():", error);
  process.exit(1);
}); 