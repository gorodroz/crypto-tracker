import os
from visualize import load_filtered_data, plot_price

path = "filtered/BTCUSDT_1m_filtered.csv"

if not os.path.exists(path):
    print(f"File not found: {path}")
    exit()

df = load_filtered_data(path)
plot_price(df)
