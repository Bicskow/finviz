#!/usr/bin/python3

import finviz
from datetime import date

tickers = ['MMM', 'ATO','CSCO', 'EMN', 'HPQ', 'INGR', 'JPM', 'MAN', 'NTAP', 'NKE', 'SNY', 'SWKS', 'UNM', 'VZ', 'WBA', 'PFE', 'O', 'MO', 'SWK', 'TSN', 'LEG', 'USB', 'MAIN','MED','CVX','SON','APD','NNN','BKH','ES','CMI']
fields = ['Price','Target Price', 'P/E', 'Forward P/E', 'P/B', 'PEG', 'P/FCF', 'Dividend %', 'Debt/Eq', 'Payout', 'EPS next 5Y', 'EPS growth next Y', 'Company','Sector','Industry']

def printStock(ticker):
    stock = finviz.get_stock(ticker)
    print(f"{ticker}", end="")
    for field in fields:
        print(f";{stock[field]}", end="")
    print(f";{date.today()}", end="")
    print()


print("Ticker", end="")
for field in fields:
     print(f";{field}", end="")
print(";Date", end="")
print()

tickers.sort()    
for ticker in tickers:
    printStock(ticker)