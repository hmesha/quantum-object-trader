# Quantum Trader

🤖 An intelligent autonomous trading system using a multi-agent architecture for algorithmic trading via Interactive Brokers

## Overview

Quantum Trader is a sophisticated algorithmic trading system that leverages Interactive Brokers' API to make trading decisions. The system uses a multi-agent approach where specialized components collaborate to analyze market data, assess risks, and execute trades.

## Key Features

### Multi-Agent Architecture

1. **Technical Analysis Agent**
   - Analyzes market data using multiple indicators:
     - SMA (20, 50, 200 periods)
     - EMA (12, 26 periods)
     - RSI
     - MACD
     - Bollinger Bands
   - Identifies trading patterns and signals

2. **Sentiment Analysis Agent**
   - Analyzes market sentiment from news and social media
   - Monitors multiple platforms (Twitter, Reddit)
   - Provides weighted sentiment signals

3. **Risk Management System**
   - Position size and portfolio exposure limits
   - Daily loss limits and drawdown protection
   - Trade frequency controls
   - Dynamic stop-loss using ATR

4. **Trade Execution System**
   - Supports market and limit orders
   - Slippage tolerance controls
   - Position sizing based on risk or fixed size
   - Order timeout management

## Training Program

A comprehensive training program is included to help you understand and effectively use Quantum Trader.

### Running the Training Program

1. Start the development server (with no-cache for instant content updates):
```bash
cd training
python3 server.py
```

Alternatively, you can use the basic Python server (note: content changes may be cached):
```bash
cd training
python3 -m http.server 8000
```

2. Open your web browser and visit: `http://localhost:8000`

### Training Structure

1. **Level 1: Getting Started (Trader - Basic)**
   - Prerequisites
   - System Setup
   - Basic Operations
   - Risk Management Fundamentals

2. **Level 2: Intermediate Trading**
   - Advanced configuration
   - Portfolio management
   - Technical analysis implementation

3. **Level 3: Advanced Operations**
   - Custom strategy development
   - Advanced risk metrics
   - System optimization

### Training Resources

- Interactive tutorials with step-by-step guidance
- Practical exercises to reinforce learning
- Progress tracking
- Quizzes to test understanding
- Comprehensive documentation for each module

## Prerequisites

1. **Python 3.10+**

2. **Interactive Brokers TWS or IB Gateway**
   - Download and install from [Interactive Brokers](https://www.interactivebrokers.com)
   - Enable API connections in TWS/Gateway
   - Configure the socket port (default: 7497)
   - Enable auto-restart in TWS/Gateway
   - Disable 'Read-Only API' in TWS/Gateway configuration

3. **Market Data Subscriptions**
   - Appropriate market data subscriptions for your symbols
   - Permissions for the markets you want to trade

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/zoharbabin/quantum-trader.git
cd quantum-trader
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the system:
   - Review and modify `src/config/config.yaml` for your needs
   - Key configurations include:
     - API connection settings
     - Risk management parameters
     - Trading execution preferences
     - Analysis thresholds

5. Start trading:
```bash
python -m src.cli.cli_interface --symbols AAPL MSFT GOOGL --mode paper
```

Required arguments:
- `--symbols`: List of stock symbols to trade
- `--mode`: Trading mode ('paper' or 'live', default: paper)

## Configuration

The system is configured through `src/config/config.yaml`. Key sections include:

### API Configuration
```yaml
api:
  tws_endpoint: "127.0.0.1"
  port: 7497
```

### Risk Management
```yaml
risk_management:
  position_limits:
    max_position_size: 100
    max_portfolio_exposure: 0.25
  loss_limits:
    daily_loss_limit: 1000
    max_drawdown: 0.15
  trade_frequency:
    min_time_between_trades: 300
    max_daily_trades: 10
```

### Technical Analysis
```yaml
technical_analysis:
  indicators:
    sma_periods: [20, 50, 200]
    rsi:
      period: 14
      overbought: 70
      oversold: 30
    macd:
      fast_period: 12
      slow_period: 26
      signal_period: 9
```

### Trading Execution
```yaml
execution:
  order_types: ["market", "limit"]
  default_order_type: "limit"
  limit_order_timeout: 60
  slippage_tolerance: 0.001
```

## System Output

The system provides detailed logging of all operations:

```
2024-11-10 18:24:20,523 - INFO - === Quantum Trader Starting ===
2024-11-10 18:24:20,523 - INFO - Mode: paper
2024-11-10 18:24:20,523 - INFO - Symbols: ['AAPL', 'MSFT', 'GOOGL']
2024-11-10 18:24:20,524 - INFO - Checking Interactive Brokers prerequisites...
2024-11-10 18:24:20,525 - INFO - Successfully connected to Interactive Brokers
```

## Troubleshooting

### Common Issues

1. **Connection Problems**
   - Verify TWS/Gateway is running
   - Check API connection settings in TWS/Gateway
   - Confirm port configuration matches config.yaml
   - Ensure proper permissions in TWS/Gateway

2. **Market Data Issues**
   - Verify market data subscriptions
   - Check symbol validity
   - Confirm market hours
   - Monitor data synchronization logs

3. **Trading Issues**
   - Check risk limits in config.yaml
   - Verify account permissions in TWS/Gateway
   - Monitor order status in logs
   - Review execution reports

## Documentation

Detailed documentation is available in the `docs` directory:

- [CLI Interface](docs/cli_interface.md)
- [IB Connector](docs/ib_connector.md)
- [Trading Logic](docs/trading_logic.md)
- [Technical Analysis](docs/technical_analysis.md)
- [Sentiment Analysis](docs/sentiment_analysis.md)

## Testing

Run the test suite:

```bash
python -m unittest discover tests
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
