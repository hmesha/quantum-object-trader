from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from threading import Thread
import time
import yaml

class IBClient(EWrapper, EClient):

    def __init__(self, config):
        EClient.__init__(self, self)

        self.config = config
        self.host = self.config['api']['tws_endpoint']
        self.port = self.config['api']['port']
        self.client_id = 1

        self.connect(self.host, self.port, self.client_id)

        thread = Thread(target=self.run)
        thread.start()

    def error(self, req_id, code, msg, misc):
        if code in [2104, 2106, 2158]:
            print(msg)
        else:
            print('Error {}: {}'.format(code, msg))

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

if __name__ == "__main__":
    with open('src/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    client = IBClient(config)
