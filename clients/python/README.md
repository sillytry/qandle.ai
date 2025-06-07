# Qandle AI Python SDK

A Python client for interacting with the Qandle AI API.

## Installation

Install the package from PyPI:

```bash
pip install qandle-ai
```

## Configuration

The client can be configured using environment variables:

- `QANDLE_API_KEY`: Your Qandle AI API key (required)
- `QANDLE_API_URL`: The base URL for the Qandle AI API (optional, defaults to `https://api.qandle.ai`)

## Usage

### Basic Usage

```python
from qandle_ai import QandleClient

# Initialize the client (uses QANDLE_API_KEY environment variable)
client = QandleClient()

# Get stock summary
summary = client.get("AAPL")
print(summary)
```

### Custom Configuration

```python
from qandle_ai import QandleClient

# Initialize with custom API key and base URL
client = QandleClient(
    api_key="your-api-key-here",
    base_url="https://custom-api.qandle.ai"
)

# Get stock summary
summary = client.get("TSLA")
print(summary)
```

## API Reference

### QandleClient

#### `__init__(api_key=None, base_url=None)`

Initialize the Qandle AI client.

**Parameters:**
- `api_key` (str, optional): The API key for Qandle AI. If not provided, will attempt to get from `QANDLE_API_KEY` environment variable.
- `base_url` (str, optional): The base URL for the Qandle AI API. If not provided, will use the default `https://api.qandle.ai` or `QANDLE_API_URL` environment variable.

#### `get(symbol)`

Retrieve the current action summary for a stock using the Qandle AI API.

**Parameters:**
- `symbol` (str): The stock symbol for which to obtain the current action summary.

**Returns:**
- `str`: The stock summary message or error message.

## Error Handling

The client handles various types of errors and returns descriptive error messages:

- Missing API key: Raises `ValueError` during initialization
- Network errors: Returns error message with details
- JSON parsing errors: Returns error message with details
- Other unexpected errors: Returns generic error message 