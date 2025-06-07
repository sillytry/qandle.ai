"""
Qandle AI Python SDK

A Python client for interacting with the Qandle AI API.
"""

import os
import requests
import json
from typing import Optional


class QandleClient:
    """Client for interacting with the Qandle AI API."""
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """Initialize the Qandle AI client.
        
        Args:
            api_key (Optional[str]): The API key for Qandle AI. If not provided,
                                   will attempt to get from QANDLE_API_KEY environment variable.
            base_url (Optional[str]): The base URL for the Qandle AI API. If not provided,
                                    will use the default https://api.qandle.ai or QANDLE_API_URL environment variable.
        """
        self.api_key = api_key or os.getenv("QANDLE_API_KEY")
        self.base_url = base_url or os.getenv("QANDLE_API_URL", "https://api.qandle.ai")
        
        if not self.api_key:
            raise ValueError("API key is required. Set QANDLE_API_KEY environment variable or pass api_key parameter.")
    
    def get(self, symbol: str) -> str:
        """Retrieve the current action summary for a stock using the Qandle AI API.

        Args:
            symbol (str): The stock symbol for which to obtain the current action summary.
            
        Returns:
            str: The stock summary message or error message.
        """
        try:
            # Make API call to Qandle AI
            url = f"{self.base_url}/asset?symbol={symbol}"
            headers = {
                "x-api-key": self.api_key
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Parse JSON response
            data = response.json()
            
            # Extract message from response
            return data["message"] if "message" in data else f"No data available for {symbol}"
            
        except requests.RequestException as e:
            return f"Error fetching data for {symbol}: {str(e)}"
        except json.JSONDecodeError as e:
            return f"Error parsing response for {symbol}: {str(e)}"
        except Exception as e:
            return f"Unexpected error for {symbol}: {str(e)}" 