# User Manual

## Overview
This user manual provides detailed instructions on how to use the trading bot, including setup, configuration, and operation. The trading bot is designed to automate stock trading using both technical and qualitative analysis.

## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Configuration](#configuration)
4. [Running the Bot](#running-the-bot)
5. [CLI Interface](#cli-interface)
6. [Troubleshooting](#troubleshooting)
7. [Contact](#contact)

## Introduction
The trading bot is a high-performance, production-ready algorithmic trading system that combines real-time technical analysis with natural language processing for sentiment-driven trading decisions. Built with Python, it features sub-100ms latency, comprehensive risk management, and a color-coded CLI interface for monitoring live trading operations.

## Setup
Follow the steps in the [Setup Guide](trading_bot/docs/setup_guide.md) to set up the trading bot on your local machine. This includes cloning the repository, setting up a virtual environment, installing dependencies, and configuring environment variables.

## Configuration
The trading bot uses YAML-based configuration files to manage settings. There are three main configuration files:

- `trading_bot/config/config.yaml`: General configuration
- `trading_bot/config/config_dev.yaml`: Development configuration
- `trading_bot/config/config_prod.yaml`: Production configuration

### General Configuration
The general configuration file (`trading_bot/config/config.yaml`) includes settings for logging, API integration, data management, technical analysis, qualitative analysis, trading, and the CLI interface. Modify these settings according to your requirements.

### Development and Production Configuration
The development (`trading_bot/config/config_dev.yaml`) and production (`trading_bot/config/config_prod.yaml`) configuration files override the general configuration for specific environments. Use these files to set environment-specific settings.

## Running the Bot
You can run the trading bot using the CLI interface. For example, to execute a market order to buy 10 shares of AAPL, use the following command:

```sh
python -m trading_bot.src.cli.cli_interface --symbol AAPL --order_type market --quantity 10
```

## CLI Interface
The CLI interface provides a real-time dashboard for monitoring the trading bot's operations. It includes the following features:

- Real-time market data display
- Order execution status
- Position monitoring
- Risk management alerts

### Command-Line Arguments
The CLI interface accepts the following command-line arguments:

- `--symbol` (string, required): The stock symbol to trade
- `--order_type` (string, required): The type of order to place (e.g., market, limit, stop)
- `--quantity` (integer, required): The number of shares to trade
- `--price` (float, optional): The price for limit/stop orders

### Example Usage
To place a limit order to buy 50 shares of GOOGL at $2500, use the following command:

```sh
python -m trading_bot.src.cli.cli_interface --symbol GOOGL --order_type limit --quantity 50 --price 2500
```

## Troubleshooting
Refer to the [Troubleshooting Guide](trading_bot/docs/troubleshooting_guide.md) for common issues and their solutions. This guide includes information on error messages, connectivity issues, and performance optimization.

## Contact
For any questions or support, please contact our support team at support@tradingbot.com.
