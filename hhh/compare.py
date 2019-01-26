import pandas as pd
import os
from matplotlib import pyplot as plt
a = pd.read_csv("AMZN_2018-06-26.csv")
b = pd.read_csv("current_ticker_info.csv")

print(b.index.values)
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.plot(a.index.values, b.current_price)
ax.plot(13,1680,'bo')
fig.savefig("lol.png")












# import matplotlib.pyplot as plt, mpld3
# plt.plot([3,1,4,1,5], 'ks-', mec='w')
# f= open("index.html",'w')
# mpld3.save_html(fileobj=f)
