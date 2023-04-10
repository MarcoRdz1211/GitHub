import matplotlib.pyplot as plt #Libreria que te permite graficar datos.
import math
import random
import numpy as np

X = np.linspace(0,7,100)
Y = np.power(X,2)
Z = np.exp(X)
e = math.exp(1)

#for i in X:
#    Y.append(i**2)

print(X,Y)

plt.title("My first graph")
plt.xlabel("X") , plt.ylabel("Y")

plt.plot(X,Y,c="red",label="y=x^2")
#plt.scatter(X,Y,c="black")

plt.plot(X,Z,c="blue",label="y=e^x") , plt.scatter(X,Z,c="green")

plt.legend()

plt.savefig("Ejemplo1")
plt.show()
