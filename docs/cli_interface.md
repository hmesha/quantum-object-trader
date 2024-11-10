# CLI Interface Documentation

## Overview

The CLI interface provides a command-line tool for interacting with the trading system. It offers commands for executing trades, monitoring positions, and managing the trading bot.

## Command Structure

### Basic Command Format
```bash
python -m src.cli.cli_interface [command] [options]
```

### Global Options
- `--verbose`: Enable detailed logging
- `--config`: Specify custom config file path
- `--output`: Specify output format (text/json)

## Available Commands

### Trading Commands

#### Execute Order
```bash
python -m src.cli.cli_interface --symbol AAPL --order_type market --quantity 100
```

Options:
- `--symbol`: Stock symbol (required)
- `--order_type`: Type of order (market/limit/stop) (required)
- `--quantity`: Number of shares (required)
- `--price`: Price for limit/stop orders
- `--action`: BUY/SELL (default: BUY)

#### Cancel Order
```bash
python -m src.cli.cli_interface cancel --order_id 12345
```

Options:
- `--order_id`: ID of order to cancel (required)

### Monitoring Commands

#### Show Positions
```bash
python -m src.cli.cli_interface positions
```

Options:
- `--symbol`: Filter by symbol
- `--min_value`: Minimum position value
- `--format`: Output format (table/json)

#### Show Orders
```bash
python -m src.cli.cli_interface orders
```

Options:
- `--status`: Filter by status (open/filled/cancelled)
- `--symbol`: Filter by symbol
- `--start_date`: Filter by start date
- `--end_date`: Filter by end date

### Configuration Commands

#### Show Config
```bash
python -m src.cli.cli_interface config show
```

#### Update Config
```bash
python -m src.cli.cli_interface config update --key value
```

### System Commands

#### Check Status
```bash
python -m src.cli.cli_interface status
```

Shows:
- Connection status
- System health
- API rate limits
- Active processes

#### Start Bot
```bash
python -m src.cli.cli_interface start
```

Options:
- `--strategy`: Trading strategy to use
- `--symbols`: Symbols to trade
- `--paper_trading`: Enable paper trading mode

#### Stop Bot
```bash
python -m src.cli.cli_interface stop
```

## Error Handling

### Exit Codes
- 0: Success
- 1: General error
- 2: Configuration error
- 3: Connection error
- 4: Order error

### Error Messages
- Clear error descriptions
- Suggested solutions
- Debug information in verbose mode

## Configuration

### Environment Variables
```bash
TRADING_BOT_CONFIG=/path/to/config.yaml
TRADING_BOT_LOG_LEVEL=INFO
TRADING_BOT_OUTPUT_FORMAT=text
```

### Config File
```yaml
cli:
  default_output: text
  color_enabled: true
  timestamp_format: "%Y-%m-%d %H:%M:%S"
  log_level: INFO
```

## Integration

The CLI interface integrates with:
1. Trading system core functionality
2. Real-time dashboard
3. Configuration management
4. Logging system

## Examples

### Basic Trading
```bash
# Buy 100 shares of AAPL at market price
python -m src.cli.cli_interface --symbol AAPL --order_type market --quantity 100

# Sell 50 shares of GOOGL with limit price
python -m src.cli.cli_interface --symbol GOOGL --order_type limit --quantity 50 --price 150.00 --action SELL

# Check current positions
python -m src.cli.cli_interface positions

# View open orders
python -m src.cli.cli_interface orders --status open
```

### Bot Management
```bash
# Start bot with specific strategy
python -m src.cli.cli_interface start --strategy momentum --symbols AAPL,GOOGL,MSFT

# Check bot status
python -m src.cli.cli_interface status

# Stop bot
python -m src.cli.cli_interface stop
```

### Configuration
```bash
# Show current config
python -m src.cli.cli_interface config show

# Update config value
python -m src.cli.cli_interface config update max_position_size 1000
