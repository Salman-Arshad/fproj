# a=['a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d','a','b','c','d']
import  pandas as pd
frame = pd.read_csv("file.csv")
print(frame['ticker'].tolist())