# Technical Analysis Documentation

## Overview

This document provides a comprehensive guide to the technical analysis tools implemented in the trading bot. It covers the workings, mathematical formulas, and configuration guidelines for each tool.

## Technical Analysis Tools

### 1. Simple Moving Average (SMA)

**Description**: The Simple Moving Average (SMA) is a widely used technical indicator that calculates the average of a selected range of prices, usually closing prices, by the number of periods in that range.

**Formula**:
\[ \text{SMA} = \frac{\sum \text{Price}}{n} \]
where \( n \) is the number of periods.

**Configuration**:
- `period`: Number of periods for SMA calculation (default: 20).

### 2. Exponential Moving Average (EMA)

**Description**: The Exponential Moving Average (EMA) is a type of moving average that places a greater weight and significance on the most recent data points.

**Formula**:
\[ \text{EMA} = \text{Price}_{\text{today}} \times \left( \frac{2}{n+1} \right) + \text{EMA}_{\text{yesterday}} \times \left( 1 - \frac{2}{n+1} \right) \]
where \( n \) is the number of periods.

**Configuration**:
- `period`: Number of periods for EMA calculation (default: 20).

### 3. Volume Weighted Average Price (VWAP)

**Description**: The Volume Weighted Average Price (VWAP) is a trading benchmark that gives the average price a security has traded at throughout the day, based on both volume and price.

**Formula**:
\[ \text{VWAP} = \frac{\sum (\text{Typical Price} \times \text{Volume})}{\sum \text{Volume}} \]

**Configuration**:
- `period`: Number of periods for VWAP calculation (default: 14).

### 4. Relative Strength Index (RSI)

**Description**: The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements.

**Formula**:
\[ \text{RSI} = 100 - \frac{100}{1 + \frac{\text{Average Gain}}{\text{Average Loss}}} \]

**Configuration**:
- `period`: Number of periods for RSI calculation (default: 14).

### 5. Moving Average Convergence Divergence (MACD)

**Description**: The Moving Average Convergence Divergence (MACD) is a trend-following momentum indicator that shows the relationship between two moving averages of a security's price.

**Formula**:
\[ \text{MACD Line} = \text{EMA}_{\text{fast}} - \text{EMA}_{\text{slow}} \]
\[ \text{Signal Line} = \text{EMA of MACD Line} \]

**Configuration**:
- `fast_period`: Number of periods for fast EMA (default: 12).
- `slow_period`: Number of periods for slow EMA (default: 26).
- `signal_period`: Number of periods for signal line (default: 9).

### 6. Bollinger Bands

**Description**: Bollinger Bands are a volatility indicator that consists of a middle band (SMA) and two outer bands (standard deviations above and below the SMA).

**Formula**:
\[ \text{Upper Band} = \text{SMA} + (k \times \text{Standard Deviation}) \]
\[ \text{Lower Band} = \text{SMA} - (k \times \text{Standard Deviation}) \]

**Configuration**:
- `period`: Number of periods for SMA (default: 20).
- `std_dev`: Number of standard deviations for bands (default: 2).

### 7. Average True Range (ATR)

**Description**: The Average True Range (ATR) is a volatility indicator that measures the degree of price movement for a given period.

**Formula**:
\[ \text{ATR} = \text{Average}(\text{True Range}) \]
where True Range is the greatest of:
- Current high minus the current low
- Absolute value of the current high minus the previous close
- Absolute value of the current low minus the previous close

**Configuration**:
- `period`: Number of periods for ATR calculation (default: 14).

### 8. Average Directional Index (ADX)

**Description**: The Average Directional Index (ADX) is a trend indicator that quantifies the strength of a trend.

**Formula**:
\[ \text{ADX} = \text{Average}(\text{DX}) \]
where DX is calculated as:
\[ \text{DX} = 100 \times \frac{|\text{DI+} - \text{DI-}|}{\text{DI+} + \text{DI-}} \]

**Configuration**:
- `period`: Number of periods for ADX calculation (default: 14).

### 9. Commodity Channel Index (CCI)

**Description**: The Commodity Channel Index (CCI) is a momentum-based oscillator that measures the deviation of the price from its average price.

**Formula**:
\[ \text{CCI} = \frac{\text{Typical Price} - \text{SMA}}{0.015 \times \text{Mean Deviation}} \]
where Typical Price is calculated as:
\[ \text{Typical Price} = \frac{\text{High} + \text{Low} + \text{Close}}{3} \]

**Configuration**:
- `period`: Number of periods for CCI calculation (default: 20).

## Sentiment Analysis

The trading bot also includes sentiment analysis capabilities through the QualitativeAnalysis class. This analyzes market sentiment using:

1. News Articles Analysis
   - Fetches recent news articles about the stock
   - Analyzes sentiment of article titles and descriptions
   - Uses TextBlob for natural language processing

2. Social Media Analysis
   - Fetches recent tweets about the stock
   - Analyzes sentiment of tweet content
   - Aggregates social media sentiment

The sentiment analysis returns a score between -1 (extremely negative) and 1 (extremely positive), which can be used alongside technical indicators for trading decisions.

## Conclusion

This document provides an overview of the technical and sentiment analysis tools implemented in the trading bot. Each tool's description, mathematical formula, and configuration guidelines are provided to help users understand and utilize these tools effectively.
