import dropbox
from pprint import pprint
import os
from datetime import datetime
from termcolor import colored, cprint
import glob
import pandas as pd
from subprocess import Popen, PIPE
import config
import subprocess
d = dropbox.Dropbox(
    "Q1mV76AIRhIAAAAAAABG356f2z2RQX_7mgd7OQ92Jbtny8DfoI-XlyZelSEuKf88")


def find_file(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result
# print(d.files_list_folder(path="/csv_bags/AMZN_2018-06-26"))


def downloadTickerData(ticker, fromDate, toDate):
    fromDate = datetime.strptime(fromDate, "%Y-%m-%d").date()
    toDate = datetime.strptime(toDate, "%Y-%m-%d").date()
    data = d.files_list_folder(path="/csv_bags")
    tkr = []
    final = []

    for entry in data.entries:
        if(entry.name.startswith(ticker)):
            tkr.append(entry.name)
    for item in tkr:
        date = item.split("_", 1)[1]
        date = datetime.strptime(date, "%Y-%m-%d").date()

        print(date-fromDate)
        if date >= fromDate and date <= toDate:
            final.append(item)

    try:
        os.makedirs("data/"+ticker+"_"+str(fromDate)+"_"+str(toDate))
    except FileExistsError:
        pass
    except Exception:
        return False

    for item in final:
        _, res = d.files_download(
            path="/csv_bags/"+item+"/current_ticker_info.csv")
        f = open("data/"+str(ticker)+"_"+str(fromDate) +
                 "_"+str(toDate)+"/"+item+".csv", "wb")
        f.write(res.content)
        f.close()
    return True


def execCode(code,invest,fee, path):
    f = open("data/"+path+"/"+"main.py", 'w')
    # code = code.split("\n")
    # code = code = ''.join(code)
    print(code)

    writeInit(f, path)
    xx = """
invest = {invest}
fee = {fee}
"""
    context={
        "invest":invest,
        "fee":fee
    }
    f.write(xx.format(**context))
    f.write(code)
    graph(f,path)
    path2 = "data/"+path+"/main.py"
    f = open(path2) 
    # print(f.read())
    abc = open("abc.txt","w")
    test = Popen(['python',path2],stdout=PIPE, stderr=PIPE)
    output = test.communicate()[0].decode("utf-8")
    error = test.communicate()[1].decode("utf-8")
    print(error)
    return str(error),str(output)


def writeInit(file, path):
  
    path = "/data/"+path
    print(path)
    data = """
import pandas as pd
import pandas as pd
import os

import glob
allFiles = glob.glob("./{path}/*.csv")
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_, axis = 0, ignore_index = True)

"""
    context = {
        "path": path
    }
    file.write(data.format(**context))
    file.write(config.vars)

def graph(f,path):
    data = """
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
fig.savefig("static/{path}.png")
"""
    context= {
        "path":path
    }
    f.write(data.format(**context))


