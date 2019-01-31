import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np


a = pd.read_csv("AMZN_2018-06-26.csv")
b = pd.read_csv("current_ticker_info.csv")
current_price = a['current_price'].tolist()
current_price2 = np.array(current_price)
index2 = np.array(a.index.values)
buy=[]
buy.append(current_price[100])
buy.append(current_price[10])
ids = np.nonzero(np.in1d(current_price2, buy))[0]
# plt.plot(a.index.values,a.current_price)
# plt.scatter(a.index.values[ids],current_price2[ids],color='blue')
# plt.show()

fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
ax.scatter(a.index.values, a.current_price)
fig.savefig("lol.png")
plt.show()
# x =[ 1,2,3,4,5,6,7] # array to be plotte
# y=[100,111,112,111,112,113,114] # array to be plotte

# subArray = [111,114] # array to be highlighted
# plt.plot(x,y)
# plt.show()


# x =np.array([ 1,2,3]) # array to be plotted
# y=np.array([111,111,112]) # array to be plotted

# subArray = [111] 
# ids = np.nonzero(np.in1d(y, subArray))[0]

# plt.plot(x,y)
# plt.scatter(x[ids], y[ids],color='red')
# plt.show()











# import matplotlib.pyplot as plt, mpld3
# plt.plot([3,1,4,1,5], 'ks-', mec='w')
# f= open("index.html",'w')
# mpld3.save_html(fileobj=f)
