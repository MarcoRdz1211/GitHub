import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib.animation import FuncAnimation


def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count += 1
            if count > 2:
                break

    if count == 2:
        return 1
    else:
        return 0

def count_primes(n):
    count = 0
    for i in range(0,n+1):
        count += prime(i)

    return count

def animate(i):
    x = np.linspace()

#n=random.randrange(10**2,10**4)
n=int(input("Give the number under to verify the number of primes "))
print(n)

X=[[],[]]


count = 0
for i in range(0,n):
    count += prime(i)
    X[0].append(i)
    X[1].append(count)

x_axis=[[0,n],[0,0]]
y_axis=[[0,0],[0,count_primes(n)]]

plt.plot(X[0],X[1])
plt.plot(x_axis[0],x_axis[1])
plt.plot(y_axis[0],y_axis[1])

plt.text(n,count-count/15,"({},{})".format(n,count))
plt.text(n/4,count,"Prime distribution from 0 to {}".format(n))
plt.xlabel("x"),plt.ylabel("y")

plt.show()
