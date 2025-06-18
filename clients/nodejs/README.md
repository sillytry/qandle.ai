# Qandle AI Node.js SDK

A Node.js client for interacting with the Qandle AI API.

## Installation

Install the package from npm:

```bash
npm install qandle-ai
```

## Configuration

The client can be configured using environment variables:

- `QANDLE_API_KEY`: Your Qandle AI API key (required)
- `QANDLE_API_URL`: The base URL for the Qandle AI API (optional, defaults to `https://api.qandle.ai`)

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
  const summary = await client.get('AAPL');
  console.log(summary);
}

getStockSummary();
```

## API Reference

### QandleClient

#### `constructor(options)`

Initialize the Qandle AI client.

**Parameters:**
- `options` (Object, optional): Configuration options
  - `apiKey` (string, optional): The API key for Qandle AI. If not provided, will attempt to get from `QANDLE_API_KEY` environment variable.
  - `baseUrl` (string, optional): The base URL for the Qandle AI API. If not provided, will use the default `https://api.qandle.ai` or `QANDLE_API_URL` environment variable.

#### `get(symbol)`

Retrieve the current action summary for a stock using the Qandle AI API.

**Parameters:**
- `symbol` (string): The stock symbol for which to obtain the current action summary.

**Returns:**
- `Promise<string>`: The stock summary message or error message.

## Error Handling

The client handles various types of errors and returns descriptive error messages:

- Missing API key: Throws `Error` during initialization
- Network errors: Returns error message with details
- HTTP errors: Returns error message with status code
- Other unexpected errors: Returns generic error message 