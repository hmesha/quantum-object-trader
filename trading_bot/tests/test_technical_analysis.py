import unittest
import pandas as pd
from trading_bot.src.analysis.technical_analysis import TechnicalAnalysis

class TestTechnicalAnalysis(unittest.TestCase):

    def setUp(self):
        data = {
            'close': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'high': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
            'low': [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            'volume': [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
        }
        self.data = pd.DataFrame(data)
        self.ta = TechnicalAnalysis(self.data)

    def test_sma(self):
        sma = self.ta.sma(period=3)
        expected = pd.Series([None, None, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0])
        pd.testing.assert_series_equal(sma, expected, check_names=False)

    def test_ema(self):
        ema = self.ta.ema(period=3)
        expected = pd.Series([10.0, 10.5, 11.25, 12.125, 13.0625, 14.03125, 15.015625, 16.0078125, 17.00390625, 18.001953125, 19.0009765625])
        pd.testing.assert_series_equal(ema, expected, check_names=False)

    def test_vwap(self):
        vwap = self.ta.vwap(period=3)
        expected = pd.Series([None, None, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0])
        pd.testing.assert_series_equal(vwap, expected, check_names=False)

    def test_rsi(self):
        rsi = self.ta.rsi(period=3)
        expected = pd.Series([None, None, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
        pd.testing.assert_series_equal(rsi, expected, check_names=False)

    def test_macd(self):
        macd_line, signal_line = self.ta.macd(fast_period=3, slow_period=6, signal_period=3)
        expected_macd = pd.Series([0.0, 0.25, 0.4375, 0.578125, 0.68359375, 0.7626953125, 0.822021484375, 0.8675166015625, 0.902637451171875, 0.9294780883789062, 0.9496085662841797])
        expected_signal = pd.Series([0.0, 0.125, 0.28125, 0.4296875, 0.561640625, 0.6763671875, 0.7751953125, 0.8601953125, 0.9331953125, 0.9961953125, 1.0501953125])
        pd.testing.assert_series_equal(macd_line, expected_macd, check_names=False)
        pd.testing.assert_series_equal(signal_line, expected_signal, check_names=False)

    def test_bollinger_bands(self):
        upper_band, lower_band = self.ta.bollinger_bands(period=3, std_dev=2)
        expected_upper = pd.Series([None, None, 13.632993161855452, 14.632993161855452, 15.632993161855452, 16.632993161855452, 17.632993161855452, 18.632993161855452, 19.632993161855452, 20.632993161855452, 21.632993161855452])
        expected_lower = pd.Series([None, None, 8.367006838144548, 9.367006838144548, 10.367006838144548, 11.367006838144548, 12.367006838144548, 13.367006838144548, 14.367006838144548, 15.367006838144548, 16.367006838144548])
        pd.testing.assert_series_equal(upper_band, expected_upper, check_names=False)
        pd.testing.assert_series_equal(lower_band, expected_lower, check_names=False)

    def test_atr(self):
        atr = self.ta.atr(period=3)
        expected = pd.Series([None, None, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0])
        pd.testing.assert_series_equal(atr, expected, check_names=False)

    def test_adx(self):
        adx = self.ta.adx(period=3)
        expected = pd.Series([None, None, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        pd.testing.assert_series_equal(adx, expected, check_names=False)

    def test_cci(self):
        cci = self.ta.cci(period=3)
        expected = pd.Series([None, None, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        pd.testing.assert_series_equal(cci, expected, check_names=False)

if __name__ == '__main__':
    unittest.main()
