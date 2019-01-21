
import pandas as pd
import pandas as pd
import os
# for i,j,y in os.walk('.'):
#     print(y)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)
import glob
allFiles = glob.glob(".//data/AMZN_2018-06-10_2018-07-25/*.csv")
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_, axis = 0, ignore_index = True)
print(len(frame))


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
print(ticker)
print(len(ticker))
