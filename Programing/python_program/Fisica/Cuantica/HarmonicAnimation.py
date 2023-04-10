import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def fac(n):
    return np.math.factorial(n)

def H(x,n):
    g = 0

    #Suma de los monomios en el polinomio de Hermite de grado n
    for m in range(0,n//2+1):
        s = ((-1)**m)*fac(n)/(fac(m)*fac(n-2*m))
        g += s*(2**(n-2*m))*np.power(x,n-2*m)
    
    return g

def inplot_h(X,Y,n0,a):
    #Creación de los ejes coordenados
    X_axis = np.zeros(len(X))
    Y_axis = np.linspace(-abs(min(Y))*1.1,abs(max(Y))*1.1,len(X))

    rgb = (random.random(),random.random(),random.random())

    #Declaraciones para graficar los datos, y nombramiento de los ejes y la grafica
    plt.title("Harmonics")
    plt.plot(X,X_axis,c="black") , plt.plot(X_axis,Y_axis,c="black")
    plt.plot(X,Y,c=rgb,label="H_{}".format(n0))
    plt.xlabel("x") , plt.ylabel("y")
    plt.legend()

#n = int(input("Give the Hermite-Polynomial "))
n = 10
a = 10
N = 200
m,w,h,pi = 1,1,1,math.pi
k = np.sqrt(m*w/h)
X = np.linspace(-a,a,N)
Hermite = []

for n0 in range(0,n+1):
    Hermite.append(np.sqrt(np.pi)*k*H(k*X,n0)*np.exp(-k*np.power(X,2)/2))

plt.figure()
for n0 in range(0,n+1):
    inplot_h(X,Hermite[n0],n0,a)

plt.savefig("Harmonics unitl {}".format(n))
plt.show()

fig = plt.figure()
ax = fig.gca()

X_axis = np.zeros(len(X))
Y_axis = np.linspace(-abs(min(Hermite[0]))*1.1,abs(max(Hermite[0]))*1.1,len(X))
plt.title("Harmonic - {}".format(n))
plt.xlabel("X"),plt.ylabel("Y")
plt.plot(X,X_axis,c="black") , plt.plot(X_axis,Y_axis,c="black")

def act(j):
    for n0 in range(0,n+1):
        ax.plot(X[:j+1],Hermite[n0][:j+1])

    plt.grid()

ani = animation.FuncAnimation(fig,act,range(N),interval=1,repeat=False)
ani.save('Harmonic_{}.mp4'.format(n), fps=10, dpi=80)
plt.show()
