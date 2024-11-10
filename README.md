# Quantum Trader

🤖 An intelligent stock trading bot combining technical & sentiment analysis with Interactive Brokers TWS API integration

## Description

Quantum Trader is a high-performance, production-ready algorithmic trading system that combines real-time technical analysis with natural language processing for sentiment-driven trading decisions. Built with Python, it features sub-100ms latency, comprehensive risk management, and a color-coded CLI interface for monitoring live trading operations.

## Key Features

- Real-time market data processing with <100ms latency
- Advanced technical indicators:
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
  - Volume Weighted Average Price (VWAP)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
  - Bollinger Bands
  - Average True Range (ATR)
  - Average Directional Index (ADX)
  - Commodity Channel Index (CCI)
- Sentiment analysis using:
  - News articles analysis via NewsAPI
  - Social media sentiment via Twitter API
  - Natural language processing with TextBlob
- Interactive Brokers TWS API integration with auto-reconnection
- Color-coded CLI dashboard for real-time monitoring
- Comprehensive testing suite with >95% coverage

## Installation

### Prerequisites

- Python 3.11+
- Virtual environment tool (e.g., `venv`, `virtualenv`, `conda`)
- Git
- Interactive Brokers Trader Workstation (TWS) or IB Gateway
- NewsAPI key for news sentiment analysis
- Twitter API keys for social media sentiment analysis

### Steps

1. Clone the repository:

```sh
git clone https://github.com/zoharbabin/quantum-trader.git
cd quantum-trader
```

2. Set up a virtual environment:

```sh
# Using venv
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Using virtualenv
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Using conda
conda create --name trading_bot python=3.11
conda activate trading_bot
```

3. Install Interactive Brokers TWS API:
   - Download the IBAPI from the official Interactive Brokers GitHub page: https://interactivebrokers.github.io/
   - Follow the installation instructions in the downloaded package
   - Ensure the TWS API is properly set up and configured in your environment

4. Install other dependencies:

```sh
pip install -r requirements.txt
```

5. Set up environment variables:

Create a `.env` file in the root directory of the project:

```sh
# .env file
NEWS_API_KEY=your_news_api_key
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
```

6. Configure the bot:

Modify the configuration file in `src/config/config.yaml` according to your requirements.

## Usage

You can run the trading bot using the CLI interface:

```sh
python -m src.cli.cli_interface --symbol AAPL --order_type market --quantity 10
```

## Documentation

Comprehensive documentation for all system components:

- [Technical Analysis](./docs/technical_analysis.md) - Technical indicators and their implementation
- [Sentiment Analysis](./docs/sentiment_analysis.md) - News and social media sentiment analysis
- [Interactive Brokers Integration](./docs/ib_connector.md) - TWS API integration and order management
- [CLI Interface](./docs/cli_interface.md) - Command-line interface usage and options
- [Dashboard](./docs/dashboard.md) - Real-time monitoring interface
- [Trading Logic](./docs/trading_logic.md) - Core trading algorithms and risk management

## Unit Tests

The `tests` directory contains unit tests for various components of the trading bot. To run the tests:

```sh
python -m unittest discover tests
```

## API Integration

The `src/api/ib_connector.py` file handles Interactive Brokers TWS API integration, including:
- Connection management and auto-reconnection
- Order execution and monitoring
- Real-time market data streaming
- Error handling and rate limit monitoring

## Real-time Dashboard

The `src/cli/dashboard.py` provides a color-coded CLI interface for monitoring:
- Live trading operations
- Technical indicator values
- Sentiment analysis scores
- Position status and P&L
- Order execution status

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
