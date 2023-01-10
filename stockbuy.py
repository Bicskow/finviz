#!/usr/bin/python3

import finviz
from datetime import date

tickers = ['LEG', 'INTC', 'META', 'VZ', 'WBA', 'EMN', 'EPD', 'HPQ', 'INGR', 'JPM', 'MO', 'UGI', 'GSK']
fields = ['Price', 'P/E', 'Forward P/E', 'P/B', 'PEG', 'P/FCF', 'Dividend', 'Target Price', 'Debt/Eq', 'Payout', 'EPS next 5Y', 'EPS next Y']

def printStock(ticker):
    stock = finviz.get_stock(ticker)
    print(f"{ticker}", end="")
    for field in fields:
        print(f"\t{stock[field]}", end="")
    print(f"\t{date.today()}", end="")
    print()


print("Ticker", end="")
for field in fields:
     print(f"\t{field}", end="")
print("\tDate", end="")
print()
    
for ticker in tickers:
    printStock(ticker)