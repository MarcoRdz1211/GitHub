import math #Libreria que permite realizar operaciones matematicas en elementos.
import numpy as np #Libreria que permite realizar operaciones matematicas en arreglos.
import random #Libreria que genera numeros aleatorios.
import matplotlib #Libreria que te permite graficar datos.
import statistics #Libreria que te permite realizar calculos estadisticos.

#Introducción a math

def dist(A,B):

    return (A[0]-B[0])**2+(A[1]-B[1])**2

e = math.exp(1)
pi = math.pi

print(e)

print(math.degrees(pi))

A = [0.01,0.32,0.45,1.2,9.8] #Convertir de radianes a grados
B = []

for i in A:
    B.append(math.degrees(i))

print(B)

print("--------------------------------")
#Introducción a Numpy

X = np.linspace(0,180,720)
print(X)
print(np.cos(X))

print("--------------------------------")
#Introducción a random
C = range(1,10)

for i in C:
    print(i)

D = random.randrange(1,10)
print(D)

print(random.randint(1,1000))
print(random.choice([1,2,-3,3,4,5,6,7,8,9,10]))
print(random.uniform(1,100))

R = []

for i in range(1,100):
    R.append(random.uniform(-10,10))

print(R)
