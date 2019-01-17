import pandas as pd
import os

a = pd.read_csv("AMZN_2018-06-26.csv")
b = pd.read_csv("current_ticker_info.csv")
print(b.columns.difference(a.columns))


