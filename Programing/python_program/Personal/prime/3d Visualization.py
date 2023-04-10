import matplotlib.pyplot as plt
import random

X = [[],[],[]]

n = random.randrange(10**2,10**3)

for i in range(0,n+1):
    X[0].append(i)
    X[1].append(i**2)
    X[2].append(i**3)

my_list = [line.split(',') for line in open("Stars_Positions.txt")]
ax = plt.axes(projection="3d")
plt.plot(X[0],X[1],X[2])
plt.show()
