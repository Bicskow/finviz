#!/usr/bin/python3

import finviz
from datetime import date

tickers = ['MMM', 'ATO','CSCO', 'EMN', 'HPQ', 'INGR', 'JPM', 'MAN', 'NTAP', 'NKE', 'SNY', 'SWKS', 'UNM', 'VZ', 'WBA', 'PFE', 'O', 'MO', 'SWK', 'TSN', 'LEG', 'USB', 'MAIN','MED','CVX','SON','APD','NNN','BKH','ES']
fields = ['Company','Sector','Industry', 'Price', 'Dividend']

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
    
for ticker in tickers:
    printStock(ticker)