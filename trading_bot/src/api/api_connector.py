import time
import logging
from ib_insync import IB, util
from requests.exceptions import ConnectionError

class APIConnector:
    def __init__(self, base_url, api_key, api_secret, reconnect_attempts=5, reconnect_backoff=2):
        self.base_url = base_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.reconnect_attempts = reconnect_attempts
        self.reconnect_backoff = reconnect_backoff
        self.ib = IB()
        self.logger = logging.getLogger(__name__)
        self.connected = False

    def connect(self):
        attempt = 0
        while attempt < self.reconnect_attempts:
            try:
                self.ib.connect(self.base_url, self.api_key, self.api_secret)
                self.connected = True
                self.logger.info("Connected to Interactive Brokers API")
                return
            except ConnectionError as e:
                self.logger.error(f"Connection failed: {e}")
                attempt += 1
                time.sleep(self.reconnect_backoff ** attempt)
        self.logger.error("Failed to connect to Interactive Brokers API after multiple attempts")

    def disconnect(self):
        if self.connected:
            self.ib.disconnect()
            self.connected = False
            self.logger.info("Disconnected from Interactive Brokers API")

    def is_connected(self):
        return self.connected

    def get_market_data(self, symbol):
        if not self.connected:
            self.logger.error("Not connected to Interactive Brokers API")
            return None
        try:
            contract = util.symbol(symbol)
            market_data = self.ib.reqMktData(contract)
            return market_data
        except Exception as e:
            self.logger.error(f"Error getting market data: {e}")
            return None

    def place_order(self, symbol, order_type, quantity, price=None):
        if not self.connected:
            self.logger.error("Not connected to Interactive Brokers API")
            return None
        try:
            contract = util.symbol(symbol)
            order = util.createOrder(order_type, quantity, price)
            trade = self.ib.placeOrder(contract, order)
            return trade
        except Exception as e:
            self.logger.error(f"Error placing order: {e}")
            return None

    def monitor_positions(self):
        if not self.connected:
            self.logger.error("Not connected to Interactive Brokers API")
            return None
        try:
            positions = self.ib.positions()
            return positions
        except Exception as e:
            self.logger.error(f"Error monitoring positions: {e}")
            return None

    def monitor_account(self):
        if not self.connected:
            self.logger.error("Not connected to Interactive Brokers API")
            return None
        try:
            account_summary = self.ib.accountSummary()
            return account_summary
        except Exception as e:
            self.logger.error(f"Error monitoring account: {e}")
            return None

    def handle_rate_limit(self):
        self.logger.warning("Rate limit reached. Pausing requests.")
        time.sleep(60)  # Sleep for 60 seconds before retrying

    def validate_configuration(self):
        if not self.api_key or not self.api_secret:
            self.logger.error("API key or secret is missing in the configuration")
            raise ValueError("API key or secret is missing in the configuration")
        if not self.base_url:
            self.logger.error("Base URL is missing in the configuration")
            raise ValueError("Base URL is missing in the configuration")
