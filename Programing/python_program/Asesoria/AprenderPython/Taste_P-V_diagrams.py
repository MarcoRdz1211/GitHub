import matplotlib.pyplot as plt
import math
import random
import numpy as np

def presion(t,v):
    p = 8*t/(3*v-1)-3/(v**2)

    return p

def polynomial(T,P):
    a,b,c,d = 1,-(8*T+P)/(3*P),3/P,-1/P

    return a,b,c,d

def raices(T,P):
    coeficientes = polynomial(T,P)
    r = np.real(np.roots(coeficientes))
    r.sort()

    return r

def Area(T,P):
    r3,r2,r1 = raices(T,P)

    Area1 = (8/3)*T*math.log((3*r3-1)/(3*r2-1))+3*(1/r3-1/r2)-P*(r3-r2)
    Area2 = P*(r2-r1)-(8/3)*T*math.log((3*r2-1)/(3*r1-1))-3*(1/r2-1/r1)
    dif = Area1-Area2

    return dif

n =  1000
T_data=[0.85,0.9,0.95,1.0,1.05,1.1,1.15,1.2]
Colors=["black","red","blue","green","black","yellow","blue","red","yellow"]

V = np.linspace(0.25,10,n)
P_null = []

for i in range(0,len(T_data)):
    T = T_data[i]
    P = presion(T,V)

    if T<=1:
        V_max,V_min,V_null = np.real(np.roots([4*T,-9,6,-1]))
        P_min,P_max = presion(T,V_min),presion(T,V_max)
        P_interval = np.linspace(P_min,P_max,n)

        difmin = abs(Area(T,P_min))
        P_zero = P_min

        for P_0 in P_interval:

            if abs(Area(T,P_0))<difmin:
                difmin = abs(Area(T,P_0))
                P_zero = P_0

        P_null.append(P_zero)
        print("Diferencia_{}={}".format(P_zero,Area(T,P_zero)))

        V_critical,P_critical = [V_min,V_max],[P_min,P_max]
        plt.scatter(V_critical,P_critical,c="black")
        plt.plot(V,P_zero*np.ones(n),c=Colors[i])

    plt.plot(V,P,c=Colors[i],label="T={}".format(T))
    
plt.title("Isotermas de un Gas Real")
plt.xlabel("V_red") , plt.ylabel("P_red")
plt.xlim(0.4,4),plt.ylim(0,2)

plt.legend()

plt.savefig("IsotermasDeUnGasReal")

plt.show()

#----------------------------------------------------------

for i in range(0,len(P_null)):
    T_0,P_0 = T_data[i],P_null[i]
    r1,r2,r3 = raices(T_0,P_0)

    P_new = [] #P modificada que permanece constante entre las raices v1 y v3

    for v in V:
        if (v<r1 or v>r3):
            P_new.append(presion(T_0,v))

        else:
            P_new.append(P_0)

    V_dots = [r1,r3]
    P_dots = [presion(T_0,r1),presion(T_0,r3)]
    plt.scatter(V_dots,P_dots,c="black")
    plt.plot(V,P_new,c=Colors[i],label="T={}".format(T_0))

plt.title("Isotermas modificado para P={}, y T={}".format(P_0,T_0))
plt.xlabel("V_red") , plt.ylabel("P_red")
plt.xlim(0.4,4),plt.ylim(0,2)

plt.legend()

plt.savefig("IsotermaModificado")

plt.show()
