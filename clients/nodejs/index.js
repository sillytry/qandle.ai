import axios from 'axios';

/**
 * Client for interacting with the Qandle AI API
 */
class QandleClient {
  /**
   * Initialize the Qandle AI client
   * @param {Object} options - Configuration options
   * @param {string} [options.apiKey] - The API key for Qandle AI. If not provided, will use QANDLE_API_KEY environment variable
   * @param {string} [options.baseUrl] - The base URL for the Qandle AI API. If not provided, will use QANDLE_API_URL environment variable or default
   */
  constructor(options = {}) {
    this.apiKey = options.apiKey || process.env.QANDLE_API_KEY;
    this.baseUrl = options.baseUrl || process.env.QANDLE_API_URL || 'https://api.qandle.ai';
    
    if (!this.apiKey) {
      throw new Error('API key is required. Set QANDLE_API_KEY environment variable or pass apiKey in options.');
    }
  }

  /**
   * Retrieve the current action summary for a stock using the Qandle AI API
   * @param {string} symbol - The stock symbol for which to obtain the current action summary
   * @returns {Promise<string>} The stock summary message or error message
   */
  async get(symbol) {
    try {
      const url = `${this.baseUrl}/asset?symbol=${symbol}`;
      const response = await axios.get(url, {
        headers: {
          'x-api-key': this.apiKey
        }
      });

      const data = response.data;
      return data.message || `No data available for ${symbol}`;
    } catch (error) {
      if (error.response) {
        return `Error fetching data for ${symbol}: ${error.response.status} ${error.response.statusText}`;
      } else if (error.request) {
        return `Error fetching data for ${symbol}: Network error`;
      } else {
        return `Unexpected error for ${symbol}: ${error.message}`;
      }
    }
  }
}

export { QandleClient }; 