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

def Area(P,T):
    v3,v2,v1 = raices(T,P)
    
    A1 = (8/3)*T*math.log((3*v3-1)/(3*v2-1))+3*(1/v3-1/v2)-P*(v3-v2)
    A2 = P*(v2-v1)-(8/3)*T*math.log((3*v2-1)/(3*v1-1))-3*(1/v2-1/v1)

    return A1-A2

T_data=[0.85,0.9,0.95,1.0,1.05,1.1,1.15,1.2]
Colors=["red","blue","green","black","yellow","blue","red","Magenta"]

V = np.linspace(0.25,4,1000)
P_null = []
V_dots,P_dots = [],[]

for i in range(0,len(T_data)):
    T = T_data[i]
    P = presion(T,V)

    plt.plot(V,P,c=Colors[i],label="T={}".format(T))

    if T<=1:    
        v_max,v_min,v_not = np.real(np.roots([4*T,-9,6,-1]))
        V_critical = [v_min,v_max]
        P_critical = [presion(T,v_min),presion(T,v_max)]

        plt.scatter(V_critical,P_critical,c="black")

        P_interval = np.linspace(P_critical[0],P_critical[1],1009)

        P_inicial = presion(T,v_min)
        r = raices(T,P_inicial)
        difmin = abs(Area(P_inicial,T))
        r_zero = r
        P_zero = P_inicial

        for P_0 in P_interval:

            if abs(Area(P_0,T))<difmin:
                difmin = abs(Area(P_0,T))
                r_zero = r
                P_zero = P_0

        print("La diferencia minima es: dif={}".format(difmin))
        print("Los valores que hacen que I1=I2, son:",
              "P={}, \n T={}, \n v1,v2,v3={},{},{}".format(P_zero,T,r_zero[0],r_zero[1],r_zero[2]))
        print("-----------------------------")

        plt.plot(V,P_zero*np.ones(len(V)),c=Colors[i])

        P_null.append(P_zero)


plt.title("Isotermas de un Gas Real")
plt.xlabel("V_red") , plt.ylabel("P_red")
plt.xlim(0.4,4),plt.ylim(0,2)

plt.legend()

plt.savefig("IsotermasDeUnGasReal")

plt.show()

V1_null,V2_null = [],[]

for i in range(0,len(T_data)):
    T_0 = T_data[i]

    if T_0<1:
        P_new = [] #P modificada que permanece constante entre las raices v1 y v3
        P_0 = P_null[i]
        r = raices(T_0,P_0)
        for v in V:
            if (v<r[0] or v>r[2]):
                P_new.append(presion(T_0,v))

            else:
                P_new.append(P_0)

        plt.plot(V,P_new,c=Colors[i],label="T={}".format(T_0))

        V1_null.append(r[0]),V2_null.append(r[2])
        
    else:
        P = presion(T_0,V)

        plt.plot(V,P,c=Colors[i],label="T={}".format(T))

plt.title("Isotermas modificados")
plt.xlabel("V_red") , plt.ylabel("P_red")
plt.xlim(0.4,4),plt.ylim(0,2)

plt.legend()

plt.savefig("IsotermaModificado")

plt.show()
