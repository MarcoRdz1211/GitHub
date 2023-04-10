import matplotlib.pyplot as plt
import numpy as np
import math
import random

#------- Apartado 1: Datos iniciales. --------#
pi = math.pi

constant = 8.9875*10**9

delta = 1/10**3

#------ Definicion de funciones autosimilares ---#
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

#------- Apartado 2: Generación de la posición de la distribución. --------#
X,charge = [[0,0]],[]

k = int(input("How many cycles do you want? ")) #if n>9; then it's gonna need a big time.
for i in range(0,k):
    print(int(math.log(len(X),5)))
    for j in range(0,len(X)):
        X.append(f1(X[j][0],X[j][1]))
        X.append(f2(X[j][0],X[j][1]))
        X.append(f3(X[j][0],X[j][1]))
        X.append(f4(X[j][0],X[j][1]))

posx,posy = [],[]
for i in range(0,len(X)):   
    posx.append(X[i][0]) , posy.append(X[i][1]) , charge.append(1)

n=len(posx)

print(n)

#------- Apartado 3: Modelación del campo electrico. --------#
def E(x,y,n):
    u,v = 0,0
    for i in range(0,n):
        s=constant*charge[i]/((x-posx[i])**2+(y-posy[i])**2)**(3/2)
        u,v = u+s*(x-posx[i]),v+s*(y-posy[i])
    return np.array([u,v])

#a,b = abs(max(posx))+abs(min(posx))+abs(x0),abs(max(posy))+abs(min(posy))+abs(y0)
minx,maxx = -0.1,1.01
miny,maxy = -0.1,0.5

lins_num = 50
linsx,linsy = np.linspace(minx,maxx,lins_num),np.linspace(miny,maxy,lins_num)

xmesh,ymesh = np.meshgrid(linsx,linsy)

umesh,vmesh = E(xmesh,ymesh,n)
fmesh,gmesh = umesh/((umesh**2+vmesh**2)**(1/2)),vmesh/((umesh**2+vmesh**2)**(1/2))

#------- Apartado 4: Muestra de los campos electricos (real y unitaria). --------#

plt.title("Koch's fractal")
plt.xlim(minx,maxx)
plt.ylim(miny,maxy)
plt.quiver(minx,0,maxx,0,scale=1)
plt.quiver(0,miny,0,maxy,scale=1)
#plt.quiver(xmesh,ymesh,fmesh,gmesh)

for i in range(0,n):
    plt.scatter(posx[i],posy[i],c="blue",s=1)

plt.savefig("Koch_Fragtal.png")

plt.show()
