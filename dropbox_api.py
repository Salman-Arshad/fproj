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

d = dropbox.Dropbox("Q1mV76AIRhIAAAAAAABG356f2z2RQX_7mgd7OQ92Jbtny8DfoI-XlyZelSEuKf88")
def find_file(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result
#print(d.files_list_folder(path="/csv_bags/AMZN_2018-06-26"))


def downloadTickerData(fileName):
    print("/csv_bags/"+fileName+"/current_ticker_info.csv")
    try:
        md, res = d.files_download(path="/csv_bags/"+fileName+"/current_ticker_info.csv")
    except:
        return False   
    f = open(fileName+"-current_ticker_info.csv",'wb')
    f.write(res.content)
    f.close()
    return True