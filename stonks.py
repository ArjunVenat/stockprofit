import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from yahoo_fin import stock_info as si
import json
import requests


stonks = []
tickers = []
prices = []
profit = []



print("How many stocks have you invested in?")
n = int(input())
if (n == 0):
    print("Understandable, have a nice day")

def getStonks():
    for i in range (n):
        invested = input()
        stonks.append(invested)

def getTicker():
    headers = {'Content-Type': 'application/json'}
    for i in range (n):
        requestResponse = requests.get("https://api.tiingo.com/tiingo/utilities/search?query="+stonks[i]+"&token=74a7b32409c6cb4f4b265ceea0c1319dcc4b76dd", headers=headers)
        stockdata = requestResponse.json()
        stockticker = stockdata[0]['ticker']
        tickers.append(stockticker)


def currentPrice():
    getStonks()
    getTicker()
    for i in range(n):
        prices.append(round(si.get_live_price(tickers[i]), 2))
    print("\n")
    for i in range(n):
        print(tickers[i] + ": " + str(prices[i]))
        shares = int(input("How many shares of " + stonks[i] + " did you purchase: "))
        oldprice = int(input("How much did each share cost: "))
        profit.append(round(int(shares) * (prices[i] - oldprice), 2))
        print("Your profit for " + stonks[i] + "/" + tickers[i] + " is: " + str(profit[i]))
        print('\n')

def totalProfit():
    finalStocksProfit = 0.00
    for i in range (n):
        finalStocksProfit = round(finalStocksProfit + profit[i], 2)
    print("Your Total Profit is: " + str(finalStocksProfit))



currentPrice()
totalProfit()
