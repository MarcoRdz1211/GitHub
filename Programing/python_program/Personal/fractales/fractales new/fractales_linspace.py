import matplotlib.pyplot as plt
import random
import numpy as np
import math
import cmath
from matplotlib.animation import FuncAnimation

def sqrt(x):
    return math.sqrt(x)

def f1(x0,y0,zx,zy):
    x,y =(1+x0*zx-y0*zy),(x0*zx+y0*zy)
    return [x,y]

def f2(x0,y0,zx,zy):
    x,y =(-1-x0*zx+y0*zy),(-x0*zx-y0*zy)
    return [x,y]

#------------------------------Plots------------------------------#
    
#x_dots,y_dots = np.linspace(-4,4,10000,endpoint=True),np.linspace(-4,4,10000,endpoint=True)
limx,limy = [-3,3],[-3,3]
x_dots,y_dots = np.arange(limx[0],limx[1],0.1),np.arange(limy[0],limy[1],0.1)

x,y = np.meshgrid(x_dots,y_dots)

#------------------------------Plots------------------------------#

x_plots,y_plots = [],[]

print(len(x),len(x[0]))

for i in range(0,len(x)):
    for j in range(0,len(x[0])):
        X = [[0,0]]
        option = ""
        zx,zy = float(x[i][j]),float(y[i][j])

        print(i+j,"\n")
        for k in range(0,8):
            print(k)
            for l in range(0,len(X)):
                x0,y0 = X[l][0],X[l][1]
                if (f1(x0,y0,zx,zy)==0 or f2(x0,y0,zx,zy)==0):
                    x_plots.append(zx),y_plots.append(zy)
                    print("one")
                    input()
                    break
                else:
                    X.append(f1(x0,y0,zx,zy))
                    X.append(f2(x0,y0,zx,zy))
        print("------")

        posx,posy = [],[]
        n = len(X)
        for k in range(0,n):
            posx.append(X[k][0]) , posy.append(X[k][1])

        x_axis=[[1.1*min(posx),1.1*max(posx)],[0,0]]
        y_axis=[[0,0],[1.1*min(posy),1.1*max(posy)]]

        plt.title("Litlewood fractal with: c={}+{}i".format(zx,zy))
        plt.scatter(posx,posy,c="Blue",s=0.5)
        plt.plot(x_axis[0],x_axis[1],c="Black")
        plt.plot(y_axis[0],y_axis[1],c="Black")
        plt.xlabel("Re(z)"),plt.ylabel("Im(z)")
        
minx,maxx = min(limx),max(limx)
miny,maxy = min(limy),max(limy)

plt.scatter(x_plots,y_plots,s=1)
plt.quiver(-3,0,1,0,scale=1.05)
plt.quiver(0,-3,0,1,scale=1.40)

plt.show()
