
import pandas as pd
import pandas as pd
import os

import glob
allFiles = glob.glob(".//data/AMZN_2018-07-10_2018-08-30/*.csv")
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_, axis = 0, ignore_index = True)


rosbagTimestamp=frame['rosbagTimestamp'].tolist()
header=frame['header'].tolist()
seq=frame['seq'].tolist()
stamp=frame['stamp'].tolist()
secs=frame['secs'].tolist()
nsecs=frame['nsecs'].tolist()
frame_id=frame['frame_id'].tolist()
ticker=frame['ticker'].tolist()
current_price=frame['current_price'].tolist()
date=frame['date'].tolist()
trade_time=frame['trade_time'].tolist()
record_time=frame['record_time'].tolist()
gain_loss_currency=frame['gain_loss_currency'].tolist()
gain_loss_percent=frame['gain_loss_percent'].tolist()
previous_close=frame['previous_close'].tolist()
open=frame['open'].tolist()
current_bid_price=frame['current_bid_price'].tolist()
current_bid_volume=frame['current_bid_volume'].tolist()
current_ask_price=frame['current_ask_price'].tolist()
current_ask_volume=frame['current_ask_volume'].tolist()
days_range_low=frame['days_range_low'].tolist()
days_range_high=frame['days_range_high'].tolist()
fiftytwo_week_range_low=frame['fiftytwo_week_range_low'].tolist()
fiftytwo_week_range_high=frame['fiftytwo_week_range_high'].tolist()
current_volume=frame['current_volume'].tolist()
avg_volume=frame['avg_volume'].tolist()
market_cap=frame['market_cap'].tolist()
beta=frame['beta'].tolist()
eps=frame['eps'].tolist()
earnings_date=frame['earnings_date'].tolist()
forward_dividend_and_yield_currency=frame['forward_dividend_and_yield_currency'].tolist()
forward_dividend_and_yield_percentage=frame['forward_dividend_and_yield_percentage'].tolist()
ex_dividend_date=frame['ex_dividend_date'].tolist()
one_year_target_est=frame['one_year_target_est'].tolist()
net_assets=frame['net_assets'].tolist()
nav=frame['nav'].tolist()
pe_ratio=frame['pe_ratio'].tolist()
yield_=frame['yield_'].tolist()
ytd_return=frame['ytd_return'].tolist()
beta_3y=frame['beta_3y'].tolist()
expense_ratio_net=frame['expense_ratio_net'].tolist()
inception_date=frame['inception_date'].tolist()
buy=[]
sell=[]



invest = 12
fee = 33
length = len(current_price)
for i in range(0,length):
    if gain_loss_percent[i]>0.12 and current_price[i] >1700:
        sell.append(current_price[i])
print(sell)


length = len(current_price)
for i in range(0,length):
    if gain_loss_percent[i]>1 and current_price[i] >1700:
        buy.append(current_price[i])
print(buy)
from matplotlib import pyplot as plt
import numpy as np
current_price2 = np.array(current_price)
index2 = np.array(frame.index.values)
idsb = np.nonzero(np.in1d(current_price2, buy))[0]
idss = np.nonzero(np.in1d(current_price2, sell))[0]
fig, ax = plt.subplots( nrows=1, ncols=1 )
ax.plot(index2,current_price2)
ax.scatter(frame.index.values[idss],current_price2[idss],color='green')
ax.scatter(frame.index.values[idsb],current_price2[idsb],color='red')
fig.savefig("static/AMZN_2018-07-10_2018-08-30.png")
