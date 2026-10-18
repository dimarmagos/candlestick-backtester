import pandas as pd
import yfinance as yf
from patterns import all_patterns,box,win_rate

df = yf.download("AAPL", period="max", multi_level_index=False, interval="1d")
print(yf.Ticker("AAPL").info["longName"])
print("AAPL", "from", df.index[0].date(), "to", df.index[-1].date(), "total", len(df), "candles")
for name, (func, n) in all_patterns.items():
    found = func(df)
    top, bottom = box(df, n)
    total, rate = win_rate(df, found, top, bottom)
    print(name, total, round(rate, 1), "% up")