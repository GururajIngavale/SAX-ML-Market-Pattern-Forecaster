import yfinance as yf 

ticker = yf.Ticker("^NSEI")

data = ticker.history(start = "2015-01-01" , end = "2025-10-01" , interval = "1d")

data.to_csv("nifty_fifty_OHLCV.csv")

print("done")