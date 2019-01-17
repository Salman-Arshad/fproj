# import pandas as pd
# df = pd.read_csv("file.csv")
# #print(df)
# lst = df['record_time'].tolist()
# #print('[%s]' % ', '.join(map(str, lst)))
# print(lst[0])











import glob
import pandas as pd
import os
path =r'hhh/' # use your path
allFiles = glob.glob(path + "/*.csv")

list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)

frame = pd.concat(list_, axis = 0, ignore_index = True)
for item in list(frame):
    print(item)
f = pd.read_csv("file.csv")
d = f['seq'].tolist()
print(d[0])

















# import subprocess
# out = open("out.txt", "wb")
# err = open("err.txt", "wb")
# test = subprocess.Popen(["pwd"], stdout=out, stderr=err,shell=True)
# output = test.communicate()[0]
# out.close()
# err.close()
# out = open("out.txt", "r")
# print(out.read())
