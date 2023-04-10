import random
import numpy as np
import matplotlib.pyplot as plt

n = 1000

A_null = np.zeros(n)
X_data,Y_data = [],[]
x0,y0 = 0,0

for i in range(0,n):
    x0 += random.randint(-1,1)
    y0 += 1
    X_data.append(x0),Y_data.append(y0)

plt.grid()
plt.title("Normal Distribution")
plt.scatter(X_data,Y_data,c="red") #Puntos
plt.plot(X_data,Y_data,c="blue") #Camino/Recorrido
plt.plot(X_data,A_null,c="black") #Eje x
plt.plot(A_null,Y_data,c="black") #Eje y
plt.xlabel("X"),plt.ylabel("Y")
plt.xlim(1.1*min(X_data),1.1*max(X_data)),plt.ylim(1.1*min(Y_data),1.1*max(Y_data))

plt.show()
