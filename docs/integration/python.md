---
icon: "material/language-python"
---

# Python SDK

A Python client for interacting with the Qandle AI API. The SDK provides a simple and intuitive interface to access financial market data and analysis.

## Installation

Install the package from PyPI using pip:

```bash
pip install qandle-ai
```

### Requirements

- Python ≥3.7

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

=== "Python (.env file)"

    ```python
    import os
    from dotenv import load_dotenv
    
    load_dotenv()  # Load environment variables from .env file
    ```

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

The main class for interacting with the Qandle AI API.

#### Constructor

```python
QandleClient(api_key=None, base_url=None)
```

**Parameters:**

- `api_key` (str, optional): The API key for Qandle AI. If not provided, will attempt to get from `QANDLE_API_KEY` environment variable.
- `base_url` (str, optional): The base URL for the Qandle AI API. If not provided, will use the default `https://api.qandle.ai` or `QANDLE_API_URL` environment variable.

**Raises:**

- `ValueError`: If no API key is provided and `QANDLE_API_KEY` environment variable is not set.

#### Methods

### `get(symbol)`

Retrieve the current action summary for a stock using the Qandle AI API.

**Parameters:**

- `symbol` (str): The stock symbol for which to obtain the current action summary (e.g., "AAPL", "GOOGL", "TSLA").

**Returns:**

- `str`: The stock summary message containing analysis and recommendations.

**Example:**

```python
client = QandleClient()
result = client.get("AAPL")
print(result)
```