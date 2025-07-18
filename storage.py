import csv
import os
from datetime import datetime

CSV_FILE = "price_history.csv"

def save_price_to_csv(timestamp: int, price: float, symbol: str, interval: str):
    """
    Save a price entry to CSV with timestamp, price, symbol, and interval.
    If file doesn't exist, writes header first.
    """
    file_exists = os.path.isfile(CSV_FILE)
    dt = timestamp.strftime('%Y-%m-%d %H:%M:%S')

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["datetime", "price", "symbol", "interval"])
        writer.writerow([dt, price, symbol, interval])