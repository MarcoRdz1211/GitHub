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

def f1(x0,y0,zx,zy):
    x,y =(1+x0*zx-y0*zy),(x0*zx+y0*zy)
    return [x,y]

def f2(x0,y0,zx,zy):
    x,y =(-1-x0*zx+y0*zy),(-x0*zx-y0*zy)
    return [x,y]

#------- Apartado 2: Generación de la posición de la distribución. --------#
X,charge = [[0,0]],[]

option = ""

while (option!="aleatory" and option!="given"):
    option = str(input("Do you want aleatory or given points? "))

if option=="aleatory":
    k = 10 #if n>13. then it's gonna need a big time.
    zx,zy = random.uniform(-1,1),random.uniform(-1,1)

else:
    k = int(input("How many cycles do you want? ")) #if n>9; then it's gonna need a big time.
    zx,zy = input("Give c=x+yi ").split()
    zx,zy = float(zx),float(zy)

for i in range(0,k):
    print(i)
    for j in range(0,len(X)):
        x0,y0 = X[j][0],X[j][1]
        X.append(f1(x0,y0,zx,zy))
        X.append(f2(x0,y0,zx,zy))

print("----")
posx,posy = [],[]
n = len(X)
for i in range(0,n):
    posx.append(X[i][0]) , posy.append(X[i][1]) , charge.append(1)

#for i in range(0,n):
#    print(posx[i],posy[i])

#------- Apartado 3: Modelación del campo electrico. --------#
def E(x,y,n):
    u,v = 0,0
    for i in range(0,n):
        s=constant*charge[i]/((x-posx[i])**2+(y-posy[i])**2)**(3/2)
        u,v = u+s*(x-posx[i]),v+s*(y-posy[i])
    return np.array([u,v])

#a,b = abs(max(posx))+abs(min(posx))+abs(x0),abs(max(posy))+abs(min(posy))+abs(y0)
minx,maxx = min(posx),max(posx)
miny,maxy = min(posy),max(posy)

lins_num = 50
linsx,linsy = np.linspace(minx,maxx,lins_num),np.linspace(miny,maxy,lins_num)

xmesh,ymesh = np.meshgrid(linsx,linsy)

umesh,vmesh = E(xmesh,ymesh,n)
fmesh,gmesh = umesh/((umesh**2+vmesh**2)**(1/2)),vmesh/((umesh**2+vmesh**2)**(1/2))

#------- Apartado 4: Muestra de los campos electricos (real y unitaria). --------#

plt.title("Litlewood fractal with: c={}+{}i".format(zx,zy))
plt.xlim(minx,maxx)
plt.ylim(miny,maxy)
plt.quiver(minx,0,maxx,0,scale=1)
plt.quiver(0,miny,0,maxy,scale=1)
plt.quiver(xmesh,ymesh,fmesh,gmesh)

print("{}-->10^{}".format(n,math.log(n,10)))

for i in range(0,n):
    plt.scatter(posx[i],posy[i],c="blue",s=2)

plt.savefig("Fractal-Electric_Field.png")

plt.show()
