import requests
from datetime import datetime


def get_binance_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return float(data["price"])
    except (requests.RequestException, KeyError, ValueError) as e:
        print("Помилка отримання ціни Binance:", e)
        return None


def get_binance_kline_data(symbol="BTCUSDT", interval="1m", limit=30):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        timestamps = [datetime.fromtimestamp(k[0] / 1000.0) for k in data]
        close_prices = [float(k[4]) for k in data]

        return timestamps, close_prices

    except (requests.RequestException, KeyError, ValueError) as e:
        print("Помилка отримання графіку:", e)
        return [], []
