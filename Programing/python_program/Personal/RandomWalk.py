import matplotlib.pyplot as plt
import random
import numpy as np
import math

r = random.uniform(0,100)
n = 10000
pi = math.pi
number = 50

for k in range(0,number):
    X,Y = [],[]
    f = []
    
    x0,y0 = random.uniform(0,r),random.uniform(0,r)

    while(x0**2+y0**2 > r**2):
        x0,y0 = random.uniform(0,r),random.uniform(0,r)

    X.append(x0),Y.append(y0)

    while(x0**2+y0**2 < r**2):
        x0,y0 = x0+random.uniform(-10,10),y0+random.uniform(-10,10)
        X.append(x0),Y.append(y0)
        
    plt.scatter(X,Y,c=(0,0,1),s=r/10)
    plt.plot(X,Y,c=(0,k/number,0))

for i in range(0,n):
    f.append(i*2*pi/n)

Fx = r*np.cos(f)
Fy = r*np.sin(f)

plt.title("RandomWalk")
plt.fill(Fx,Fy,c=(1,0,0))
plt.plot(Fx,Fy,c=(1,1,1))

plt.savefig("RandomWalk.png")

plt.show()
