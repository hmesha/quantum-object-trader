import unittest
from unittest.mock import patch, MagicMock
from src.trading.trading_logic import TradingLogic
from src.analysis.technical_analysis import TechnicalAnalysis
import pandas as pd
import logging

class TestTradingLogic(unittest.TestCase):

    def setUp(self):
        # Configure test data
        self.config = {
            'trading': {
                'max_position_size': 100,
                'daily_loss_limit': 1000,
                'max_trade_frequency': 10
            }
        }
        
        # Create market data with realistic values
        market_data = pd.DataFrame({
            'close': [150.25, 151.50, 149.75, 152.00, 151.25],
            'high': [151.00, 152.25, 150.50, 152.75, 152.00],
            'low': [149.50, 150.75, 149.00, 151.25, 150.50],
            'volume': [1000000, 1200000, 800000, 1500000, 1100000]
        })
        
        # Initialize components
        self.technical_analysis = TechnicalAnalysis(market_data)
        self.mock_api_connector = MagicMock()
        self.trading_logic = TradingLogic(
            self.config,
            self.technical_analysis,
            self.mock_api_connector
        )

    def test_execute_trade_market_order(self):
        """Test executing a market order"""
        # Setup
        self.mock_api_connector.placeOrder.return_value = {
            'orderId': '12345',
            'status': 'filled'
        }

        # Execute
        self.trading_logic.execute_trade('AAPL', 'market', 10)

        # Verify
        self.mock_api_connector.placeOrder.assert_called_once_with(
            'AAPL', 'market', 10, None
        )

    def test_execute_trade_limit_order(self):
        """Test executing a limit order"""
        # Setup
        self.mock_api_connector.placeOrder.return_value = {
            'orderId': '12345',
            'status': 'pending'
        }

        # Execute
        self.trading_logic.execute_trade('AAPL', 'limit', 10, 150.00)

        # Verify
        self.mock_api_connector.placeOrder.assert_called_once_with(
            'AAPL', 'limit', 10, 150.00
        )

    def test_execute_trade_invalid_quantity(self):
        """Test executing a trade with invalid quantity"""
        # Execute
        self.trading_logic.execute_trade('AAPL', 'market', 0)

        # Verify
        self.mock_api_connector.placeOrder.assert_not_called()

    def test_evaluate_trading_opportunity(self):
        """Test evaluating a trading opportunity"""
        # Setup
        market_data = {
            'price': 150.25,
            'volume': 1000000,
            'high': 151.00,
            'low': 149.50
        }

        with patch.object(self.technical_analysis, 'evaluate', return_value=0.8):
            # Execute
            signal = self.trading_logic.evaluate_trading_opportunity('AAPL', market_data)

            # Verify
            self.assertEqual(signal, 0.4)  # Combined signal should be technical_signal / 2

    def test_evaluate_trading_opportunity_no_data(self):
        """Test evaluating a trading opportunity with no market data"""
        # Execute
        signal = self.trading_logic.evaluate_trading_opportunity('AAPL', None)

        # Verify
        self.assertIsNone(signal)

    def test_manage_risk_within_limits(self):
        """Test risk management within acceptable limits"""
        # Setup
        with patch.object(self.trading_logic, 'calculate_daily_loss', return_value=500), \
             patch.object(self.trading_logic, 'calculate_trade_frequency', return_value=5):
            
            # Execute & Verify
            self.assertTrue(
                self.trading_logic.manage_risk('AAPL', 50, 150.00)
            )

    def test_manage_risk_position_size_exceeded(self):
        """Test risk management with exceeded position size"""
        # Execute & Verify
        self.assertFalse(
            self.trading_logic.manage_risk('AAPL', 150, 150.00)  # Max size is 100
        )

    def test_manage_risk_loss_limit_exceeded(self):
        """Test risk management with exceeded loss limit"""
        # Setup
        with patch.object(self.trading_logic, 'calculate_daily_loss', return_value=1500):
            # Execute & Verify
            self.assertFalse(
                self.trading_logic.manage_risk('AAPL', 50, 150.00)
            )

    def test_manage_risk_frequency_exceeded(self):
        """Test risk management with exceeded trade frequency"""
        # Setup
        with patch.object(self.trading_logic, 'calculate_trade_frequency', return_value=15):
            # Execute & Verify
            self.assertFalse(
                self.trading_logic.manage_risk('AAPL', 50, 150.00)
            )

if __name__ == '__main__':
    unittest.main()
