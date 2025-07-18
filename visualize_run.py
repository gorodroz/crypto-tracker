from visualize import load_filtered_data, plot_price

symbol = "BTCUSDT"
interval = "1m"
path = f"filtered/{symbol}_{interval}_filtered.csv"

df = load_filtered_data(path)
plot_price(df, symbol, interval)