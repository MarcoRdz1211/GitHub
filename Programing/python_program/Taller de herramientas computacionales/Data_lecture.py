import numpy as np
import math
import matplotlib.pyplot as plt

data0,data1,data2,data3,data4 = np.loadtxt("data.txt",unpack=True)
n = len(data0)

for i in range(0,10):
    print(data0[i],data1[i],data2[i],data3[i],data4[i])

average0 = sum(data0)/len(data0)
average1 = sum(data1)/len(data1)

plt.scatter(data0,data1,c="blue")
plt.plot(data0,data1,c="blue")
plt.scatter(average0,average1,c="red")

plt.show()
