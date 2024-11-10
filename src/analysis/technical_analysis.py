import pandas as pd
import numpy as np


class TechnicalAnalysis:
    def __init__(self, data):
        self.data = data

    def sma(self, period=20):
        """
        Calculate Simple Moving Average (SMA).

        :param period: Number of periods for SMA calculation
        :return: SMA values
        """
        return self.data['close'].rolling(window=period).mean()

    def ema(self, period=20):
        """
        Calculate Exponential Moving Average (EMA).

        :param period: Number of periods for EMA calculation
        :return: EMA values
        """
        return self.data['close'].ewm(span=period, adjust=False).mean()

    def vwap(self, period=14):
        """
        Calculate Volume Weighted Average Price (VWAP).

        :param period: Number of periods for VWAP calculation
        :return: VWAP values
        """
        typical_price = (self.data['high'] + self.data['low'] + self.data['close']) / 3
        return (typical_price * self.data['volume']).rolling(window=period).sum() / self.data['volume'].rolling(window=period).sum()

    def rsi(self, period=14):
        """
        Calculate Relative Strength Index (RSI).

        :param period: Number of periods for RSI calculation
        :return: RSI values
        """
        delta = self.data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def macd(self, fast_period=12, slow_period=26, signal_period=9):
        """
        Calculate Moving Average Convergence Divergence (MACD).

        :param fast_period: Number of periods for fast EMA
        :param slow_period: Number of periods for slow EMA
        :param signal_period: Number of periods for signal line
        :return: MACD line and signal line values
        """
        fast_ema = self.data['close'].ewm(span=fast_period, adjust=False).mean()
        slow_ema = self.data['close'].ewm(span=slow_period, adjust=False).mean()
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
        return macd_line, signal_line

    def bollinger_bands(self, period=20, std_dev=2):
        """
        Calculate Bollinger Bands.

        :param period: Number of periods for SMA calculation
        :param std_dev: Number of standard deviations for the bands
        :return: Upper and lower Bollinger Bands
        """
        sma = self.data['close'].rolling(window=period).mean()
        std = self.data['close'].rolling(window=period).std()
        upper_band = sma + (std_dev * std)
        lower_band = sma - (std_dev * std)
        return upper_band, lower_band

    def atr(self, period=14):
        """
        Calculate Average True Range (ATR).

        :param period: Number of periods for ATR calculation
        :return: ATR values
        """
        high_low = self.data['high'] - self.data['low']
        high_close = np.abs(self.data['high'] - self.data['close'].shift())
        low_close = np.abs(self.data['low'] - self.data['close'].shift())
        true_range = high_low.combine(high_close, max).combine(low_close, max)
        atr = true_range.rolling(window=period).mean()
        return atr

    def adx(self, period=14):
        """
        Calculate Average Directional Index (ADX).

        :param period: Number of periods for ADX calculation
        :return: ADX values
        """
        high_diff = self.data['high'].diff()
        low_diff = self.data['low'].diff()
        plus_dm = high_diff.where((high_diff > low_diff) & (high_diff > 0), 0)
        minus_dm = low_diff.where((low_diff > high_diff) & (low_diff > 0), 0)
        tr = self.atr(period)
        plus_di = 100 * (plus_dm.rolling(window=period).sum() / tr)
        minus_di = 100 * (minus_dm.rolling(window=period).sum() / tr)
        dx = 100 * np.abs((plus_di - minus_di) / (plus_di + minus_di))
        adx = dx.rolling(window=period).mean()
        return adx

    def cci(self, period=20):
        """
        Calculate Commodity Channel Index (CCI).

        :param period: Number of periods for CCI calculation
        :return: CCI values
        """
        typical_price = (self.data['high'] + self.data['low'] + self.data['close']) / 3
        sma = typical_price.rolling(window=period).mean()
        mean_deviation = typical_price.rolling(window=period).apply(lambda x: np.mean(np.abs(x - np.mean(x))))
        cci = (typical_price - sma) / (0.015 * mean_deviation)
        return cci
