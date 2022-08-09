import math
import warnings
import numpy as np
import pandas as pd
import datetime as dt
import pandas_datareader as web
warnings.filterwarnings("ignore")


stocks = []
with open("SmallStockList.txt") as f:
    for line in f:
        stocks.append(line.strip())

web.DataReader(stocks, 'yahoo', start='1/1/2010', end='1/1/2016')['Adj Close'].to_csv("Prices.csv")
web.DataReader(stocks, 'yahoo', start='1/1/2010', end='1/1/2016')['Volume'].to_csv("Volumes.csv")