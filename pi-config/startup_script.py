import json
import time
import requests
import webbrowser
import logging
from datetime import datetime, timedelta
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import socket

# Set up logging
logging.basicConfig(
    filename='pi_display.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RefreshHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/refresh':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            # Verify the refresh token
            if data.get('token') == config.get('refresh_token'):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Refresh triggered')
                logging.info("Manual refresh triggered by server")
                os.system("pkill chromium")
                open_browser(config["server_url"])
            else:
                self.send_response(401)
                self.end_headers()
                self.wfile.write(b'Invalid token')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s" % (self.address_string(), self.log_date_time_string(), format%args))

def load_config():
    try:
        with open('pi_config.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading config: {e}")
        return None

def authenticate_with_server(config):
    try:
        response = requests.post(
            f"{config['server_url']}/api/authenticate",
            json={
                "device_id": config["device_id"],
                "password": config["static_password"]
            }
        )
        return response.status_code == 200
    except Exception as e:
        logging.error(f"Authentication error: {e}")
        return False

def open_browser(url):
    try:
        # Open in fullscreen mode
        os.system(f"chromium-browser --kiosk --incognito {url}")
    except Exception as e:
        logging.error(f"Error opening browser: {e}")

def start_http_server(port=8080):
    server = HTTPServer(('0.0.0.0', port), RefreshHandler)
    logging.info(f"Starting HTTP server on port {port}")
    server.serve_forever()

def main():
    global config
    config = load_config()
    if not config:
        logging.error("Failed to load configuration")
        return

    if not authenticate_with_server(config):
        logging.error("Failed to authenticate with server")
        return

    # Start HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server)
    http_thread.daemon = True
    http_thread.start()

    # Open the website
    open_browser(config["server_url"])

    # Set up refresh timer
    refresh_interval = timedelta(hours=config["refresh_interval_hours"])
    next_refresh = datetime.now() + refresh_interval

    while True:
        if datetime.now() >= next_refresh:
            logging.info("Scheduled refresh triggered")
            os.system("pkill chromium")
            open_browser(config["server_url"])
            next_refresh = datetime.now() + refresh_interval
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main() 