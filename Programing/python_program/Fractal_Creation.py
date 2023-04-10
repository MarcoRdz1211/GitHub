import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import numpy as np
import math
import cmath

def sqrt(x):
    return math.sqrt(x)

def f1(x0,y0,zx,zy):
    x,y = (1+x0*zx-y0*zy),(x0*zy+y0*zx)
    return [x,y]

def f2(x0,y0,zx,zy):
    x,y = (-1-x0*zx+y0*zy),(-x0*zy-y0*zx)
    return [x,y]

def name(zx,zy,j):
    return "LitlewoodFractal".format(zx,zy,j)
    

X = [[0,0]]

option = ""

while (option!="aleatory" and option!="given"):
    option = str(input("Do you want aleatory or given points? (aleatory / given) "))
#fractal with: c=(0.6567076459118035,0.39860333360712996)

if option=="aleatory":
    k = 9 #if n>13. then it's gonna need a big time.
    zx,zy = random.uniform(-1,1),random.uniform(-1,1)

else:
    k = int(input("How many cycles do you want? ")) #if n>9; then it's gonna need a big time.
    z = input("Give c=x+yi (x,y form) ").split(",")
    zx,zy = float(z[0]),float(z[1])

for i in range(0,k):
#    print(i)
    for j in range(0,len(X)):
        x0,y0 = X[j][0],X[j][1]
        X.append(f1(x0,y0,zx,zy))
        X.append(f2(x0,y0,zx,zy))

print("----")
posx,posy = [],[]
n = len(X)
for i in range(0,n):
    posx.append(X[i][0]) , posy.append(X[i][1])

#for i in range(0,n):
#    print(posx[i],posy[i])

print("Total points: {} [10^{}]".format(n,math.log(n,10)))
x_axis=[[1.1*min(posx),1.1*max(posx)],[0,0]]
y_axis=[[0,0],[1.1*min(posy),1.1*max(posy)]]

plt.title("Litlewood fractal with: c={}+{}i".format(zx,zy))
plt.scatter(posx,posy,c="Blue",s=0.5)
plt.plot(x_axis[0],x_axis[1],c="Black")
plt.plot(y_axis[0],y_axis[1],c="Black")
plt.xlabel("Re(z)"),plt.ylabel("Im(z)")

plt.savefig("LitlewoodFractal")

fig = plt.figure()
ax = fig.gca()

def act(j):
    ax.scatter(posx[:j+1],posy[:j+1],s=0.5)
    plt.grid()

    plt.title(name(zx,zy,j)+" (n={})".format(j))
    plt.xlabel("Re(z)"),plt.ylabel("Im(z)")

ani = animation.FuncAnimation(fig,act,range(n),interval=1,repeat=False)
#ani.save("LitlewoodFractal.mp4", fps=10, dpi=80)

plt.show()
