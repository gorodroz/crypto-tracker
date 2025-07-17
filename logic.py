import requests
from datetime import datetime

def get_binance_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data["price"])
    except (requests.RequestException, KeyError, ValueError) as e:
        print("Error fetching Binance price:", e)
        return None

def get_binance_kline_data(symbol="BTCUSDT", interval="1h", limit=50):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Кожна свічка має формат:
        # [
        #   0 Open time, 1 Open, 2 High, 3 Low, 4 Close, 5 Volume,
        #   6 Close time, 7 Quote asset volume, 8 Number of trades,
        #   9 Taker buy base asset volume, 10 Taker buy quote asset volume, 11 Ignore
        # ]
        timestamps = [datetime.fromtimestamp(k[0] / 1000.0) for k in data]
        close_prices = [float(k[4]) for k in data]

        return timestamps, close_prices

    except (requests.RequestException, KeyError, ValueError) as e:
        print("Error fetching Binance kline data:", e)
        return [], []
