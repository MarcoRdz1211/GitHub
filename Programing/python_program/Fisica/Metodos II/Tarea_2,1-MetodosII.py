import matplotlib.pyplot as plt
import numpy as np
import math
import random

def u(x,y,n):
    f = 0
    for k in range(0,n):
        r = (2*k+1)*pi
        f += (np.sin(r*x)*np.sinh(r*y))/(r*np.sinh(r))

    return 400*f

pi = math.pi
a,b,n = 1,1,100
X,Y = np.linspace(0,a,n),np.linspace(0,b,n)
X_data,Y_data = np.meshgrid(X,Y)
U_data = u(X_data,Y_data,n)
u_0 = u(1/2,1/2,n)

print("u({},{})={}".format(1/2,1/2,u_0))

fig = plt.figure()

#Grafica: Datos numericos
ax = fig.add_subplot(projection='3d')
ax.set_title("Solution of example 1")
ax.set_xlabel("x") , ax.set_ylabel("y") , ax.set_zlabel("u(x,y)")
ax.scatter(1/2,1/2,u_0,c="red")
ax.plot_surface(X_data,Y_data,U_data,cmap="viridis")

#Guardado de la imagen de ambas graficas.
plt.savefig("MetodosII-example1.png")

plt.show()

