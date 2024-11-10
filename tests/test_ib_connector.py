import unittest
from unittest.mock import patch, MagicMock
from src.api.ib_connector import IBClient

class TestIBClient(unittest.TestCase):

    @patch('src.api.ib_connector.EClient.connect')
    @patch('src.api.ib_connector.Thread')
    def test_ib_client_initialization(self, mock_thread, mock_connect):
        mock_thread.return_value = MagicMock()
        client = IBClient('127.0.0.1', 7497, 1)
        mock_connect.assert_called_once_with('127.0.0.1', 7497, 1)
        mock_thread.assert_called_once()

    @patch('src.api.ib_connector.EClient.connect')
    @patch('src.api.ib_connector.Thread')
    def test_error_handling(self, mock_thread, mock_connect):
        mock_thread.return_value = MagicMock()
        client = IBClient('127.0.0.1', 7497, 1)
        with patch.object(client, 'error') as mock_error:
            client.error(1, 2104, 'Test message', None)
            mock_error.assert_called_once_with(1, 2104, 'Test message', None)

    @patch('src.api.ib_connector.EClient.connect')
    @patch('src.api.ib_connector.Thread')
    def test_rate_limit_handling(self, mock_thread, mock_connect):
        mock_thread.return_value = MagicMock()
        client = IBClient('127.0.0.1', 7497, 1)
        with patch.object(client, 'error') as mock_error:
            client.error(1, 101, 'Rate limit exceeded', None)
            mock_error.assert_called_once_with(1, 101, 'Rate limit exceeded', None)

if __name__ == '__main__':
    unittest.main()
