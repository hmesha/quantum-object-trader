import requests
import logging
from textblob import TextBlob

class QualitativeAnalysis:
    def __init__(self, news_api_key, twitter_api_key, twitter_api_secret):
        self.news_api_key = news_api_key
        self.twitter_api_key = twitter_api_key
        self.twitter_api_secret = twitter_api_secret
        self.logger = logging.getLogger(__name__)

    def fetch_news(self, query):
        """
        Fetch news articles from NewsAPI.org.

        :param query: The search query for news articles
        :return: JSON response containing news articles
        """
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={self.news_api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching news: {e}")
            return None

    def fetch_twitter_data(self, query):
        """
        Fetch tweets from Twitter API.

        :param query: The search query for tweets
        :return: JSON response containing tweets
        """
        url = f"https://api.twitter.com/2/tweets/search/recent?query={query}"
        headers = {
            "Authorization": f"Bearer {self.twitter_api_key}"
        }
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching Twitter data: {e}")
            return None

    def analyze_sentiment(self, text):
        """
        Analyze the sentiment of a given text.

        :param text: The text to analyze
        :return: Sentiment polarity score
        """
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def aggregate_sentiment(self, news_data, twitter_data):
        """
        Aggregate sentiment scores from news articles and tweets.

        :param news_data: JSON response containing news articles
        :param twitter_data: JSON response containing tweets
        :return: Average sentiment score
        """
        sentiments = []
        if news_data:
            for article in news_data.get('articles', []):
                sentiment = self.analyze_sentiment(article['title'] + " " + article['description'])
                sentiments.append(sentiment)
        if twitter_data:
            for tweet in twitter_data.get('data', []):
                sentiment = self.analyze_sentiment(tweet['text'])
                sentiments.append(sentiment)
        if sentiments:
            return sum(sentiments) / len(sentiments)
        return 0

    def get_qualitative_analysis(self, query):
        """
        Perform qualitative analysis by fetching and analyzing news and tweets.

        :param query: The search query for news and tweets
        :return: Aggregated sentiment score
        """
        news_data = self.fetch_news(query)
        twitter_data = self.fetch_twitter_data(query)
        sentiment_score = self.aggregate_sentiment(news_data, twitter_data)
        return sentiment_score

    def fetch_sec_filings(self, company_symbol):
        """
        Fetch SEC filings for a given company.

        :param company_symbol: The stock symbol of the company
        :return: JSON response containing SEC filings
        """
        url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={company_symbol}&type=10-K&output=json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching SEC filings: {e}")
            return None

    def analyze_sec_filings(self, sec_filings):
        """
        Analyze the sentiment of SEC filings.

        :param sec_filings: JSON response containing SEC filings
        :return: Sentiment polarity score
        """
        sentiments = []
        for filing in sec_filings.get('filings', []):
            sentiment = self.analyze_sentiment(filing['description'])
            sentiments.append(sentiment)
        if sentiments:
            return sum(sentiments) / len(sentiments)
        return 0

    def get_qualitative_analysis_with_sec(self, query, company_symbol):
        """
        Perform qualitative analysis by fetching and analyzing news, tweets, and SEC filings.

        :param query: The search query for news and tweets
        :param company_symbol: The stock symbol of the company
        :return: Aggregated sentiment score
        """
        news_data = self.fetch_news(query)
        twitter_data = self.fetch_twitter_data(query)
        sec_filings = self.fetch_sec_filings(company_symbol)
        sentiment_score = self.aggregate_sentiment(news_data, twitter_data)
        sec_sentiment_score = self.analyze_sec_filings(sec_filings)
        return (sentiment_score + sec_sentiment_score) / 2
