import unittest
import threading
import time
from src.api.ib_connector import IBClient

class TestIBClient(unittest.TestCase):
    def setUp(self):
        """Initialize test environment"""
        self.config = {
            'api': {
                'tws_endpoint': '127.0.0.1',
                'port': 7497
            }
        }
        self.ib_client = IBClient(self.config)
        self.connection_timeout = 10  # seconds

    def tearDown(self):
        """Ensure proper cleanup after each test"""
        if hasattr(self, 'ib_client'):
            self.ib_client.disconnect()
            time.sleep(1)  # Give time for cleanup

    def test_init(self):
        """Test initialization without connecting"""
        self.assertEqual(self.ib_client.host, '127.0.0.1')
        self.assertEqual(self.ib_client.port, 7497)
        self.assertEqual(self.ib_client.client_id, 1)
        self.assertFalse(self.ib_client._stop_event.is_set())
        self.assertIsNone(self.ib_client._thread)
        self.assertFalse(self.ib_client.isConnected())

    def test_connection_lifecycle(self):
        """Test the full connection lifecycle with actual TWS/Gateway connection"""
        # Start connection
        self.ib_client.connect_and_run()
        
        # Wait for connection with timeout
        start_time = time.time()
        while not self.ib_client.isConnected() and (time.time() - start_time) < self.connection_timeout:
            time.sleep(0.1)
            
        # Verify connection was established
        self.assertTrue(self.ib_client.isConnected(), "Failed to establish connection within timeout")
        self.assertTrue(self.ib_client._thread.is_alive(), "Client thread should be running")
        
        # Test disconnection
        self.ib_client.disconnect()
        
        # Wait for disconnection with timeout
        start_time = time.time()
        while self.ib_client.isConnected() and (time.time() - start_time) < self.connection_timeout:
            time.sleep(0.1)
            
        # Verify disconnection
        self.assertFalse(self.ib_client.isConnected(), "Failed to disconnect within timeout")
        
        # Verify thread cleanup
        if self.ib_client._thread:
            self.ib_client._thread.join(timeout=5)
            self.assertFalse(self.ib_client._thread.is_alive(), "Client thread should not be running")

    def test_reconnection(self):
        """Test that client can disconnect and reconnect successfully"""
        # First connection
        self.ib_client.connect_and_run()
        
        # Wait for initial connection
        start_time = time.time()
        while not self.ib_client.isConnected() and (time.time() - start_time) < self.connection_timeout:
            time.sleep(0.1)
        
        self.assertTrue(self.ib_client.isConnected(), "Failed to establish first connection")
        
        # Disconnect
        self.ib_client.disconnect()
        time.sleep(1)  # Give time for cleanup
        
        # Reconnect
        self.ib_client.connect_and_run()
        
        # Wait for reconnection
        start_time = time.time()
        while not self.ib_client.isConnected() and (time.time() - start_time) < self.connection_timeout:
            time.sleep(0.1)
        
        self.assertTrue(self.ib_client.isConnected(), "Failed to establish second connection")
        
        # Final cleanup
        self.ib_client.disconnect()

    def test_connection_state_tracking(self):
        """Test that connection state is properly tracked"""
        # Initial state
        self.assertFalse(self.ib_client.isConnected())
        
        # Connect
        self.ib_client.connect_and_run()
        
        # Wait for connection
        start_time = time.time()
        while not self.ib_client.isConnected() and (time.time() - start_time) < self.connection_timeout:
            time.sleep(0.1)
        
        self.assertTrue(self.ib_client.isConnected())
        
        # Disconnect
        self.ib_client.disconnect()
        
        # Wait for disconnection
        start_time = time.time()
        while self.ib_client.isConnected() and (time.time() - start_time) < self.connection_timeout:
            time.sleep(0.1)
        
        self.assertFalse(self.ib_client.isConnected())

if __name__ == '__main__':
    unittest.main()
