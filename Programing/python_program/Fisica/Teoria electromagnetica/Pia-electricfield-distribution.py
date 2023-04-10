import matplotlib.pyplot as plt
import numpy as np
import math
import random

#------- Apartado 1: Datos iniciales. --------#
choose,name = "x","x"
while choose != "a" and choose != "b":
    choose=str(input("¿Que tipo de distribución buscas dar? a) Distribución aleatoria b) distribución proporcionada por mi. "))

while name != "a" and name != "b" and name != "c":
    name=str(input("¿Que distribución quieres dar?: a) Circulo b) poligono, c) puntos "))

pi = math.pi

constant = 8.9875*10**9

delta = 1/10**3

#------- Apartado 2: Generación de la posición de la distribución. --------#

if name == "a":
    r0 = random.uniform(-10,10)
    r = np.arange(0,2*pi,pi*delta)
    posx,posy = r0*np.cos(r),r0*np.sin(r)
    if choose == "a":
        charge0=random.uniform(-10,10)
        print("La carga total de la distribución es: {}".format(charge0))
    elif choose == "b":
        charge0=float(input("Dar el valor de la carga total del anillo "))

    charge=np.ones(len(posx))
    charge=charge*charge0/len(posx)

if name == "b":
    x,y,posx,posy,charge = [],[],[],[],[]
    n=int(input("Dar el numero de lados del poligono "))
    L0=int((10**4)/n)

    if choose =="a":
        for i in range(0,n+1):
            s=2*pi*i/n
            x.append(math.cos(s))
            y.append(math.sin(s))
            
        charge0=random.uniform(-10,10)
    else:
        for i in range(0,n):
            x0,y0 = input("Dar la posición de la particula ",i).split()
            x.append(float(x0))
            y.append(float(y0))

        x.append(x[0])
        y.append(y[0])

        charge0=float(input("Dar el valor de la carga total del anillo "))

    for i in range(0,n):
        x1,y1,x2,y2 = x[i],y[i],x[i+1],y[i+1]
        for j in range(0,int(L0/n)):
            posx.append((x2-x1)*j/int(L0/n)+x1)
            posy.append((y2-y1)*j/int(L0/n)+y1)

    charge=np.ones(len(posx))
    charge=charge*charge0/len(posx)

if name == "c":
    posx,posy,charge = [],[],[]
    k=int(input("Dar el numero de particulas "))
    for i in range (0,k):
        if choose == "a":
            posx.append(random.uniform(-10,10))
            posy.append(random.uniform(-10,10))
            charge.append(random.uniform(-5,5))
        else: 
            x0,y0,charge0 = input("Dar la posición y la carga de la particula ").split()
            posx.append(float(x0))
            posy.append(float(y0))
            charge.append(float(charge0))
    for i in range(0,k):
        print("La posición y la carga de la particula ", i, " es: ", posx[i],posy[i],charge[i])


n=len(posx)


#------- Apartado 3: Modelación del campo electrico. --------#
def E(x,y,n):
    u,v = 0,0
    for i in range(0,n):
        s=constant*charge[i]/((x-posx[i])**2+(y-posy[i])**2)**(3/2)
        u,v = u+s*(x-posx[i]),v+s*(y-posy[i])
    return np.array([u,v])

question = str(input("¿Quieres conocer el campo electrico en algun punto del espacio (si o no)? "))
if question == "si":
    x0,y0 = input("Dar el punto en el espacio ").split()
    x0,y0 = float(x0),float(y0)
    print("E={}".format(E(x0,y0,n)))
else:
    x0,y0 = 0,0

a,b = abs(max(posx))+abs(min(posx))+abs(x0),abs(max(posy))+abs(min(posy))+abs(y0)
a,b = 1.01*a,1.01*b

if name == "b":
    linsx,linsy = np.linspace(-a,a,50),np.linspace(-b,b,50)
else:
    linsx,linsy = np.linspace(-a,a,35),np.linspace(-b,b,35)    

xmesh,ymesh = np.meshgrid(linsx,linsy)

umesh,vmesh = E(xmesh,ymesh,n)
fmesh,gmesh = umesh/((umesh**2+vmesh**2)**(1/2)),vmesh/((umesh**2+vmesh**2)**(1/2))

#------- Apartado 4: Muestra de los campos electricos (real y unitaria). --------#

plt.title("Unitary Electric Field")
plt.xlim(-a,a),plt.ylim(-b,b)
plt.quiver(-a,0,1,0,scale=1),plt.quiver(0,-b,0,1,scale=1)
plt.quiver(xmesh,ymesh,fmesh,gmesh)

if question == "si":
    plt.scatter(x0,y0,c="black")


if name == "c":
    for i in range(0,n):
        if charge[i]>0:
            plt.scatter(posx[i],posy[i],c="red")
        else:
            plt.scatter(posx[i],posy[i],c="blue")
else:
    plt.plot(posx,posy)

plt.title("Real Electric Field")
plt.xlim(-a,a),plt.ylim(-b,b)
plt.quiver(-a,0,1,0,scale=1),plt.quiver(0,-b,0,1,scale=1)
plt.quiver(xmesh,ymesh,umesh,vmesh)

if question == 'si':
    plt.scatter(x0,y0,c='black')

if name == "c":
    for i in range(0,n):
        if charge[i]>0:
            plt.scatter(posx[i],posy[i],c="red")
        else:
            plt.scatter(posx[i],posy[i],c="blue")
else:
    plt.plot(posx,posy)

plt.show()
