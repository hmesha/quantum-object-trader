# API Documentation

## Overview
This document provides detailed information about the API endpoints, request parameters, and response formats for the trading bot. The API allows users to interact with the trading bot programmatically, enabling automated trading, data retrieval, and account management.

## Base URL
The base URL for the API is:
```
https://api.tradingbot.com/v1
```

## Authentication
All API requests require authentication using an API key. The API key must be included in the request headers as follows:
```
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### 1. Market Data

#### Get Real-Time Market Data
**Endpoint:** `/market_data`

**Method:** `GET`

**Description:** Retrieves real-time market data for a specified stock symbol.

**Request Parameters:**
- `symbol` (string, required): The stock symbol to retrieve data for.

**Response:**
```json
{
  "symbol": "AAPL",
  "price": 150.25,
  "volume": 1000000,
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### 2. Trading

#### Place Order
**Endpoint:** `/orders`

**Method:** `POST`

**Description:** Places a new order for a specified stock.

**Request Parameters:**
- `symbol` (string, required): The stock symbol to trade.
- `order_type` (string, required): The type of order (e.g., market, limit, stop).
- `quantity` (integer, required): The number of shares to trade.
- `price` (float, optional): The price for limit/stop orders.

**Response:**
```json
{
  "order_id": "12345",
  "status": "submitted",
  "symbol": "AAPL",
  "order_type": "limit",
  "quantity": 100,
  "price": 150.00,
  "timestamp": "2024-01-01T12:01:00Z"
}
```

#### Cancel Order
**Endpoint:** `/orders/{order_id}`

**Method:** `DELETE`

**Description:** Cancels an existing order.

**Request Parameters:**
- `order_id` (string, required): The ID of the order to cancel.

**Response:**
```json
{
  "order_id": "12345",
  "status": "cancelled",
  "timestamp": "2024-01-01T12:02:00Z"
}
```

### 3. Account

#### Get Account Summary
**Endpoint:** `/account/summary`

**Method:** `GET`

**Description:** Retrieves the account summary, including balance, positions, and P&L.

**Response:**
```json
{
  "balance": 100000.00,
  "positions": [
    {
      "symbol": "AAPL",
      "quantity": 100,
      "average_price": 150.00,
      "current_price": 150.25,
      "pnl": 25.00
    }
  ],
  "total_pnl": 25.00,
  "timestamp": "2024-01-01T12:03:00Z"
}
```

## Error Handling
The API uses standard HTTP status codes to indicate the success or failure of a request. In case of an error, the response will include an error message in the following format:
```json
{
  "error": "Invalid API key",
  "code": 401
}
```

## Rate Limiting
To ensure fair usage, the API enforces rate limits on the number of requests per minute. If the rate limit is exceeded, the API will return a `429 Too Many Requests` status code.

## Contact
For any questions or support, please contact our support team at support@tradingbot.com.
