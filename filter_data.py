import os
import pandas as pd

def filter_and_save_data(input_path: str, output_path: str):
    # Завантаження даних
    df = pd.read_csv(input_path, parse_dates=["timestamp"])

    # Фільтрація
    df.dropna(inplace=True)  # видаляє рядки з NaN
    df.drop_duplicates(inplace=True)  # видаляє дублікати
    df.sort_values("timestamp", inplace=True)  # сортує по часу
    df.reset_index(drop=True, inplace=True)

    # Створення директорії, якщо потрібно
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Збереження
    df.to_csv(output_path, index=False)
    print(f"[✓] Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    symbol = "BTCUSDT"
    interval = "1m"

    input_csv = f"data/{symbol}_{interval}.csv"
    output_csv = f"filtered/{symbol}_{interval}_filtered.csv"

    filter_and_save_data(input_csv, output_csv)
