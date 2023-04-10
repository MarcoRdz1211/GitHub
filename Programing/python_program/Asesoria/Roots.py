import math
import random
import numpy as np
import matplotlib.pyplot as plt

def p(v,t):
    f = v**3-(8*t+p)*(v**2)/(3*p)+(3*v)/p-1/p

def roots(t,p):
    p = [1,-(8*t+p)/(3*p),3/p,-1/p]
    x = np.roots(p)

    return x

a,b = 0.5,4
c,d = 0,2
V_data = np.linspace(a,b,100)
T_data = [0.8,0.9,1.0,1.1,1.2]
P_data = []

for t in T_data:
    P_data.append(p(t,V_data))

plt.title("P-V Diagram")
plt.plot(V_data,np.zeros(len(V_data)),c="black")

for data in P_data:
    plt.plot(V_data,data,c="blue")

plt.xlabel("V_R"),plt.ylabel("P_R")
plt.xlim([a,b])
plt.ylim([c,d])
plt.grid()
plt.show()
