# Crypto Tracker 🪙📈

A simple Python application that tracks Bitcoin (BTC) prices in real-time via WebSocket (Binance) and fetches historical data via REST API. Prices are logged to a CSV file and stored in a Pandas DataFrame for further analysis.

## 🔧 Features

- ✅ Fetch historical hourly BTC/USDT prices (Binance REST API)
- ✅ Listen to live BTC/USDT trades (Binance WebSocket)
- ✅ Store and update live data in CSV format
- ✅ Realtime logging to file and console
- ✅ Fully threaded and ready for extension (graphs, alerts, etc.)

## 📦 Dependencies

- `requests`
- `websocket-client`
- `pandas`
- `logging` (built-in)

Install with:

```bash
pip install -r requirements.txt

▶️ Usage

python main.py

Outputs:

    live_data.csv — rolling BTC/USDT price data

    crypto_tracker.log — logging output

🛠️ Roadmap

    📊 Plot live graph (matplotlib / plotly)

    📍 Add CLI options (interval, symbol)

    🧪 Unit tests

    🧬 Makefile + .env support

    💾 Save/restore session data

🧑‍💻 Author

github.com/gorodroz