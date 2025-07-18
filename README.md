# Crypto Tracker 🪙📈

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GUI](https://img.shields.io/badge/built%20with-PyQt5-orange)](https://riverbankcomputing.com/software/pyqt/intro)
[![Binance API](https://img.shields.io/badge/API-Binance-yellow.svg)](https://binance-docs.github.io/apidocs/spot/en/)

**Crypto Tracker** is a lightweight Python desktop app that displays real-time cryptocurrency prices and historical price charts using the Binance API.  
Built with **PyQt5** and **matplotlib**, it supports live updates, interactive symbol/timeframe selection, and clear visual tracking of trends.

---

## 🚀 Features

✅ Select from popular crypto pairs (BTC/USDT, ETH/USDT, etc.)  
✅ Choose timeframes (`1m`, `5m`, `15m`, `1h`, `4h`, `1d`)  
✅ Auto-update every 5 seconds  
✅ Real-time price display  
✅ Dynamic matplotlib chart  
✅ Clean, responsive UI built with PyQt5  
✅ Easy to run and extend

---

## 📦 Requirements

- `PyQt5`
- `matplotlib`
- `requests`

Install all dependencies with:

```bash
pip install -r requirements.txt

▶️ Usage

python main.py

You can also use the Makefile for convenience:

make install
make run

📷 Screenshots

(Add screenshots of the app here if you have them, e.g. with BTC chart and GUI visible)
🛠️ Roadmap
✅ Completed

Basic GUI with PyQt5

Plot BTC/USDT historical data with matplotlib

Symbol selector (BTC, ETH, BNB, etc.)

Timeframe selector (1m, 5m, 1h, etc.)

Auto-update every 5 seconds

Project restructured and modularized

    Initial Makefile with common dev tasks

🧭 In Progress / Planned

Convert to async (with aiohttp + qasync)

Candlestick charts (via mplfinance or plotly)

Add price alerts / notifications

Save historical data to CSV or SQLite

Theme switcher (dark/light mode)

Show last update time

Internationalization (English/Ukrainian)

Unit tests and CI integration

    Build .exe for Windows via PyInstaller

📂 Project Structure

crypto-tracker/
├── main.py            # Main PyQt5 application window
├── logic.py           # Functions for fetching Binance data
├── requirements.txt   # Python dependencies
├── Makefile           # Developer utilities
├── .gitignore
└── README.md

👤 Author

Created by @gorodroz
📄 License

MIT License. See LICENSE for more info.