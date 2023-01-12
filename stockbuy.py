#!/usr/bin/python3

import finviz
from datetime import date

tickers = ['LEG', 'INTC', 'META', 'VZ', 'WBA', 'EMN', 'EPD', 'HPQ', 'INGR', 'JPM', 'MO', 'UGI', 'GSK', 'AVGO', 'HP', 'NTAP', 'OMC','TFC','MMM', 'NSA','MPW','CC','EPD']
fields = ['Price','Target Price', 'P/E', 'Forward P/E', 'P/B', 'PEG', 'P/FCF', 'Dividend %', 'Debt/Eq', 'Payout', 'EPS next 5Y', 'EPS growth next Y', 'Company']

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