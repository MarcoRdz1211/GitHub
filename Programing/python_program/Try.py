# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 03:02:45 2022

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#Este programa es respuesta al problema 6.4 


#Tenemos los parámetros:
    
Numpasos= 1000


Deltat= 0.001

delta= 0.00001
#Generamos el vector posición:

pos=np.zeros((Numpasos,2))
# Genero vectores para guardar las normales y generar su histrograma.
X=np.zeros((Numpasos,1))
Y=np.zeros((Numpasos,1))


pos2=np.zeros((Numpasos,2))
X2=np.zeros((Numpasos,1))
Y2=np.zeros((Numpasos,1))

for r in range(1, Numpasos):
    
    
    X[r]=np.random.normal(0, 1)
    Y[r]=np.random.normal(0, 1)
    pos[r,0]= pos[r-1,0]+X[r]*np.sqrt(delta**2 *Deltat)
    pos[r,1]= pos[r-1,1]+Y[r]*np.sqrt(delta**2 *Deltat)
    
    #Ahora para el método de Box Muller:
    a=np.random.uniform(0,1)
    b=np.random.uniform(0,1)
    X2[r]=np.sqrt(-2 *np.log(a)) *np.cos(2* np.pi* b)
    Y2[r]=np.sqrt(-2 *np.log(a)) *np.sin(2* np.pi* b)
    pos2[r,0]= pos2[r-1,0]+X2[r]*np.sqrt(delta**2 *Deltat)
    pos2[r,1]= pos2[r-1,1]+Y2[r]*np.sqrt(delta**2 *Deltat)
    

plt.figure()
plt.title("Histograma X")
plt.hist(X)

plt.figure()
plt.title("Histograma Y")
plt.hist(Y)

plt.figure()    
plt.title("Trayectoria total")
plt.plot(pos[:,0],pos[:,1], marker = "o", linestyle= "--", linewidth = 0.5,
             markersize = 2)    


plt.figure()
plt.title("Histograma X2")
plt.hist(X2)

plt.figure()
plt.title("Histograma Y2")
plt.hist(Y2)

plt.figure()    
plt.title("Trayectoria total utilizando Box Muller")
plt.plot(pos2[:,0],pos2[:,1], marker = "o", linestyle= "--", linewidth = 0.5,
             markersize = 2)    


fig1=plt.figure()
ax = fig1.gca()
def actualizar1(j):
    ax.plot(pos[:j+1,0],pos[:j+1,1])
    plt.xlabel("x",fontsize=13)
    plt.ylabel("y",fontsize=13)
    plt.title('Trayectoria de la partícula Browniana')
    plt.grid(True)
ani = animation.FuncAnimation(fig1, actualizar1, range(Numpasos), interval = 10,
                          repeat = False)
plt.show()
    



""" Para ver la animación de Box Muller, descomentar esta sección 
y comentar la anterior animación.

fig=plt.figure()
ax = fig.gca()
def actualizar(j):
    ax.plot(pos2[:j+1,0],pos2[:j+1,1])
    plt.xlabel("x",fontsize=13)
    plt.ylabel("y",fontsize=13)
    plt.title('Trayectoria de la partícula Browniana con Box Muller')
    plt.grid(True)
ani = animation.FuncAnimation(fig, actualizar, range(Numpasos), interval = 10,
                          repeat = False)
plt.show()  
    
  """
   
