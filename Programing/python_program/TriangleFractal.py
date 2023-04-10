import math
import random
import numpy as np
import matplotlib.pyplot as plt

X = [0,3,6]
Y = [0,3*math.sqrt(3),0]

n = 100000

for i in range(0,n):
    a,b = random.randint(0,len(X)-1),random.randint(0,len(X)-1)
    x_new,y_new = (X[a]+X[b])/2,(Y[a]+Y[b])/2
    X.append(x_new),Y.append(y_new)

plt.title("Fractal-Triangle_{}".format(n))
plt.scatter(X,Y,c="blue")
plt.savefig("Fractal-Triangle_{}".format(n))
plt.show()
