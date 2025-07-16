import requests
import websocket
import json
import threading
import pandas as pd
import logging
import time
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("crypto_tracker.log"),
        logging.StreamHandler()
    ]
)

df = pd.DataFrame(columns=["timestamp", "price"])
df_lock = threading.Lock()

#REST API
def fetch_historical_data():
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": "BTCUSDT",
        "interval": "1h",
        "limit": 24
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        candles = response.json()
        logging.info("Fetched historical price data from Binance")

        with df_lock:
            for candle in candles:
                open_time = datetime.fromtimestamp(candle[0] / 1000)
                close_price = float(candle[4])
                df.loc[len(df)] = [open_time, close_price]
    except requests.RequestException as e:
        logging.error(f"Error fetching historical data: {e}")

#WebSocket
def on_message(ws, message):
    try:
        msg = json.loads(message)
        price = float(msg["p"])
        timestamp = datetime.utcnow()
        logging.info(f"Live price: ${price:.2f}")

        with df_lock:
            df.loc[len(df)] = [timestamp, price]
    except Exception as e:
        logging.error(f"Error processing WebSocket message: {e}")

def on_error(ws, error):
    logging.error(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    logging.warning(f"WebSocket closed: {close_status_code}, {close_msg}")

def on_open(ws):
    logging.info("WebSocket connection opened")
    subscribe_message = {
        "method": "SUBSCRIBE",
        "params": ["btcusdt@trade"],
        "id": 1
    }
    ws.send(json.dumps(subscribe_message))

def run_websocket():
    url = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    ws = websocket.WebSocketApp(
        url,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open
    )
    ws.run_forever()

#Main
if __name__ == "__main__":
    logging.info("Starting Crypto Tracker")

    fetch_historical_data()

    ws_thread = threading.Thread(target=run_websocket, daemon=True)
    ws_thread.start()

    try:
        while True:
            pd.set_option("display.max_rows", 5)
            with df_lock:
                logging.info(f"Current dataset size: {len(df)} rows")
                df.tail(5).to_csv("live_data.csv", index=False)
            time.sleep(30)
    except KeyboardInterrupt:
        logging.warning("Program interrupted by user")
