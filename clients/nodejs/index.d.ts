export interface QandleClientOptions {
  apiKey?: string;
  baseUrl?: string;
}

export declare class QandleClient {
  constructor(options?: QandleClientOptions);
  get(symbol: string): Promise<string>;
}

export = QandleClient; 