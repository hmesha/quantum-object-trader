from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import threading
import time


class IBClient(EWrapper):
    """Interactive Brokers API Client"""
    
    def __init__(self, config):
        """Initialize the IB client with configuration"""
        # Initialize wrapper
        super().__init__()
        
        # Connection settings
        self.host = config['api']['tws_endpoint']
        self.port = config['api']['port']
        self.client_id = 1
        
        # Initialize connection state
        self.connState = False
        self.connectOptions = ""
        self.optCapab = ""
        self.serverVersion_ = 0
        
        # Threading control
        self._stop_event = threading.Event()
        self._thread = None
        
        # Initialize EClient
        self.client = None
        self._init_client()

    def _init_client(self):
        """Initialize the EClient instance"""
        if self.client is None:
            self.client = EClient(wrapper=self)

    def connect_and_run(self):
        """Establish connection and start message processing thread"""
        try:
            # Ensure client is initialized
            self._init_client()
            
            # Connect using the client
            self.client.connect(self.host, self.port, self.client_id)
            self.connState = True
            
            # Start message processing in a separate thread
            self._thread = threading.Thread(target=self._run_thread)
            self._thread.start()
        except Exception as e:
            print(f"Error in connect_and_run: {e}")
            self.disconnect()

    def _run_thread(self):
        """Thread target for running the client message loop"""
        try:
            if hasattr(self.client, 'run'):
                self.client.run()
        except Exception as e:
            print(f"Error in client thread: {e}")
        finally:
            if self.isConnected():
                self._safe_disconnect()

    def _safe_disconnect(self):
        """Internal method to safely disconnect without thread joining"""
        try:
            self._stop_event.set()
            
            if self.isConnected() and hasattr(self.client, 'disconnect'):
                self.client.disconnect()
                self.connState = False
        except Exception as e:
            print(f"Error in safe disconnect: {e}")

    def disconnect(self):
        """Disconnect from TWS and cleanup resources"""
        try:
            self._safe_disconnect()
            
            # Only attempt to join the thread if we're not in the same thread
            if (self._thread and self._thread.is_alive() and 
                self._thread is not threading.current_thread()):
                self._thread.join(timeout=5)
        except Exception as e:
            print(f"Error in disconnect: {e}")

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson):
        """Handle error messages from TWS"""
        if errorCode == 2104:  # Market data farm connection is OK
            print(errorString)
        else:
            print(f"Error {errorCode}: {errorString}")

    def run(self):
        """Run the client message loop with error handling"""
        try:
            while not self._stop_event.is_set() and self.isConnected():
                if hasattr(self.client, 'run'):
                    self.client.run()
        except Exception as e:
            print(f"Fatal error in client thread: {e}")
        finally:
            if self.isConnected():
                self._safe_disconnect()

    def connectionClosed(self):
        """Handle connection closed event"""
        self.connState = False
        self._safe_disconnect()

    def nextValidId(self, orderId):
        """Handle next valid order ID event"""
        print(f"Connected with client ID: {self.client_id}")

    def isConnected(self):
        """Check if client is connected"""
        return self.connState
