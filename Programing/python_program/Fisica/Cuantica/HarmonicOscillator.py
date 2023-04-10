#Definición de las librerias
import math
import random
import numpy as np
import matplotlib.pyplot as plt

#Definición de la función que guardara los valores de la función de onda
def f(x,n):
    #Definición de parametros, constantes y coeficientes
    pi = math.pi
    k = 64
    a1 = (k/pi)**(1/4)
    a2 = (fac(n)*2**n)**(1/2)

    #Evaluación de la función psi_n(x)
    psi = (a1/a2)*H(k*x,n)*np.exp(-0.5*np.power(k*x,2))

    return psi

#Definición de la función que guardara los valores de los polinomios de Hermite
def H(x,n):
    g = 0

    #Suma de los monomios en el polinomio de Hermite de grado n
    for m in range(0,n//2+1):
        s = ((-1)**m)*fac(n)/(fac(m)*fac(n-2*m))
        g += s*(2**(n-2*m))*np.power(x,n-2*m)
    
    return g

#Definición del factorial
def fac(n):
    r = 1

    for i in range(2,n+1):
        r = r*i

    return r


#Definición de la función que proyectara los un conjunto de datos y sus valores
#en el polinomio de Hermite de grado n
def inplot_h(n,a):
    #Declaración del conjunto de datos, la evaluación de ellos
    X_data = np.linspace(-a,a,1000)
    Y_data = H(X_data,n)
    #Creación de los ejes coordenados
    X_axis = np.zeros(len(X_data))
    Y_axis = np.linspace(-abs(min(Y_data))*1.1,abs(max(Y_data))*1.1,len(X_data))

    #Generación aleatoria de colores (unicamente estetico)
    rgb = (random.random(),random.random(),random.random())

    #Declaraciones para graficar los datos, y nombramiento de los ejes y la grafica
    plt.title("Hermit's polynomials")
    plt.plot(X_data,X_axis,c="black") , plt.plot(X_axis,Y_axis,c="black")
    plt.xlabel("x") , plt.ylabel("y".format(n))
    plt.plot(X_data,Y_data,c=rgb,label="H_{}".format(n))
    plt.legend()

#Definición de la función que proyectara los un conjunto de datos y sus valores
#en la n-esima función de onda
def inplot_psi(n,a):
    #Declaración del conjunto de datos, la evaluación de ellos
    X_data = np.linspace(-a,a,1000)
    Y_data = f(X_data,n)
    #Creación de los ejes coordenados
    X_axis = np.zeros(len(X_data))
    Y_axis = np.linspace(-abs(min(Y_data))*1.1,abs(max(Y_data))*1.1,len(X_data))

    #Generación aleatoria de colores (unicamente estetico)
    rgb = (random.uniform(0,0.5),random.uniform(0,0.5),random.uniform(0,0.5))

    #Declaraciones para graficar los datos, y nombramiento de los ejes y la grafica
    plt.title("Wave Functions for Harmonic Oscillator")
    plt.plot(X_data,X_axis,c="black") , plt.plot(X_axis,Y_axis,c="black")
    plt.xlabel("x") , plt.ylabel("y".format(n))
    plt.plot(X_data,Y_data,c=rgb,label="Y_{}".format(n))
    plt.legend()

#Atribución de los valores: longitud del conjunto de datos, y limites de los ejes
a,b = 3,20

#Proyección de los polinomios de Hermite de grado 0<=n<6
for i in range(0,6):
    inplot_h(i,a)

#Visualización de datos y guardado de la figura
plt.xlim([-a,a]) , plt.ylim([-b,b])
plt.grid()
plt.savefig("Hermit's polynomials")
plt.show()

plt.clf()

#Atribución de los valores: longitud del conjunto de datos
a = 0.15

#Proyección de las n-esimas funciones de onda asociadas
for i in range(0,4):
    inplot_psi(i,a)

#Visualización de datos y guardado de la figura
plt.xlim([-a,a])
plt.grid()
plt.savefig("WaveFunctionsForQuantumArmonicOscillator")
plt.show()
