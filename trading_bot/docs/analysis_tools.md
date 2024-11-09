# Analysis Tools Documentation

## Technical Analysis Tools

### Simple Moving Average (SMA)
The Simple Moving Average (SMA) is calculated by taking the average of a stock's closing prices over a specified period. The formula for SMA is:
\[ \text{SMA} = \frac{\sum \text{Closing Prices}}{n} \]
where \( n \) is the number of periods.

### Exponential Moving Average (EMA)
The Exponential Moving Average (EMA) gives more weight to recent prices. The formula for EMA is:
\[ \text{EMA} = \text{Price}_{\text{today}} \times \left( \frac{2}{n+1} \right) + \text{EMA}_{\text{yesterday}} \times \left( 1 - \frac{2}{n+1} \right) \]
where \( n \) is the number of periods.

### Volume Weighted Average Price (VWAP)
The Volume Weighted Average Price (VWAP) is calculated by taking the average price of a stock weighted by volume. The formula for VWAP is:
\[ \text{VWAP} = \frac{\sum (\text{Price} \times \text{Volume})}{\sum \text{Volume}} \]

### Relative Strength Index (RSI)
The Relative Strength Index (RSI) measures the speed and change of price movements. The formula for RSI is:
\[ \text{RSI} = 100 - \left( \frac{100}{1 + \text{RS}} \right) \]
where \( \text{RS} \) is the average gain divided by the average loss over a specified period.

### Moving Average Convergence Divergence (MACD)
The Moving Average Convergence Divergence (MACD) is calculated by subtracting the 26-period EMA from the 12-period EMA. The signal line is a 9-period EMA of the MACD line.

### Bollinger Bands
Bollinger Bands consist of a middle band (SMA) and two outer bands (standard deviations above and below the SMA). The formula for Bollinger Bands is:
\[ \text{Upper Band} = \text{SMA} + (k \times \text{Standard Deviation}) \]
\[ \text{Lower Band} = \text{SMA} - (k \times \text{Standard Deviation}) \]
where \( k \) is the number of standard deviations.

### Average True Range (ATR)
The Average True Range (ATR) measures market volatility. The formula for ATR is:
\[ \text{ATR} = \frac{\sum \text{True Range}}{n} \]
where \( \text{True Range} \) is the maximum of the following:
- Current high minus current low
- Absolute value of current high minus previous close
- Absolute value of current low minus previous close

### Average Directional Index (ADX)
The Average Directional Index (ADX) measures the strength of a trend. The formula for ADX is:
\[ \text{ADX} = \frac{\sum \text{DX}}{n} \]
where \( \text{DX} \) is the Directional Movement Index calculated as:
\[ \text{DX} = 100 \times \left| \frac{\text{Plus DI} - \text{Minus DI}}{\text{Plus DI} + \text{Minus DI}} \right| \]
and \( \text{Plus DI} \) and \( \text{Minus DI} \) are the smoothed values of the directional movement indicators.

### Commodity Channel Index (CCI)
The Commodity Channel Index (CCI) measures the deviation of the typical price from its average. The formula for CCI is:
\[ \text{CCI} = \frac{\text{Typical Price} - \text{SMA}}{0.015 \times \text{Mean Deviation}} \]
where \( \text{Typical Price} \) is the average of the high, low, and close prices, and \( \text{Mean Deviation} \) is the average of the absolute differences between the typical price and the SMA.

## Qualitative Analysis Tools

### Google News API
The Google News API is used to fetch news articles related to a specific stock. The sentiment of the articles is analyzed using Natural Language Processing (NLP) techniques.

### Twitter API
The Twitter API is used to fetch tweets related to a specific stock. The sentiment of the tweets is analyzed using NLP techniques.

### Sentiment Analysis
Sentiment analysis is performed using the TextBlob library. The sentiment polarity score ranges from -1 (negative) to 1 (positive).

### Aggregated Sentiment Score
The aggregated sentiment score is calculated by averaging the sentiment scores from news articles and tweets.

## Fundamental Analysis Tools

### Price-to-Earnings (P/E) Ratio
The Price-to-Earnings (P/E) ratio is calculated by dividing the stock price by the earnings per share (EPS). The formula for P/E ratio is:
\[ \text{P/E Ratio} = \frac{\text{Price}}{\text{Earnings Per Share}} \]

### Price-to-Book (P/B) Ratio
The Price-to-Book (P/B) ratio is calculated by dividing the stock price by the book value per share. The formula for P/B ratio is:
\[ \text{P/B Ratio} = \frac{\text{Price}}{\text{Book Value Per Share}} \]

### Debt-to-Equity (D/E) Ratio
The Debt-to-Equity (D/E) ratio is calculated by dividing the total debt by the total equity. The formula for D/E ratio is:
\[ \text{D/E Ratio} = \frac{\text{Total Debt}}{\text{Total Equity}} \]

### Return on Equity (ROE)
The Return on Equity (ROE) is calculated by dividing the net income by the total equity. The formula for ROE is:
\[ \text{ROE} = \frac{\text{Net Income}}{\text{Total Equity}} \]

### Current Ratio
The Current Ratio is calculated by dividing the current assets by the current liabilities. The formula for Current Ratio is:
\[ \text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}} \]

### Quick Ratio
The Quick Ratio is calculated by subtracting the inventory from the current assets and then dividing by the current liabilities. The formula for Quick Ratio is:
\[ \text{Quick Ratio} = \frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}} \]

### Gross Margin
The Gross Margin is calculated by subtracting the cost of goods sold from the revenue and then dividing by the revenue. The formula for Gross Margin is:
\[ \text{Gross Margin} = \frac{\text{Revenue} - \text{Cost of Goods Sold}}{\text{Revenue}} \]

### Operating Margin
The Operating Margin is calculated by dividing the operating income by the revenue. The formula for Operating Margin is:
\[ \text{Operating Margin} = \frac{\text{Operating Income}}{\text{Revenue}} \]

### Net Profit Margin
The Net Profit Margin is calculated by dividing the net income by the revenue. The formula for Net Profit Margin is:
\[ \text{Net Profit Margin} = \frac{\text{Net Income}}{\text{Revenue}} \]

### Earnings Per Share (EPS)
The Earnings Per Share (EPS) is calculated by dividing the net income by the number of shares outstanding. The formula for EPS is:
\[ \text{EPS} = \frac{\text{Net Income}}{\text{Shares Outstanding}} \]
