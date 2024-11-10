import unittest
from unittest.mock import patch, MagicMock
from src.cli.dashboard import Dashboard

class TestDashboard(unittest.TestCase):
    @patch('src.cli.dashboard.TradingLogic')
    @patch('src.cli.dashboard.config')
    def setUp(self, mock_config, mock_trading_logic):
        self.mock_trading_logic = mock_trading_logic.return_value
        self.mock_config = mock_config
        self.dashboard = Dashboard()

    def test_display_dashboard(self):
        with patch('builtins.print') as mock_print:
            with patch('time.sleep', return_value=None):
                self.dashboard.display_dashboard()
                mock_print.assert_called()

    def test_run(self):
        with patch.object(self.dashboard, 'display_dashboard') as mock_display_dashboard:
            self.dashboard.run()
            mock_display_dashboard.assert_called_once()

if __name__ == '__main__':
    unittest.main()
