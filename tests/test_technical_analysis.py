import unittest
import pandas as pd
import numpy as np
from src.analysis.technical_analysis import TechnicalAnalysis

class TestTechnicalAnalysis(unittest.TestCase):

    def setUp(self):
        data = {
            'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'high': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'low': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'volume': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }
        self.data = pd.DataFrame(data)
        self.ta = TechnicalAnalysis(self.data)

    def test_sma(self):
        sma = self.ta.sma(3)
        expected = pd.Series([np.nan, np.nan, 2, 3, 4, 5, 6, 7, 8, 9])
        pd.testing.assert_series_equal(sma, expected)

    def test_ema(self):
        ema = self.ta.ema(3)
        expected = pd.Series([1, 1.5, 2.25, 3.125, 4.0625, 5.03125, 6.015625, 7.0078125, 8.00390625, 9.001953125])
        pd.testing.assert_series_equal(ema, expected)

    def test_vwap(self):
        vwap = self.ta.vwap(3)
        expected = pd.Series([np.nan, np.nan, 2, 3, 4, 5, 6, 7, 8, 9])
        pd.testing.assert_series_equal(vwap, expected)

    def test_rsi(self):
        rsi = self.ta.rsi(3)
        expected = pd.Series([np.nan, np.nan, 100, 100, 100, 100, 100, 100, 100, 100])
        pd.testing.assert_series_equal(rsi, expected)

    def test_macd(self):
        macd_line, signal_line = self.ta.macd(3, 6, 3)
        expected_macd = pd.Series([0, 0.5, 1.25, 2.125, 3.0625, 4.03125, 5.015625, 6.0078125, 7.00390625, 8.001953125])
        expected_signal = pd.Series([0, 0.25, 0.75, 1.4375, 2.25, 3.125, 4.0625, 5.03125, 6.015625, 7.0078125])
        pd.testing.assert_series_equal(macd_line, expected_macd)
        pd.testing.assert_series_equal(signal_line, expected_signal)

    def test_bollinger_bands(self):
        upper_band, lower_band = self.ta.bollinger_bands(3, 2)
        expected_upper = pd.Series([np.nan, np.nan, 4, 5, 6, 7, 8, 9, 10, 11])
        expected_lower = pd.Series([np.nan, np.nan, 0, 1, 2, 3, 4, 5, 6, 7])
        pd.testing.assert_series_equal(upper_band, expected_upper)
        pd.testing.assert_series_equal(lower_band, expected_lower)

    def test_atr(self):
        atr = self.ta.atr(3)
        expected = pd.Series([np.nan, np.nan, 1, 1, 1, 1, 1, 1, 1, 1])
        pd.testing.assert_series_equal(atr, expected)

    def test_adx(self):
        adx = self.ta.adx(3)
        expected = pd.Series([np.nan, np.nan, 0, 0, 0, 0, 0, 0, 0, 0])
        pd.testing.assert_series_equal(adx, expected)

    def test_cci(self):
        cci = self.ta.cci(3)
        expected = pd.Series([np.nan, np.nan, 0, 0, 0, 0, 0, 0, 0, 0])
        pd.testing.assert_series_equal(cci, expected)

if __name__ == '__main__':
    unittest.main()
