#!/usr/bin/python3

import finviz
from datetime import date

tickers = ["IBM","FIS","MAIN","MED","QCOM","FRT","CCI","ADM","CVX","SON","MDU","APD","NNN","NJR","BKH","ES"]
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
    
for ticker in tickers:
    printStock(ticker)