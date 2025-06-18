---
icon: "material/api"
---

# /GET Symbol

Retrieve comprehensive financial intelligence for any stock symbol in a single API call. Get pre-computed technical indicators, price data, volume analysis, and support/resistance levels optimized for AI applications.

## Endpoint

```
GET https://api.qandle.ai/asset?symbol={symbol}
```

## Authentication

Include your API key in the request header:

```
x-api-key: YOUR_API_KEY
```

!!! tip "Get your API key"
    Visit [qandle.ai](https://www.qandle.ai) to create an account and generate your API key.

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | ✅ Required | Stock symbol (e.g., "AAPL", "NVDA", "TSLA") |

## Response Format

The API returns a JSON object with a `message` field containing the formatted financial intelligence:

```json
{
  "message": "PRICE: NVDA 143.85 -1.63 (-1.12%) | Range: 142.65-146.20 |Range_position: 33.80% | Gap: down -0.03\nMOVING_AVERAGES: 20MA:139.64+3.01% 50MA:125.49 (+14.63%) 200MA:128.06(+12.33%) Order: 20>200>50 Slopes: 20: +25.66° 50: +36.96° 200:+4.99°\nVOLUME: Current:242.40M | vs_20d_avg:117x | vs_yesterday:1.50x 5d_trend:down\nPRICE_LEVELS: Test_count R:144.37:4x S:143.74:2x | Distance_to R: -0.52(-0.36%) S:0.11(+0.07%) | Last_touch R:8d S:15d"
}
```

## Data Sections

The response message contains structured financial intelligence in these sections:

**PRICE**: Current price, change, percentage change, daily range, range position, and gap analysis

**MOVING_AVERAGES**: 20, 50, and 200-day moving averages with relative positions, order, and slope angles

**VOLUME**: Current volume vs historical averages and trends

**PRICE_LEVELS**: Support and resistance levels with test counts, distances, and last touch dates

## Example Request

=== "cURL"

    ```bash
    curl -X GET "https://api.qandle.ai/asset?symbol=AAPL" \
         -H "x-api-key: YOUR_API_KEY"
    ```

=== "Python"

    ```python
    from qandle_ai import QandleClient
    
    client = QandleClient()
    summary = client.get("AAPL")
    print(summary)
    ```

=== "Node.js"

    ```javascript
    import { QandleClient } from 'qandle-ai';
    
    const client = new QandleClient();
    const summary = await client.get('AAPL');
    console.log(summary);
    ```

## Error Responses

The API returns appropriate HTTP status codes and error messages:

- `400` - Bad Request (invalid symbol format)
- `401` - Unauthorized (invalid or missing API key)
- `404` - Not Found (symbol not found)
- `429` - Too Many Requests (rate limit exceeded)
- `500` - Internal Server Error

## SDK Integration

For easier integration, use our official SDKs:

- **[Python SDK](../integration/python.md)** - `pip install qandle-ai`
- **[Node.js SDK](../integration/nodejs.md)** - `npm install qandle-ai`
- **[MCP Server](../integration/mcp-server.md)** - Zero-code integration with AI assistants