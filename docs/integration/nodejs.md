---
icon: "material/nodejs"
---

# Node.js SDK

A Node.js client for interacting with the Qandle AI API. The SDK provides a simple and intuitive interface to access financial market data and analysis with full TypeScript support.

## Installation

Install the package from npm:

```bash
npm install qandle-ai
```

### Requirements

- Node.js (compatible with modern Node.js versions)

## Configuration

The client can be configured using environment variables for easy setup:

| Environment Variable | Description | Required |
|---------------------|-------------|----------|
| `QANDLE_API_KEY` | Your Qandle AI API key | ✅ Required |
| `QANDLE_API_URL` | The base URL for the Qandle AI API | ❌ Optional (defaults to `https://api.qandle.ai`) |

### Setting Environment Variables

=== "Linux/macOS"

    ```bash
    export QANDLE_API_KEY="your-api-key-here"
    export QANDLE_API_URL="https://api.qandle.ai"  # Optional
    ```

=== "Windows"

    ```cmd
    set QANDLE_API_KEY=your-api-key-here
    set QANDLE_API_URL=https://api.qandle.ai
    ```

=== "Node.js (.env file)"

    ```javascript
    // Using dotenv package
    require('dotenv').config();
    
    // Or with ES modules
    import 'dotenv/config';
    ```

## Usage

### Basic Usage

```javascript
import { QandleClient } from 'qandle-ai';

// Initialize the client (uses QANDLE_API_KEY environment variable)
const client = new QandleClient();

// Get stock summary
client.get('AAPL').then(summary => {
  console.log(summary);
});
```

### Custom Configuration

```javascript
import { QandleClient } from 'qandle-ai';

// Initialize with custom API key and base URL
const client = new QandleClient({
  apiKey: 'your-api-key-here',
  baseUrl: 'https://custom-api.qandle.ai'
});

// Get stock summary
client.get('TSLA').then(summary => {
  console.log(summary);
});
```

### Using with async/await

```javascript
import { QandleClient } from 'qandle-ai';

async function getStockSummary() {
  const client = new QandleClient();
  try {
    const summary = await client.get('AAPL');
    console.log(summary);
  } catch (error) {
    console.error('Error:', error);
  }
}

getStockSummary();
```

## API Reference

### QandleClient

The main class for interacting with the Qandle AI API.

#### Constructor

```typescript
constructor(options?: QandleClientOptions)
```

**Parameters:**

- `options` (Object, optional): Configuration options
  - `apiKey` (string, optional): The API key for Qandle AI. If not provided, will attempt to get from `QANDLE_API_KEY` environment variable.
  - `baseUrl` (string, optional): The base URL for the Qandle AI API. If not provided, will use the default `https://api.qandle.ai` or `QANDLE_API_URL` environment variable.

**Throws:**

- `Error`: If no API key is provided and `QANDLE_API_KEY` environment variable is not set.

#### Methods

### `get(symbol)`

Retrieve the current action summary for a stock using the Qandle AI API.

**Parameters:**

- `symbol` (string): The stock symbol for which to obtain the current action summary (e.g., "AAPL", "GOOGL", "TSLA").

**Returns:**

- `Promise<string>`: The stock summary message containing analysis and recommendations.

**Example:**

```javascript
const client = new QandleClient();
const result = await client.get("AAPL");
console.log(result);
```