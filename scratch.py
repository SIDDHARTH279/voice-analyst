import yfinance as yf

stock = yf.Ticker('TCS.NS')
print(stock.info)