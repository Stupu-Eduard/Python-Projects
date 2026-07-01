import numpy as np
import pandas as pd
import yfinance as yf
import xlsxwriter
import math

stocks = pd.read_csv('sp_500_stocks.csv')
#print(stocks);

symbol = 'AAPL'

data = yf.Ticker(symbol).info

#print(data)

price = data['regularMarketPrice']
#print(price)

market_cap = data['marketCap']
print(market_cap/1_000_000_000_000)
