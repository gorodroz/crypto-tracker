import pandas as pd
import matplotlib.pyplot as plt


def load_filtered_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["timestamp"])
    df.sort_values("timestamp", inplace=True)
    return df


def plot_price(df: pd.DataFrame, symbol: str, interval: str):
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["price"], marker='o', linestyle='-', color='dodgerblue')

    plt.title(f"{symbol} — Cleaned Price History ({interval})")
    plt.xlabel("Time")
    plt.ylabel("Price (USDT)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()