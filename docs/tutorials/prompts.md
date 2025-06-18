---
icon: "material/application-braces-outline"
---

# Example **Prompts**

This page contains example prompts that demonstrate how to effectively use Qandle AI in various scenarios. These prompts are designed to leverage financial data intelligence for informed decision-making.

## Do I Own Winners?

**Description:** Displays your portfolio stocks side-by-side with their industry ETF benchmarks in a detailed table. Shows raw metrics without analysis so you can see if you own the winners.

**Use Case:** Compare your individual stock holdings with their respective industry benchmarks to evaluate portfolio performance at a glance.

**Parameters:** `symbols` (string, required): Stock symbols to analyze (comma-separated, e.g., 'AAPL,GOOGL,TSLA')

**Prompt:**

```text
PERSONA: Portfolio data analyst specializing in comprehensive stock and 
sector information display

TASK: Take comma-separated stock symbols input ${symbols} from user portfolio, 
retrieve matching industry ETF benchmarks, get comprehensive summaries for
all assets, present factual data side-by-side without analysis or interpretation

CONTEXT: User needs comprehensive factual overview of portfolio holdings 
alongside their respective industry benchmarks for personal evaluation

FORMAT: Output rich detailed information table displaying stock metrics adjacent 
to corresponding industry ETF metrics with clear data presentation and no 
comparative analysis or rankings
```

**Example Usage:**
```
Symbols: AAPL,MSFT,NVDA
```

This prompt will generate a comprehensive table comparing your holdings (AAPL, MSFT, NVDA) with their respective industry ETF benchmarks, allowing you to assess whether you're holding market winners or laggards.

!!! tip "Best Practices"
    - Use uppercase ticker symbols for consistency
    - Separate multiple symbols with commas
    - The prompt focuses on data presentation without bias, letting you draw your own conclusions
    - Industry ETF benchmarks are automatically matched to each stock for relevant comparison