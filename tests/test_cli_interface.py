import unittest
from unittest.mock import patch, MagicMock, call
from src.cli.dashboard import Dashboard
import pandas as pd

class TestDashboard(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.test_config = {
            'cli': {
                'refresh_interval': 0.1
            },
            'api': {
                'tws_endpoint': 'localhost',
                'port': 7497
            },
            'trading': {
                'max_position_size': 100,
                'daily_loss_limit': 1000,
                'max_trade_frequency': 10
            }
        }

    @patch('src.cli.dashboard.TradingLogic')
    @patch('src.cli.dashboard.TechnicalAnalysis')
    @patch('src.cli.dashboard.IBClient')
    def test_dashboard_initialization(self, MockIBClient, MockTechnicalAnalysis, MockTradingLogic):
        """Test dashboard initialization with mocked dependencies"""
        dashboard = Dashboard(config=self.test_config)
        
        # Verify components were initialized
        MockIBClient.assert_called_once_with(self.test_config)
        MockTechnicalAnalysis.assert_called_once()
        MockTradingLogic.assert_called_once()
        
        # Verify config was properly set
        self.assertEqual(dashboard.refresh_interval, 0.1)
        self.assertFalse(dashboard._running)

    @patch('src.cli.dashboard.TradingLogic')
    @patch('src.cli.dashboard.TechnicalAnalysis')
    @patch('src.cli.dashboard.IBClient')
    def test_display_dashboard(self, MockIBClient, MockTechnicalAnalysis, MockTradingLogic):
        """Test single refresh cycle of dashboard display"""
        dashboard = Dashboard(config=self.test_config)
        
        with patch('builtins.print') as mock_print:
            success = dashboard.display_dashboard()
            
            # Verify display was successful
            self.assertTrue(success)
            
            # Verify essential sections were displayed in order
            expected_calls = [
                call("\nReal-time Trading Dashboard"),
                call("\nPerformance Metrics:"),
                call("-" * 20),
                call("Daily P/L: $0.00"),
                call("Win Rate: 0%"),
                call("\nActive Positions:"),
                call("-" * 20),
                call("No active positions"),
                call("\nAlerts:"),
                call("-" * 20),
                call("No active alerts")
            ]
            
            mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('src.cli.dashboard.TradingLogic')
    @patch('src.cli.dashboard.TechnicalAnalysis')
    @patch('src.cli.dashboard.IBClient')
    def test_run_and_stop(self, MockIBClient, MockTechnicalAnalysis, MockTradingLogic):
        """Test dashboard run loop and stopping mechanism"""
        dashboard = Dashboard(config=self.test_config)
        
        # Mock display_dashboard to run twice then stop
        with patch.object(dashboard, 'display_dashboard', side_effect=[True, True, False]) as mock_display:
            with patch('time.sleep') as mock_sleep:  # Prevent actual sleeping
                dashboard.run()
                
                # Verify dashboard loop ran expected number of times
                self.assertEqual(mock_display.call_count, 3)
                self.assertEqual(mock_sleep.call_count, 2)
                self.assertFalse(dashboard._running)

    @patch('src.cli.dashboard.TradingLogic')
    @patch('src.cli.dashboard.TechnicalAnalysis')
    @patch('src.cli.dashboard.IBClient')
    def test_keyboard_interrupt_handling(self, MockIBClient, MockTechnicalAnalysis, MockTradingLogic):
        """Test dashboard handles keyboard interrupt gracefully"""
        dashboard = Dashboard(config=self.test_config)
        
        # Mock display_dashboard to raise KeyboardInterrupt
        with patch.object(dashboard, 'display_dashboard', side_effect=KeyboardInterrupt):
            with patch('builtins.print') as mock_print:
                dashboard.run()
                
                # Verify proper shutdown
                self.assertFalse(dashboard._running)
                mock_print.assert_called_with("\nDashboard stopped by user")

    @patch('src.cli.dashboard.TradingLogic')
    @patch('src.cli.dashboard.TechnicalAnalysis')
    @patch('src.cli.dashboard.IBClient')
    def test_error_handling(self, MockIBClient, MockTechnicalAnalysis, MockTradingLogic):
        """Test dashboard handles display errors gracefully"""
        dashboard = Dashboard(config=self.test_config)
        
        # Mock display_dashboard to raise an exception
        with patch.object(dashboard, 'display_dashboard', side_effect=Exception("Test error")):
            with patch('builtins.print') as mock_print:
                dashboard.run()
                
                # Verify error was handled
                self.assertFalse(dashboard._running)
                mock_print.assert_called_with("Error displaying dashboard: Test error")

if __name__ == '__main__':
    unittest.main()
