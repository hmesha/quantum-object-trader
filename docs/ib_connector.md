# Interactive Brokers Connector Documentation

## Overview

The IB Connector module provides integration with Interactive Brokers' Trader Workstation (TWS) API, handling market data streaming, order execution, and connection management.

## Connection Management

### Initialization
```python
from src.api.ib_connector import IBConnector

connector = IBConnector(
    host="127.0.0.1",  # TWS/Gateway host
    port=7497,         # TWS/Gateway port
    client_id=1        # Unique client identifier
)
```

### Auto-Reconnection
The connector implements automatic reconnection logic:
- Detects connection drops
- Implements exponential backoff
- Maintains state during reconnection
- Resubscribes to market data feeds
- Resynchronizes open orders and positions

## Market Data

### Real-time Data Streaming
- Subscribes to market data feeds
- Processes tick-by-tick data
- Handles multiple data types:
  - Trade data
  - Bid/Ask quotes
  - Volume
  - OHLC data

### Data Management
- Efficient data buffering
- Rate limit monitoring
- Data validation
- Error handling

## Order Management

### Order Types
Supports multiple order types:
- Market orders
- Limit orders
- Stop orders
- Stop-limit orders
- Trailing stop orders

### Order Operations
```python
# Place a market order
order_id = connector.place_market_order(
    symbol="AAPL",
    quantity=100,
    action="BUY"
)

# Place a limit order
order_id = connector.place_limit_order(
    symbol="AAPL",
    quantity=100,
    action="BUY",
    limit_price=150.00
)

# Cancel an order
connector.cancel_order(order_id)
```

### Order Monitoring
- Real-time order status updates
- Fill price tracking
- Partial fills handling
- Order modification support

## Position Management

### Position Tracking
- Real-time position updates
- Average cost calculation
- P&L monitoring
- Position reconciliation

### Risk Management
- Position size limits
- Exposure monitoring
- Stop loss management
- Take profit management

## Error Handling

### Error Types
- Connection errors
- Order rejection errors
- Market data errors
- System errors

### Error Recovery
- Automatic error classification
- Recovery strategies
- Error logging
- Alert generation

## Rate Limiting

### TWS API Rate Limits
- Request rate monitoring
- Queue management
- Throttling implementation
- Burst handling

### Best Practices
- Batch similar requests
- Implement request spacing
- Monitor API usage
- Handle rate limit errors

## Logging

### Log Levels
- ERROR: Critical failures
- WARNING: Potential issues
- INFO: Normal operations
- DEBUG: Detailed debugging

### Log Categories
- Connection events
- Order operations
- Market data events
- Error events

## Configuration

### Required Settings
```yaml
ib_connector:
  host: "127.0.0.1"
  port: 7497
  client_id: 1
  reconnect_attempts: 5
  reconnect_interval: 10
  market_data_type: "DELAYED"  # or "REALTIME"
```

### Optional Settings
```yaml
ib_connector:
  log_level: "INFO"
  max_requests_per_second: 50
  connection_timeout: 30
  market_data_timeout: 10
```

## Usage Example

```python
from src.api.ib_connector import IBConnector

# Initialize connector
connector = IBConnector(
    host="127.0.0.1",
    port=7497,
    client_id=1
)

# Connect to TWS
connector.connect()

# Subscribe to market data
connector.subscribe_market_data("AAPL")

# Place a trade
order_id = connector.place_market_order(
    symbol="AAPL",
    quantity=100,
    action="BUY"
)

# Monitor order status
status = connector.get_order_status(order_id)

# Close connection
connector.disconnect()
```

## Integration

The IB Connector integrates with other system components:
1. Provides market data to technical analysis module
2. Executes trades based on trading logic signals
3. Reports position updates to dashboard
4. Logs all operations for analysis and debugging
