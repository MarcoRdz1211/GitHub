#Definición de las librerias
import math
import random
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

def V(x,m,w):
    s = (1/2)*m*w**2
 
    return s*x**2

a,n = 10,100
delta = a/n
X_data = []
X_real,Y_real = [],[]

for j in range(0,n):
    X_data.append(j*delta) , X_real.append(j*delta)

m,w,h = 1,3,2.2
q,E = 3.2,1.4
E_t = E+((q*E)**2)/(2*m*w**2)
pi,l = math.pi,(h**2)/(2*m*delta**2)

for j in range(0,n):
    Y_real.append(math.sin(pi*X_real[j]/100)*(2/100)**(1/2))

#--------------------------------
#       auxiliar
#--------------------------------

H = []

for i in range(0,n):
    H.append([])
    for j in range(0,n):
        if (j==i-1) or (j==i+1):
            H[i].append(-l)
        elif (j==i):
#            H[i].append(2+V(X_data[0],m,w)/l)
            H[i].append(2+8/(n+1)**(2))
        else:
            H[i].append(0)    

L_data,Y_data = LA.eig(H)

#print("The eigenvalues are: ")
#for j in range(0,len(L_data)):
#    print("lambda_{}={:.5f}".format(j,L_data[j]))

#print("----------------------------------------")

#print("The eigenvectors are: ")
#for j in range(0,len(Y_data)):
#    print("v_{}={}".format(j,Y_data[j]))

#--------------------------------
#--------------------------------
#--------------------------------        

def inplot(X,Y,j):
    X_axis = np.zeros(len(X))
    Y_axis = np.linspace(-abs(min(Y))*1.1,abs(max(Y))*1.1,len(X))

    rgb = (random.uniform(0,0.5),random.uniform(0,0.5),random.uniform(0,0.5))

    plt.title("Wave function on Harmonic Oscillator")
    plt.plot(X,X_axis,c="black") , plt.plot(X_axis,Y_axis,c="black")
    plt.xlabel("x") , plt.ylabel("psi_{}(x)".format(j))
    plt.plot(X,Y,c=rgb,label="psi_{}(x)".format(j))
    plt.legend()

    plt.grid()
    plt.savefig("Wave function on Harmonic Oscillator")
    plt.show()


#r = int(input("Give the value of the eigenfunction to plot: "))
print(L_data[n-1])
inplot(X_data,Y_data[n-1],n-1)
