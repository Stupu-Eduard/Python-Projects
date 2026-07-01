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
print(price)


market_cap = data['marketCap']
#print(market_cap/1_000_000_000_000)


my_columns = [ 'Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy' ]
final_dataframe = pd.DataFrame(columns = my_columns)

final_dataframe.loc[len(final_dataframe)] = [symbol, price, market_cap,'N/A']

#print(final_dataframe.to_markdown())


final_dataframe = pd.DataFrame(columns = my_columns)
for stock in stocks['Ticker'][:10]:
    #print(stock)

    data = yf.Ticker(stock).info

    price = data.get('currentPrice') or data.get('regularMarketPrice', 0.0)
    m_cap = data.get('marketCap', 0)
    
    final_dataframe.loc[len(final_dataframe)] = [ 
                                                 stock, 
                                                 price, 
                                                 m_cap, 
                                                 'N/A' 
                                                ]
print(final_dataframe.to_markdown())
