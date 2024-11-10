# Trading Bot Setup Guide

This guide will help you set up the trading bot on your local machine.

## Prerequisites

- Python 3.11+
- Virtual environment tool (e.g., `venv`, `virtualenv`, `conda`)
- Git

## Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```sh
git clone https://github.com/zoharbabin/quantum-trader.git
cd quantum-trader
```

## Step 2: Set Up Virtual Environment

Create and activate a virtual environment:

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

## Step 3: Install Dependencies

Install the required dependencies using the provided `requirements.txt` file:

```sh
pip install -r requirements/requirements.txt
```

## Step 4: Configuration

### Environment Variables

Set up the required environment variables for API keys and secrets. You can create a `.env` file in the root directory of the project:

```sh
# .env file
IB_API_KEY=your_interactive_brokers_api_key
IB_API_SECRET=your_interactive_brokers_api_secret
GOOGLE_NEWS_API_KEY=your_google_news_api_key
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
```

### Configuration Files

The project includes three configuration files:

- `config/config.yaml`: General configuration
- `config/config_dev.yaml`: Development configuration
- `config/config_prod.yaml`: Production configuration

You can modify these files according to your requirements.

## Step 5: Run the Bot

You can run the trading bot using the CLI interface. For example:

```sh
python -m trading_bot.src.cli.cli_interface --symbol AAPL --order_type market --quantity 10
```

This command will execute a market order to buy 10 shares of AAPL.

## Step 6: Testing

Run the test suite to ensure everything is set up correctly:

```sh
pytest
```

## Additional Resources

- [API Documentation](api_documentation.md)
- [User Manual](user_manual.md)
- [Troubleshooting Guide](troubleshooting_guide.md)
- [Architecture Documentation](architecture_documentation.md)

For any issues or questions, please refer to the [Troubleshooting Guide](troubleshooting_guide.md) or open an issue on the GitHub repository.

Happy trading!
