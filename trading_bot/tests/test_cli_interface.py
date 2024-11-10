import unittest
from unittest.mock import patch, MagicMock
from trading_bot.src.cli.cli_interface import CLIInterface

class TestCLIInterface(unittest.TestCase):
    @patch('trading_bot.src.cli.cli_interface.TradingLogic')
    @patch('trading_bot.src.cli.cli_interface.argparse.ArgumentParser.parse_args')
    def test_parse_arguments(self, mock_parse_args, mock_trading_logic):
        mock_parse_args.return_value = argparse.Namespace(
            symbol='AAPL', order_type='market', quantity=10, price=None)
        cli = CLIInterface()
        args = cli.parse_arguments()
        self.assertEqual(args.symbol, 'AAPL')
        self.assertEqual(args.order_type, 'market')
        self.assertEqual(args.quantity, 10)
        self.assertIsNone(args.price)

    @patch('trading_bot.src.cli.cli_interface.TradingLogic')
    @patch('trading_bot.src.cli.cli_interface.argparse.ArgumentParser.parse_args')
    def test_run(self, mock_parse_args, mock_trading_logic):
        mock_parse_args.return_value = argparse.Namespace(
            symbol='AAPL', order_type='market', quantity=10, price=None)
        mock_trading_logic_instance = mock_trading_logic.return_value
        mock_trading_logic_instance.api_connector.is_connected.return_value = True
        mock_trading_logic_instance.manage_risk.return_value = True

        cli = CLIInterface()
        cli.run()

        mock_trading_logic_instance.api_connector.connect.assert_not_called()
        mock_trading_logic_instance.manage_risk.assert_called_once_with('AAPL', 10, None)
        mock_trading_logic_instance.execute_trade.assert_called_once_with('AAPL', 'market', 10, None)

if __name__ == '__main__':
    unittest.main()
