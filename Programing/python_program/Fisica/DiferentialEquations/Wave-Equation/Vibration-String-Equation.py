#Definición de librerias para graficar y usar formulas matematicas.
import math
import numpy as np
import matplotlib.pyplot as plt

#Definición de la función que genera el arreglo de ceros.
def zero_function(t,x):
    return 0*np.sin(x)

#Definición de la función tal que: y(x,0)=f(x).
def f(x):
    pi = math.pi
    return np.sin(pi*x/2)

#Definición de la función tal que: y_{t}(x,0)=g(x).
def g(x):
    return 0

#Definición de la función tal que: y(0,t)=h(x).
def h(t):
    return 0

#Definición de la función tal que: y(1,t)=m(x).
def m(t):
    return 0

#Definición de la función que genera la grafica real.
def Yreal(c,t,x):
    pi = math.pi
    return (np.sin(pi*(x+c*t)/2)+np.sin(pi*(x-c*t)/2))/2

#Introducción al problema y codigo.
print("Programa que determina la solución de la ecuación de onda: \n",
      "D_{tt}[y(x,t)]=(c^2)D_{xx}[y(x,t)], sujeta a: \n y(0,t)=y(L,t)=0; \n y(x,0)=sin(pi*x/2); \n y_{t}(x,0)=0 \n con: c=1")

print("El problema físico indica el movimiento ondulatorio de una cuerda")

#Definición de los valores iniciales.
t0,x0 = 0,0
xf = float(input("Dar hasta que valor de x se desea obtener la proyección de la función (de preferenciamayor a 2) "))
tf = 0.5*xf

#Obtención de la cantidad de intervalos y reescritura la naturaleza de los elementos.
n,c0 = int(input("Dar la cantidad de intervalos deseados ")),1

deltat,deltax = abs(tf-t0)/n,abs(xf-x0)/n
c = c0*deltat/deltax

#Definición de los arreglos del tiempo, el desplazamiento y la proyección inicial de Y.
T,X = np.linspace(t0,tf,n+1),np.linspace(x0,xf,n+1)
T_data,X_data = np.meshgrid(T,X)
Y = zero_function(T_data,X_data)
Y_real = Yreal(c0,T_data,X_data)

#Obtención de los valores de Y(x,t) bajo las condiciones iniciales.
Y[0][0] = f(X[0])

for i in range(1,n+1):
    Y[i][0] = f(X[i])
    Y[0][i] = h(T[i])
    Y[n][i] = m(T[i])

#Obtención de los valores de Y(x,t) mediante la primera ecuación del metodo de diferencias finitas.
for i in range(1,n):
    Y[i][1] = Y[i][0]+g(X[i])*deltat-0.5*(c**2)*(Y[i+1][0]-2*Y[i][0]+Y[i-1][0])

#Obtención de los valores de Y(x,t) mediante la segunda ecuación del metodo de diferencias finitas.
for j in range(1,n):
    for i in range(1,n):
        Y[i][j+1] = 2*Y[i][j]-Y[i][j-1]+(c**2)*(Y[i+1][j]-2*Y[i][j]+Y[i-1][j])

#Escritura de los datos en un documento .txt
TextFile = open("Vibration-String-Equation.txt","w+")

a,b,c = "       ","       ",""
for j in range(0,n+1):
    c = "x={},j={} ".format(X[j],j)
    for i in range(0,n+1):
        a += "    t={} ".format(T[i])
        b += "     i= {}  ".format(i)
        c += " {:.2f} ".format(Y[i][j])

    if j==0:
        a += "\n"
        b += "\n"

        TextFile.write(a) , TextFile.write(b)

    c += "\n"
    TextFile.write(c)

#Cierre del documento .txt
TextFile.close()

#Definición de las funciones que generan la grafica en R^3
fig = plt.figure()

#Primera grafica: Datos numericos
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_title("Solution of the Wave Equation of a Vibration String \n by Finite Differentials: \n D_tt{y(x,t)}=D_xx{y(x,t)}")
ax.set_xlabel("t"),ax.set_ylabel("x"),ax.set_zlabel("psi(x,t)")
ax.plot_surface(T_data,X_data,Y,cmap="viridis")

#Segunda grafica: Datos reales.
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_title("Real solution of the Wave Equation of a Vibration String \n by Finite Differentials: \n D_tt{y(x,t)}=D_xx{y(x,t)}")
ax.set_xlabel("t"),ax.set_ylabel("x"),ax.set_zlabel("psi(x,t)")
ax.plot_surface(T_data,X_data,Y_real,cmap="viridis")

#Guardado de la imagen de ambas graficas.
plt.savefig("Vibration-String-Equation.png")

plt.show()
