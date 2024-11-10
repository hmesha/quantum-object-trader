import argparse
import logging
import time
from colorama import Fore, Style, init
from trading_bot.src.trading.trading_logic import TradingLogic
from trading_bot.config.config import config

class CLIInterface:
    def __init__(self):
        self.trading_logic = TradingLogic(config)
        self.logger = logging.getLogger(__name__)
        init(autoreset=True)

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Trading Bot CLI")
        parser.add_argument("--symbol", type=str, required=True, help="Stock symbol to trade")
        parser.add_argument("--order_type", type=str, required=True, choices=["market", "limit", "stop"], help="Type of order to place")
        parser.add_argument("--quantity", type=int, required=True, help="Quantity of shares to trade")
        parser.add_argument("--price", type=float, help="Price for limit/stop orders")
        return parser.parse_args()

    def display_dashboard(self):
        while True:
            # Placeholder for real-time dashboard display logic
            print(Fore.GREEN + "Real-time Dashboard")
            time.sleep(config['cli']['refresh_interval'])

    def run(self):
        args = self.parse_arguments()
        self.logger.info(f"Parsed arguments: {args}")

        # Error handling for CLI input issues
        if args.quantity <= 0:
            self.logger.error("Quantity must be greater than zero")
            return
        if args.order_type in ["limit", "stop"] and args.price is None:
            self.logger.error("Price must be specified for limit/stop orders")
            return

        if not self.trading_logic.api_connector.is_connected():
            self.trading_logic.api_connector.connect()

        if self.trading_logic.manage_risk(args.symbol, args.quantity, args.price):
            self.trading_logic.execute_trade(args.symbol, args.order_type, args.quantity, args.price)
        else:
            self.logger.error("Risk management rules violated. Trade not executed.")

        self.display_dashboard()

if __name__ == "__main__":
    cli = CLIInterface()
    cli.run()
