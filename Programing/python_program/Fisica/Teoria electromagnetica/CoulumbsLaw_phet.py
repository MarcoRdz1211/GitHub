import math
import matplotlib.pyplot as plt
import numpy as np

epsilon_0,pi,miu,cm = 8.8541878128*10**(-12),math.pi,10**(-6),10**(-2)
d,q = [10*cm,8*cm,6*cm,4*cm,2*cm,7.5*cm,2.5*cm] , [-5*miu,2*miu]
F = [8.988,14.043,24.965,56.172,224.689,15.978,143.801]

n,k,e_0 = len(d),[],[]

for i in range(0,n):
    k.append(abs(F[i]*(d[i]**2)/(q[0]*q[1])))
    e_0.append(1/(4*pi*k[i]))

average_e_0 = sum(e_0)/len(e_0)
print("The experimental value of the permeability of electricity is: \n e_0={}".format(average_e_0))

def plot_data(A,B):
    A_min,A_max = -abs(min(A))*1.1,abs(max(A))*1.1
    B_min,B_max = -abs(min(B))*1.1,abs(max(B))*1.1

    plt.scatter(A,B)
    plt.plot([A_min,A_max],[0,0],c="black"),plt.plot([0,0],[B_min,B_max],c="black")
    plt.xlim(A_min,A_max),plt.ylim(B_min,B_max)

def f(k,d):
    Y = []
    for i in d:
        Y.append(k/i**2)

    return Y

k,r = abs(q[0]*q[1]/(4*pi*average_e_0)),np.arange(min(d),max(d),10**(-5))
plt.plot(r,f(k,r),c="red")
plt.xlabel("distance (d [cm])"),plt.ylabel("Force (F [N])")
plot_data(d,F),plt.title("Force by distance (d vs F)")
plt.show()

