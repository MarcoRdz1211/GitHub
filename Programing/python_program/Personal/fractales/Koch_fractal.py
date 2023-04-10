import matplotlib.pyplot as plt
import random
import numpy as np
import math
from matplotlib.animation import FuncAnimation

def sqrt(x):
    return math.sqrt(x)

def f1(x0,y0):
    x,y = x0/3,y0/3
    return [x,y]

def f2(x0,y0):
    x = (x0-y0*sqrt(3)+2)/6
    y = (x0*sqrt(3)+y0)/6
    return [x,y]

def f3(x0,y0):
    x = (x0+y0*sqrt(3)+3)/6
    y = (-x0*sqrt(3)+y0+sqrt(3))/6
    return [x,y]

def f4(x0,y0):
    x,y = (x0+2)/3,y0/3
    return [x,y]

X = [[0,0]]

n = int(input("How many cycles do you want? ")) #if n>9; then it's gonna need a big time.
for i in range(0,n):
    print(int(math.log(len(X),5)))
    for j in range(0,len(X)):
        X.append(f1(X[j][0],X[j][1]))
        X.append(f2(X[j][0],X[j][1]))
        X.append(f3(X[j][0],X[j][1]))
        X.append(f4(X[j][0],X[j][1]))

print("----")
posx,posy = [],[]
for i in range(0,len(X)):
    posx.append(X[i][0]) , posy.append(X[i][1])

#for i in range(0,len(X)):
#    print(posx[i],posy[i])

print(len(X))
x_axis=[[0,1.1],[0,0]]
y_axis=[[0,0],[0,0.4]]

plt.scatter(posx,posy,c="Blue",s=0.5)
plt.plot(x_axis[0],x_axis[1],c="Black")
plt.plot(y_axis[0],y_axis[1],c="Black")
plt.xlabel("Re(z)"),plt.ylabel("Im(z)")

plt.savefig("Koch_Fractal.png")

plt.show()
