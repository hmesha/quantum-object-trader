# Quantum Trader

🤖 An intelligent stock trading bot combining technical & qualitative analysis with Interactive Brokers TWS API integration

## Description

Quantum Trader is a high-performance, production-ready algorithmic trading system that combines real-time technical analysis with natural language processing for sentiment-driven trading decisions. Built with Python, it features sub-100ms latency, comprehensive risk management, and a color-coded CLI interface for monitoring live trading operations.

## Key Features

- Real-time market data processing with <100ms latency
- Advanced technical indicators (SMA, EMA, VWAP, RSI, MACD, Bollinger Bands)
- Natural language processing for news and social media sentiment analysis
- Robust risk management and position sizing
- Interactive Brokers TWS API integration with auto-reconnection
- Color-coded CLI dashboard for real-time monitoring
- Comprehensive testing suite with >95% coverage

## Installation

### Prerequisites

- Python 3.11+
- Virtual environment tool (e.g., `venv`, `virtualenv`, `conda`)
- Git

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

3. Install dependencies:

```sh
pip install -r requirements/requirements.txt
```

4. Set up environment variables:

Create a `.env` file in the root directory of the project:

```sh
# .env file
IB_API_KEY=your_interactive_brokers_api_key
IB_API_SECRET=your_interactive_brokers_api_secret
GOOGLE_NEWS_API_KEY=your_google_news_api_key
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
```

5. Configure the bot:

Modify the configuration files in the `config` folder according to your requirements.

## Usage

You can run the trading bot using the CLI interface. For example, to execute a market order to buy 10 shares of AAPL, use the following command:

```sh
python -m trading_bot.src.cli.cli_interface --symbol AAPL --order_type market --quantity 10
```

## Documentation

For detailed information on the trading bot's architecture, setup, and usage, refer to the `docs` folder:

- [Setup Guide](docs/setup_guide.md)
- [User Manual](docs/user_manual.md)
- [API Documentation](docs/api_documentation.md)
- [Architecture Documentation](docs/architecture_documentation.md)
- [Analysis Tools Documentation](docs/analysis_tools.md)

## Contributing

We welcome contributions to Quantum Trader! Please read our [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact our support team at support@tradingbot.com.
