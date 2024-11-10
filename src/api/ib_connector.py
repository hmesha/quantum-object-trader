from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from threading import Thread
import time

class IBClient(EWrapper, EClient):

    def __init__(self, host, port, client_id):
        EClient.__init__(self, self)

        self.connect(host, port, client_id)

        thread = Thread(target=self.run)
        thread.start()

    def error(self, req_id, code, msg, misc):
        if code in [2104, 2106, 2158]:
            print(msg)
        else:
            print('Error {}: {}'.format(code, msg))

    def connect(self, host, port, client_id):
        try:
            super().connect(host, port, client_id)
        except Exception as e:
            print(f"Failed to connect to TWS API: {e}")

    def run(self):
        while self.isConnected():
            try:
                super().run()
            except Exception as e:
                print(f"Error during API run: {e}")
                time.sleep(1)  # Retry after a short delay

    def monitor_rate_limit(self):
        # Placeholder for rate limit monitoring logic
        pass

client = IBClient('127.0.0.1', 7497, 1)
