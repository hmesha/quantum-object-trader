import unittest
import pandas as pd
import numpy as np
from src.analysis.technical_analysis import TechnicalAnalysis


class TestTechnicalAnalysis(unittest.TestCase):

    def setUp(self):
        # More realistic price data with some volatility
        data = {
            'close': [10, 10.5, 10.2, 10.8, 10.3, 10.6, 10.4, 10.9, 10.7, 10.5],
            'high':  [10.2, 10.8, 10.4, 11.0, 10.5, 10.8, 10.6, 11.1, 10.9, 10.7],
            'low':   [9.8, 10.3, 10.0, 10.6, 10.1, 10.4, 10.2, 10.7, 10.5, 10.3],
            'volume': [1000, 1500, 800, 2000, 900, 1300, 1100, 1800, 1400, 1200]
        }
        self.data = pd.DataFrame(data)
        self.ta = TechnicalAnalysis(self.data)

    def test_sma(self):
        sma = self.ta.sma(3)
        # First two values will be NaN, then 3-period moving average
        expected = pd.Series([np.nan, np.nan, 10.23333, 10.50000, 10.43333, 
                            10.56667, 10.43333, 10.63333, 10.66667, 10.70000], 
                           dtype=float)
        pd.testing.assert_series_equal(sma.round(5), expected.round(5))

    def test_ema(self):
        ema = self.ta.ema(3)
        # EMA gives more weight to recent prices
        expected = pd.Series([10.00000, 10.25000, 10.22500, 10.51250, 10.40625,
                            10.50313, 10.45156, 10.67578, 10.68789, 10.59395],
                           dtype=float)
        pd.testing.assert_series_equal(ema.round(5), expected.round(5))

    def test_vwap(self):
        vwap = self.ta.vwap(3)
        # VWAP considers volume in the calculation
        expected = pd.Series([np.nan, np.nan, 10.31667, 10.55000, 10.37778,
                            10.57778, 10.41111, 10.73889, 10.68333, 10.55000],
                           dtype=float)
        pd.testing.assert_series_equal(vwap.round(5), expected.round(5))

    def test_rsi(self):
        rsi = self.ta.rsi(3)
        # RSI should reflect overbought/oversold conditions
        expected = pd.Series([np.nan, np.nan, 40.00000, 71.42857, 35.71429,
                            64.28571, 42.85714, 78.57143, 57.14286, 42.85714],
                           dtype=float)
        pd.testing.assert_series_equal(rsi.round(5), expected.round(5))

    def test_macd(self):
        macd_line, signal_line = self.ta.macd(3, 6, 3)
        # MACD shows momentum and trend changes
        expected_macd = pd.Series([0.00000, 0.25000, 0.13750, 0.32188, 0.16094,
                                 0.20547, 0.12773, 0.29887, 0.27443, 0.15722],
                                dtype=float)
        expected_signal = pd.Series([0.00000, 0.12500, 0.13125, 0.22656, 0.19375,
                                   0.19961, 0.16367, 0.23127, 0.25285, 0.20503],
                                  dtype=float)
        pd.testing.assert_series_equal(macd_line.round(5), expected_macd.round(5))
        pd.testing.assert_series_equal(signal_line.round(5), expected_signal.round(5))

    def test_bollinger_bands(self):
        upper_band, lower_band = self.ta.bollinger_bands(3, 2)
        # Bands should expand with volatility
        expected_upper = pd.Series([np.nan, np.nan, 10.81650, 11.06650, 11.01650,
                                  11.06650, 10.93650, 11.13650, 11.16650, 11.16650],
                                 dtype=float)
        expected_lower = pd.Series([np.nan, np.nan, 9.65017, 9.93350, 9.85017,
                                  10.06683, 9.93017, 10.13017, 10.16683, 10.23350],
                                 dtype=float)
        pd.testing.assert_series_equal(upper_band.round(5), expected_upper.round(5))
        pd.testing.assert_series_equal(lower_band.round(5), expected_lower.round(5))

    def test_atr(self):
        atr = self.ta.atr(3)
        # ATR measures volatility
        expected = pd.Series([np.nan, np.nan, 0.40000, 0.43333, 0.40000,
                            0.40000, 0.36667, 0.43333, 0.40000, 0.36667],
                           dtype=float)
        pd.testing.assert_series_equal(atr.round(5), expected.round(5))

    def test_adx(self):
        adx = self.ta.adx(3)
        # ADX measures trend strength
        expected = pd.Series([np.nan, np.nan, np.nan, 20.00000, 25.71429,
                            28.57143, 25.71429, 31.42857, 34.28571, 31.42857],
                           dtype=float)
        pd.testing.assert_series_equal(adx.round(5), expected.round(5))

    def test_cci(self):
        cci = self.ta.cci(3)
        # CCI measures price deviation from average
        expected = pd.Series([np.nan, np.nan, -66.66667, 100.00000, -100.00000,
                            66.66667, -66.66667, 133.33333, 33.33333, -66.66667],
                           dtype=float)
        pd.testing.assert_series_equal(cci.round(5), expected.round(5))


if __name__ == '__main__':
    unittest.main()
