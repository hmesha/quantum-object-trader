import time
from colorama import Fore, Style, init
from src.trading.trading_logic import TradingLogic
import yaml

with open('src/config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

class Dashboard:
    def __init__(self):
        self.trading_logic = TradingLogic(config)
        init(autoreset=True)

    def display_dashboard(self):
        while True:
            # Placeholder for real-time dashboard display logic
            print(Fore.GREEN + "Real-time Dashboard")
            print(Fore.YELLOW + "Performance Metrics:")
            print(Fore.CYAN + "Positions/Orders Status:")
            print(Fore.RED + "Alerts:")
            time.sleep(config['cli']['refresh_interval'])

    def run(self):
        self.display_dashboard()

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()
