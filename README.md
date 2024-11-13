# Quantum Trader

🤖 An intelligent autonomous trading system using multi-agent orchestration with OpenAI's Swarm framework

## Overview

Quantum Trader is a sophisticated algorithmic trading system that leverages Interactive Brokers' API and OpenAI's Swarm framework to make trading decisions. The system uses a multi-agent approach where specialized agents collaborate to analyze market data, assess risks, and execute trades.

## Key Features

### Multi-Agent Architecture

1. **Technical Analysis Agent**
   - Analyzes market data using technical indicators
   - Identifies trading patterns and signals
   - Provides technical-based recommendations

2. **Sentiment Analysis Agent**
   - Analyzes market sentiment from news and social media
   - Evaluates overall market sentiment
   - Provides sentiment-based signals

3. **Risk Management Agent**
   - Monitors position sizes and exposure
   - Enforces risk limits and parameters
   - Approves or rejects potential trades

4. **Trade Execution Agent**
   - Handles order placement and management
   - Optimizes trade timing and execution
   - Manages active positions

### Market Data Processing

- Real-time price updates
- Synchronized data management
- Volume tracking
- High/low price monitoring

### Risk Management

- Position size limits
- Daily loss limits
- Portfolio exposure monitoring
- Trade frequency controls

### System Monitoring

- Detailed logging
- Performance tracking
- Error handling
- System health monitoring

## Prerequisites

Before running the system, ensure you have:

1. **Python 3.10+**

2. **Interactive Brokers TWS or IB Gateway**
   - Download and install from [Interactive Brokers](https://www.interactivebrokers.com)
   - Enable API connections in TWS/Gateway settings
   - Configure the socket port (default: 7497)
   - Enable auto-restart in TWS/Gateway
   - Disable 'Read-Only API' in TWS/Gateway configuration

3. **Market Data Subscriptions**
   - Appropriate market data subscriptions for your symbols
   - Permissions for the markets you want to trade

## Installation

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

4. Install OpenAI Swarm:
```bash
pip install git+https://github.com/openai/swarm.git
```

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
  loss_limits:
    daily_loss_limit: 1000
```

### Agent System
```yaml
agent_system:
  update_interval: 60
  confidence_thresholds:
    technical: 0.7
    sentiment: 0.6
```

## Usage

### Starting the System

```bash
python -m src.cli.cli_interface --symbols AAPL MSFT GOOGL --mode paper
```

Required arguments:
- `--symbols`: List of stock symbols to trade
- `--mode`: Trading mode ('paper' or 'live', default: paper)

### Expected Behavior

1. **Startup**
   - System checks prerequisites
   - Connects to Interactive Brokers
   - Initializes trading agents
   - Begins market data processing

2. **Market Data**
   - Receives real-time price updates
   - Processes synchronized data
   - Tracks volume and price levels

3. **Trading Decisions**
   - Analyzes technical indicators
   - Evaluates market sentiment
   - Assesses risk parameters
   - Makes trading decisions

4. **Risk Management**
   - Enforces position limits
   - Monitors risk exposure
   - Validates all trades
   - Manages stop losses

## System Output

The system provides detailed logging:

```
2024-11-10 18:24:20,523 - INFO - === Quantum Trader Starting ===
2024-11-10 18:24:20,523 - INFO - Mode: paper
2024-11-10 18:24:20,523 - INFO - Symbols: ['AAPL', 'MSFT', 'GOOGL']
...
```

## Troubleshooting

### Common Issues

1. **Connection Problems**
   - Verify TWS/Gateway is running
   - Check API connection settings
   - Confirm port configuration
   - Ensure proper permissions

2. **Market Data Issues**
   - Verify market data subscriptions
   - Check symbol validity
   - Confirm market hours
   - Monitor data synchronization

3. **Trading Issues**
   - Check risk limits
   - Verify account permissions
   - Monitor order status
   - Check execution reports

### Error Messages

The system provides clear error messages with:
- Error description
- Context information
- Suggested solutions
- Debug details (in verbose mode)

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
