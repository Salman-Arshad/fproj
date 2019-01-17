import dropbox
from pprint import pprint
import os
from datetime import datetime
from termcolor import colored, cprint
import glob
import pandas as pd


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
        if date>=fromDate and date<=toDate: 
            final.append(item)
    os.makedirs("data/"+ticker+"_"+str(fromDate)+"_"+str(toDate))
    for item in final:
        _, res = d.files_download(path="/csv_bags/"+item+"/current_ticker_info.csv")
        f = open("data/"+str(ticker)+"_"+str(fromDate)+"_"+str(toDate)+"/"+item+".csv","wb")
        f.write(res.content)
        f.close()
    path =r'data/' # use your path
    allFiles = glob.glob(path + "/*.csv")

    list_ = []

    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        list_.append(df)

    frame = pd.concat(list_, axis = 0, ignore_index = True)
    return frame['secs'].tolist()
