import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0,1,0.2)
# y = np.random.rand(len(x))
x=[1,2,3,4,5]
y=[10,20,30,50,60]
boolean= [True, False, False, True, True]
mark = list(np.arange(len(x))[boolean])
mark = [0]
plt.plot(x,y, marker="o", markevery=mark)

plt.show()