import os
for root,dirs,_ in os.walk('.'):
    for d in dirs:
        print(os.path.join(root,d))