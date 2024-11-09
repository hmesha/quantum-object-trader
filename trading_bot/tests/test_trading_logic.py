import unittest
from unittest.mock import patch, MagicMock
from trading_bot.src.trading.trading_logic import TradingLogic

class TestTradingLogic(unittest.TestCase):

    def setUp(self):
        self.config = {
            'api': {
                'base_url': 'https://api.sandbox.interactivebrokers.com',
                'api_key': 'test_api_key',
                'api_secret': 'test_api_secret',
                'reconnect_attempts': 5,
                'reconnect_backoff': 2
            },
            'qualitative_analysis': {
                'google_news_api_key': 'test_google_news_api_key',
                'twitter_api_key': 'test_twitter_api_key',
                'twitter_api_secret': 'test_twitter_api_secret'
            },
            'trading': {
                'max_position_size': 100,
                'daily_loss_limit': 1000,
                'max_trade_frequency': 10
            }
        }
        self.trading_logic = TradingLogic(self.config)

    @patch('trading_bot.src.api.api_connector.APIConnector')
    def test_execute_trade(self, MockAPIConnector):
        mock_api_connector = MockAPIConnector.return_value
        mock_api_connector.is_connected.return_value = True
        mock_api_connector.place_order.return_value = {'status': 'filled'}

        self.trading_logic.execute_trade('AAPL', 'market', 10)
        mock_api_connector.place_order.assert_called_once_with('AAPL', 'market', 10, None)

    @patch('trading_bot.src.api.api_connector.APIConnector')
    def test_evaluate_trading_opportunity(self, MockAPIConnector):
        mock_api_connector = MockAPIConnector.return_value
        mock_api_connector.get_market_data.return_value = {'price': 150}

        with patch.object(self.trading_logic.technical_analysis, 'evaluate', return_value=0.8):
            with patch.object(self.trading_logic.qualitative_analysis, 'get_qualitative_analysis', return_value=0.6):
                signal = self.trading_logic.evaluate_trading_opportunity('AAPL')
                self.assertEqual(signal, 0.7)

    def test_manage_risk(self):
        self.assertTrue(self.trading_logic.manage_risk('AAPL', 50, 150))
        self.assertFalse(self.trading_logic.manage_risk('AAPL', 150, 150))
        self.assertFalse(self.trading_logic.manage_risk('AAPL', 50, 150))

    def test_calculate_daily_loss(self):
        self.assertEqual(self.trading_logic.calculate_daily_loss(), 0)

    def test_calculate_trade_frequency(self):
        self.assertEqual(self.trading_logic.calculate_trade_frequency('AAPL'), 0)

if __name__ == '__main__':
    unittest.main()
