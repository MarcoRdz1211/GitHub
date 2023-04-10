import matplotlib.pyplot as plt
import numpy as np
import math
import random

def f1(x):
    return 100*np.sin(pi*x/a)

def f2(x):
    return 100*np.sin(pi*x/a)

def g1(x):
    return 100*np.sin(pi*x/a)

def g2(x):
    return 100*np.sin(pi*x/a)

def intf(f,x0,x1,n):
	intf,delta = 0,(x1-x0)/n
	for i in range(0,n):
		intf += f(x0+delta*i)*delta

	return intf

def A(k):
    n = 100
    f = 2*intf(f1,0,a,n)/(a*np.sinh(k*pi*b/a))
    return f

def B(k):
    n = 100
    f = 2*intf(f2,0,a,n)/(a*np.sinh(k*pi*b/a))
    return f

def C(k):
    n = 100
    f = 2*intf(g1,0,a,n)/(b*np.sinh(k*pi*a/b))
    return f

def D(k):
    n = 100
    f = 2*intf(g2,0,a,n)/(b*np.sinh(k*pi*a/b))
    return f

def u(x,y):
    f,n = 0,100
    for k in range(1,n+1):
        r = k*pi/a
        s = k*pi/b
        f += A(k)*np.sin(r*x)*np.sinh(r*(b-y))
        f += B(k)*np.sin(r*x)*np.sinh(r*y)
        f += C(k)*np.sinh(s*(a-x))*np.sin(s*y)
        f += D(k)*np.sinh(s*x)*np.sin(s*y)

    return f

pi = math.pi
a,b,n = 1,1,100
X,Y = np.linspace(0,a,n),np.linspace(0,b,n)
X_data,Y_data = np.meshgrid(X,Y)
U_data = u(X_data,Y_data)
u_0 = u(1/2,1/2)

print("u({},{})={}".format(1/2,1/2,u_0))

fig = plt.figure()

#Grafica: Datos numericos
ax = fig.add_subplot(projection='3d')
ax.set_title("Solution of example 1")
ax.set_xlabel("x") , ax.set_ylabel("y") , ax.set_zlabel("u(x,y)")
ax.scatter(1/2,1/2,u_0,c="red")
ax.plot_surface(X_data,Y_data,U_data,cmap="viridis")

#Guardado de la imagen de ambas graficas.
plt.savefig("MetodosII-example2.png")

plt.show()



