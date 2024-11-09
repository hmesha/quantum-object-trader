import unittest
from unittest.mock import patch, MagicMock
from trading_bot.src.api.api_connector import APIConnector

class TestAPIConnector(unittest.TestCase):

    @patch('trading_bot.src.api.api_connector.IB')
    def setUp(self, MockIB):
        self.mock_ib = MockIB.return_value
        self.connector = APIConnector(
            base_url='https://api.sandbox.interactivebrokers.com',
            api_key='test_key',
            api_secret='test_secret'
        )

    def test_connect_success(self):
        self.mock_ib.connect.return_value = True
        self.connector.connect()
        self.assertTrue(self.connector.is_connected())
        self.mock_ib.connect.assert_called_once_with(
            'https://api.sandbox.interactivebrokers.com', 'test_key', 'test_secret'
        )

    def test_connect_failure(self):
        self.mock_ib.connect.side_effect = ConnectionError("Connection failed")
        self.connector.connect()
        self.assertFalse(self.connector.is_connected())

    def test_disconnect(self):
        self.connector.connected = True
        self.connector.disconnect()
        self.assertFalse(self.connector.is_connected())
        self.mock_ib.disconnect.assert_called_once()

    def test_get_market_data_success(self):
        self.connector.connected = True
        self.mock_ib.reqMktData.return_value = 'market_data'
        market_data = self.connector.get_market_data('AAPL')
        self.assertEqual(market_data, 'market_data')
        self.mock_ib.reqMktData.assert_called_once()

    def test_get_market_data_not_connected(self):
        self.connector.connected = False
        market_data = self.connector.get_market_data('AAPL')
        self.assertIsNone(market_data)

    def test_place_order_success(self):
        self.connector.connected = True
        self.mock_ib.placeOrder.return_value = 'order'
        order = self.connector.place_order('AAPL', 'MKT', 10)
        self.assertEqual(order, 'order')
        self.mock_ib.placeOrder.assert_called_once()

    def test_place_order_not_connected(self):
        self.connector.connected = False
        order = self.connector.place_order('AAPL', 'MKT', 10)
        self.assertIsNone(order)

    def test_monitor_positions_success(self):
        self.connector.connected = True
        self.mock_ib.positions.return_value = 'positions'
        positions = self.connector.monitor_positions()
        self.assertEqual(positions, 'positions')
        self.mock_ib.positions.assert_called_once()

    def test_monitor_positions_not_connected(self):
        self.connector.connected = False
        positions = self.connector.monitor_positions()
        self.assertIsNone(positions)

    def test_monitor_account_success(self):
        self.connector.connected = True
        self.mock_ib.accountSummary.return_value = 'account_summary'
        account_summary = self.connector.monitor_account()
        self.assertEqual(account_summary, 'account_summary')
        self.mock_ib.accountSummary.assert_called_once()

    def test_monitor_account_not_connected(self):
        self.connector.connected = False
        account_summary = self.connector.monitor_account()
        self.assertIsNone(account_summary)

if __name__ == '__main__':
    unittest.main()
