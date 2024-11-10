import unittest
from unittest.mock import patch, MagicMock
from src.api.ib_connector import IBClient

class TestIBClient(unittest.TestCase):

    @patch('src.api.ib_connector.EClient')
    @patch('src.api.ib_connector.EWrapper')
    def setUp(self, MockEWrapper, MockEClient):
        self.mock_wrapper = MockEWrapper.return_value
        self.mock_client = MockEClient.return_value
        self.config = {
            'api': {
                'tws_endpoint': '127.0.0.1',
                'port': 7497
            }
        }
        self.ib_client = IBClient(self.config)

    def test_init(self):
        self.assertEqual(self.ib_client.host, '127.0.0.1')
        self.assertEqual(self.ib_client.port, 7497)
        self.assertEqual(self.ib_client.client_id, 1)

    def test_error(self):
        with patch('builtins.print') as mock_print:
            self.ib_client.error(1, 2104, 'Test message', None)
            mock_print.assert_called_with('Test message')

            self.ib_client.error(1, 9999, 'Error message', None)
            mock_print.assert_called_with('Error 9999: Error message')

    def test_run(self):
        with patch('src.api.ib_connector.super') as mock_super:
            mock_super().run.side_effect = Exception("Test exception")
            with patch('time.sleep', return_value=None):
                self.ib_client.run()
                mock_super().run.assert_called()

if __name__ == '__main__':
    unittest.main()
