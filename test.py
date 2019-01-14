import pandas as pd
df = pd.read_csv("file.csv")
#print(df)
lst = df['record_time'].tolist()
#print('[%s]' % ', '.join(map(str, lst)))
print(lst[0])