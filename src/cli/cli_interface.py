import argparse
from src.trading.trading_logic import TradingLogic
from src.analysis.technical_analysis import TechnicalAnalysis
import yaml
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--symbol", required=True, help="Stock symbol to trade")
    parser.add_argument("--order_type", required=True, choices=["market", "limit", "stop"], help="Type of order")
    parser.add_argument("--quantity", required=True, type=int, help="Quantity of shares to trade")
    parser.add_argument("--price", type=float, help="Price for limit/stop orders")

    args = parser.parse_args()

    with open('src/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Load market data (this is a placeholder, replace with actual data loading logic)
    market_data = pd.DataFrame({
        'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'high': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'low': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'volume': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    })

    technical_analysis = TechnicalAnalysis(market_data)
    trading_logic = TradingLogic(config, technical_analysis)

    if args.order_type in ["limit", "stop"] and args.price is None:
        print("Error: Price must be specified for limit/stop orders")
        return

    trading_logic.execute_trade(args.symbol, args.order_type, args.quantity, args.price)

if __name__ == "__main__":
    main()
