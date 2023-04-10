import matplotlib.pyplot as plt
import random
import numpy as np
import math
from matplotlib.animation import FuncAnimation

def sqrt(x):
    return math.sqrt(x)

def f(x0,y0,cx,cy):
    x,y = (x0)**2-(y0)**2+cx , 2*(x0)*(y0)+cy
    return [x,y]

X = [[0,0]]

n = int(input("How many points do you want? ")) #if n>9; then it's gonna need a big time.
cx,cy = random.uniform(-1,1),random.uniform(-1,1)

for i in range(0,n):
    x0,y0 = X[i][0],X[i][1]
    X.append(f(x0,y0,cx,cy))

print("----")
posx,posy = [],[]
for i in range(0,len(X)):
    posx.append(X[i][0]) , posy.append(X[i][1])

#for i in range(0,len(X)):
#    print(posx[i],posy[i])

print(len(X))
#x_axis=[[0.1*max(posx),1.1*max(posx)],[0,0]]
#y_axis=[[0,0],[0,0.4]]

plt.scatter(posx,posy,c="Blue",s=0.5)
#plt.plot(x_axis[0],x_axis[1],c="Red"),plt.plot(y_axis[0],y_axis[1],c="Black")
plt.xlabel("Re(z)"),plt.ylabel("Im(z)")

#plt.savefig("Mandelbrot_Fragtal.png")

plt.show()
