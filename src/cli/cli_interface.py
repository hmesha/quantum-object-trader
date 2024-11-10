import argparse
from src.trading.trading_logic import TradingLogic
from src.config.config import config

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--symbol", required=True, help="Stock symbol to trade")
    parser.add_argument("--order_type", required=True, choices=["market", "limit", "stop"], help="Type of order")
    parser.add_argument("--quantity", required=True, type=int, help="Quantity of shares to trade")
    parser.add_argument("--price", type=float, help="Price for limit/stop orders")

    args = parser.parse_args()

    trading_logic = TradingLogic(config)

    if args.order_type in ["limit", "stop"] and args.price is None:
        print("Error: Price must be specified for limit/stop orders")
        return

    trading_logic.execute_trade(args.symbol, args.order_type, args.quantity, args.price)

if __name__ == "__main__":
    main()
