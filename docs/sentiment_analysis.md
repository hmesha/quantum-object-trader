# Sentiment Analysis Documentation

## Overview

The sentiment analysis module provides real-time market sentiment analysis by processing news articles and social media data. This document details the implementation, configuration, and usage of the qualitative analysis features.

## Components

### News Analysis

The news analysis component fetches and processes news articles related to specific stocks using the NewsAPI.

#### Configuration
```python
news_api_key = "your_news_api_key"  # Required for NewsAPI access
```

#### Features
- Real-time news fetching
- Article title and description analysis
- Language filtering (English only)
- Sort by publication date

#### Methods
- `fetch_news(symbol)`: Fetches news articles for a given stock symbol
- `analyze_sentiment(text)`: Analyzes sentiment of article text
- Returns sentiment score between -1 (negative) and 1 (positive)

### Social Media Analysis

The social media component analyzes Twitter data for market sentiment using the Twitter API.

#### Configuration
```python
twitter_api_key = "your_twitter_api_key"
twitter_api_secret = "your_twitter_api_secret"
```

#### Features
- Real-time tweet fetching
- Cashtag ($symbol) tracking
- Batch processing of tweets
- Language detection and filtering

#### Methods
- `fetch_twitter_data(symbol)`: Fetches recent tweets for a stock symbol
- `analyze_sentiment(text)`: Analyzes sentiment of tweet text
- Returns sentiment score between -1 (negative) and 1 (positive)

### Sentiment Aggregation

The sentiment aggregation component combines signals from multiple sources to provide a unified sentiment score.

#### Features
- Weighted averaging of news and social media sentiment
- Outlier detection and filtering
- Time-decay weighting (recent data weighted more heavily)

#### Methods
- `aggregate_sentiment(news_data, twitter_data)`: Combines sentiment from multiple sources
- `get_qualitative_analysis(symbol)`: Provides overall sentiment analysis for a symbol
- Returns aggregated sentiment score between -1 (negative) and 1 (positive)

## Usage Example

```python
from src.analysis.qualitative_analysis import QualitativeAnalysis

# Initialize analyzer
analyzer = QualitativeAnalysis(
    news_api_key="your_news_api_key",
    twitter_api_key="your_twitter_api_key",
    twitter_api_secret="your_twitter_api_secret"
)

# Get sentiment for a symbol
sentiment = analyzer.get_qualitative_analysis("AAPL")
print(f"Current market sentiment: {sentiment}")
```

## Error Handling

The module includes comprehensive error handling:
- API rate limit management
- Network error recovery
- Data validation
- Logging of all errors and warnings

## Integration

The sentiment analysis module integrates with the trading system by:
1. Providing real-time sentiment updates
2. Contributing to trading signals
3. Logging sentiment data for analysis
4. Triggering alerts on significant sentiment changes
