#Importar librerias escenciales para la obtención de datos y sus graficas:
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Determinar los parametros iniciales: n=cantidad de puntos, m=media, a=varianza
n = int(input("Give the number of steps "))
m,a = 0.0,1.0
Delta,DeltaT = 0.001,0.000001

#Definir los arreglos que guardaran los numeros aleatorios (X,Y) y aquellos que guardaran los pasos (X_data,Y_data)
X,Y = np.random.normal(m,a,n),np.random.normal(m,a,n)
X_data,Y_data = [],[]

#Ciclo que suma los valores aletorios anteriores a un valor j, para generar su respectivo siguiente paso
for i in range(0,n):
    x0,y0 = sum(X[:1]),sum(Y[:1])
    X_data.append(sum(X[:i])),Y_data.append(sum(Y[:i]))

#Definición de la función que graficara el histograma de los parametros X
def Xhistogram(X,name):
    plt.figure()
    plt.title("Historiagram of {}_data".format(name))
    plt.xlabel("Number"),plt.ylabel(name)
    plt.hist(X)
    plt.savefig("Historiagram of X_data")

#Definición de la función que graficara el histograma de los parametros Y
def Yhistogram(Y,name):
    plt.figure()
    plt.title("Historiagram of {}_data".format(name))
    plt.xlabel(name),plt.ylabel("Number")
    plt.hist(Y)
    plt.savefig("Historiagram of Y_data")

#Definición de la función que graficara todos los pasos (X,Y)
def TotalFigure(X_data,Y_data):
    plt.figure()
    plt.title("Brownian motion - Random Walk - Total displacement (n={})".format(n))
    plt.xlabel("X"),plt.ylabel("Y")
    plt.plot(X_data,Y_data,c="blue",label="n={}".format(n))
    plt.savefig("Brownian motion - Random Walk - Total displacement")

#Impresión de las primeras 3 gracias: histograma de X, histograma de Y y el total de pasos (X,Y)
Xhistogram(X,"X")

Yhistogram(Y,"Y")

TotalFigure(X_data,Y_data)
plt.show()

#Creación de la grafica (animada) de los Random Walks
fig = plt.figure()
ax = fig.gca()

#Definición de la función que acutaliza los pasos y los grafica
def act(j):
    ax.plot(X_data[:j+1],Y_data[:j+1])
    plt.grid()

    plt.title("Brownian motion - Random Walk (n={})".format(j))
    plt.xlabel("X"),plt.ylabel("Y")    

#Grafica de los Random Walks (animada)
ani = animation.FuncAnimation(fig,act,range(n),interval=10,repeat=False)
plt.savefig("Brownian motion - Random Walk (n={})".format(n))
plt.show()
