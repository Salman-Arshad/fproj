import dropbox
from pprint import pprint
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


d = dropbox.Dropbox(
    "Q1mV76AIRhIAAAAAAABG356f2z2RQX_7mgd7OQ92Jbtny8DfoI-XlyZelSEuKf88")


def find_file(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result
# print(d.files_list_folder(path="/csv_bags/AMZN_2018-06-26"))


def downloadTickerData(ticker,fromdate, toDate):
    data = d.files_list_folder(path="/csv_bags")
    names = []
    tkr=[]
    for entry in data.entries:
        if(entry.name.startswith(ticker)):
            tkr.append(entry.name)
    return tkr

