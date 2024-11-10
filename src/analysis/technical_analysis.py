import pandas as pd
import numpy as np

class TechnicalAnalysis:
    def __init__(self, data):
        self.data = data

    def calculate_sma(self, period):
        """
        Calculate Simple Moving Average (SMA).

        :param period: Number of periods for SMA
        :return: SMA values
        """
        sma = self.data['close'].rolling(window=period).mean()
        return sma

    def calculate_ema(self, period):
        """
        Calculate Exponential Moving Average (EMA).

        :param period: Number of periods for EMA
        :return: EMA values
        """
        ema = self.data['close'].ewm(span=period, adjust=False).mean()
        return ema

    def calculate_vwap(self):
        """
        Calculate Volume Weighted Average Price (VWAP).

        :return: VWAP values
        """
        vwap = (self.data['close'] * self.data['volume']).cumsum() / self.data['volume'].cumsum()
        return vwap

    def calculate_rsi(self, period):
        """
        Calculate Relative Strength Index (RSI).

        :param period: Number of periods for RSI
        :return: RSI values
        """
        delta = self.data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_macd(self, fast_period, slow_period, signal_period):
        """
        Calculate Moving Average Convergence Divergence (MACD).

        :param fast_period: Number of periods for fast EMA
        :param slow_period: Number of periods for slow EMA
        :param signal_period: Number of periods for signal line
        :return: MACD line and signal line values
        """
        fast_ema = self.calculate_ema(fast_period)
        slow_ema = self.calculate_ema(slow_period)
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
        return macd_line, signal_line

    def calculate_bollinger_bands(self, period, num_std_dev):
        """
        Calculate Bollinger Bands.

        :param period: Number of periods for SMA
        :param num_std_dev: Number of standard deviations for bands
        :return: Upper band, lower band, and SMA values
        """
        sma = self.calculate_sma(period)
        std_dev = self.data['close'].rolling(window=period).std()
        upper_band = sma + (num_std_dev * std_dev)
        lower_band = sma - (num_std_dev * std_dev)
        return upper_band, lower_band, sma

    def calculate_atr(self, period):
        """
        Calculate Average True Range (ATR).

        :param period: Number of periods for ATR
        :return: ATR values
        """
        high_low = self.data['high'] - self.data['low']
        high_close = np.abs(self.data['high'] - self.data['close'].shift())
        low_close = np.abs(self.data['low'] - self.data['close'].shift())
        true_range = high_low.combine(high_close, max).combine(low_close, max)
        atr = true_range.rolling(window=period).mean()
        return atr

    def calculate_adx(self, period):
        """
        Calculate Average Directional Index (ADX).

        :param period: Number of periods for ADX
        :return: ADX values
        """
        high_diff = self.data['high'].diff()
        low_diff = self.data['low'].diff()
        plus_dm = high_diff.where((high_diff > low_diff) & (high_diff > 0), 0)
        minus_dm = low_diff.where((low_diff > high_diff) & (low_diff > 0), 0)
        tr = self.calculate_atr(period)
        plus_di = 100 * (plus_dm.rolling(window=period).sum() / tr)
        minus_di = 100 * (minus_dm.rolling(window=period).sum() / tr)
        dx = 100 * np.abs((plus_di - minus_di) / (plus_di + minus_di))
        adx = dx.rolling(window=period).mean()
        return adx

    def calculate_cci(self, period):
        """
        Calculate Commodity Channel Index (CCI).

        :param period: Number of periods for CCI
        :return: CCI values
        """
        typical_price = (self.data['high'] + self.data['low'] + self.data['close']) / 3
        sma = typical_price.rolling(window=period).mean()
        mean_deviation = typical_price.rolling(window=period).apply(lambda x: np.mean(np.abs(x - np.mean(x))))
        cci = (typical_price - sma) / (0.015 * mean_deviation)
        return cci
