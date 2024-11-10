import unittest
from unittest.mock import patch, MagicMock
from src.analysis.qualitative_analysis import QualitativeAnalysis

class TestQualitativeAnalysis(unittest.TestCase):

    @patch('src.analysis.qualitative_analysis.requests.get')
    def test_fetch_news(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'articles': []}
        mock_get.return_value = mock_response

        qa = QualitativeAnalysis('fake_news_api_key', 'fake_twitter_api_key', 'fake_twitter_api_secret')
        result = qa.fetch_news('AAPL')
        self.assertEqual(result, {'articles': []})

    @patch('src.analysis.qualitative_analysis.requests.get')
    def test_fetch_twitter_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'data': []}
        mock_get.return_value = mock_response

        qa = QualitativeAnalysis('fake_news_api_key', 'fake_twitter_api_key', 'fake_twitter_api_secret')
        result = qa.fetch_twitter_data('AAPL')
        self.assertEqual(result, {'data': []})

    def test_analyze_sentiment(self):
        qa = QualitativeAnalysis('fake_news_api_key', 'fake_twitter_api_key', 'fake_twitter_api_secret')
        sentiment = qa.analyze_sentiment('I love this stock!')
        self.assertGreater(sentiment, 0)

    def test_aggregate_sentiment(self):
        qa = QualitativeAnalysis('fake_news_api_key', 'fake_twitter_api_key', 'fake_twitter_api_secret')
        news_data = {'articles': [{'title': 'Great news', 'description': 'Stock is up!'}]}
        twitter_data = {'data': [{'text': 'I love this stock!'}]}
        sentiment_score = qa.aggregate_sentiment(news_data, twitter_data)
        self.assertGreater(sentiment_score, 0)

    @patch('src.analysis.qualitative_analysis.QualitativeAnalysis.fetch_news')
    @patch('src.analysis.qualitative_analysis.QualitativeAnalysis.fetch_twitter_data')
    def test_get_qualitative_analysis(self, mock_fetch_twitter_data, mock_fetch_news):
        mock_fetch_news.return_value = {'articles': [{'title': 'Great news', 'description': 'Stock is up!'}]}
        mock_fetch_twitter_data.return_value = {'data': [{'text': 'I love this stock!'}]}

        qa = QualitativeAnalysis('fake_news_api_key', 'fake_twitter_api_key', 'fake_twitter_api_secret')
        sentiment_score = qa.get_qualitative_analysis('AAPL')
        self.assertGreater(sentiment_score, 0)

if __name__ == '__main__':
    unittest.main()
