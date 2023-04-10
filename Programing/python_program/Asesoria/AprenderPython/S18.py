#---------------------------Librerias a usar----------------------------------------------

import matplotlib.pyplot as plt  #Libreria que permite graficar
import math  #Libreria que permite realizar calculos matematicos de variables
import random  #Libreria que permite obtener elementos aleatorios [No usada]
import numpy as np  #Libreria que permite realizar operacones matematicas con arreglos

#---------------------------Definición de funciones a usar----------------------------------------------

#Definición de la función que toma un valor de v, determina la presión para un isoterma t: P=8t/(3v-1)-3/v^2
def presion(t,v):
    p = 8*t/(3*v-1)-3/(v**2)

    return p

#Definición de la función que determina las raices del polinomio en v: v^3-(8t+p)v^2/(3p)+3v/p-1/p=0
def raices(T_0,P_0):
    coeficientes = [1,-(8*T_0+P_0)/(3*P_0),3/P_0,-1/P_0]  #Definición de un arreglo que tendra los coeficientes del polinomio: ax^3+bx^2+cx+d=0->Coeficientes=[a,b,c,d]
    r = np.real(np.roots(coeficientes))  #Obtención de las raices del polinomio mediante: np.roots, y filtrado de las raices en su forma real mediante: np.real
    r.sort()  #Ordenamiento de las raices: r1<=r2<=r3

    return r    

#Definicion de la funcion que dada una presión, determina el area encerrada entre las curvas para un isoterma t
def area(T_0,P_0):
    r = raices(T_0,P_0)  #Se determinan los puntos de intersección entre las curvas: v1<=v2<=v3

    Area1 = (8/3)*(T_0)*math.log((3*r[2]-1)/(3*r[1]-1))+3*(1/r[2]-1/r[1])-(P_0)*(r[2]-r[1])  #Determinar el area comprendida entre las regiones: v2<=v<=v3
    Area2 = (P_0)*(r[1]-r[0])-(8/3)*(T_0)*math.log((3*r[1]-1)/(3*r[0]-1))-3*(1/r[1]-1/r[0])  #Determinar el area comprendida entre las regiones: v1<=v<=v2
    dif = Area1-Area2  #Restas de las areas. 

    return dif

#---------------------------Datos generales----------------------------------------------

T_data=[0.85,0.9,0.95,1.0,1.05,1.1,1.15,1.2]  #Lista de los isotermas
Colors=["red","blue","green","black","yellow","blue","red","yellow"]  #Lista de colores para cada isoterma

V = np.linspace(0.25,10,1000)  #Creación de un arreglo semi-continuo de 1000 elementos comprendidos en el intervalo: [0.25,10]

P_null = []  #Lista que guardará los valores de P, tales que para un isoterma T, las areas comprendidas son iguales

#---------------------------Grafica de isotermas----------------------------------------------

#Sección que determina los valores de P, tales que para un isoterma T, las areas comprendidas son iguales; y ademas crea las graficas de los isotermas
for i in range(0,len(T_data)):
    T = T_data[i]  #Valor de T para el isoterma
    P = presion(T,V)  #Creación del arreglo: P(T,v), para todo v en V

    #Si el isoterma es tal que T<=1, entonces tiene puntos minimos y maximos locales
    #En esta sección se determinan los valores de P, tales que para un isoterma T<=1, las areas comprendidas son iguales
    if T<=1:
        V_max,V_min,V_nothing = np.real(np.roots([4*T,-9,6,-1]))  #Obtención de los valores criticos de la función P
        P_max,P_min = presion(T,V_max),presion(T,V_min)  #Obtención de los puntos criticos de la función P

        difmin = abs(area(T,P_min))  #Definición de un primer valor de la diferencia minima. Se buscara que esta sea 0 durante el siguiente ciclo.
        P_zero = P_min  #Definición de una primera aproximación del valor de presión que hara que las areas sean iguales (difmin=0)

        P_interval = np.linspace(P_min,P_max,1000)  #Creación del intervalo semi-continuo: [P_min,P_max], con 1000 elementos 

        #Inicio del ciclo que determina el valor de P tal que la diferencia sea la mas cercana al 0 de todos los puntos en el intervalo [P_min,P_max]
        for P_0 in P_interval:
            dif = abs(area(T,P_0))  #Obtención del area del isoterma T, con presión P_0 (P_0 esta en el intervalo: [P_min,P_max])
            
            #Si la diferencia anteriormente calculada es menor a la ''considera'' como diferencia minima, entonces realmente esta nueva diferencia es la diferencia minima
            if dif<difmin:
                difmin = dif  #Modificación del valor de diferencia minima
                P_zero = P_0  #Modificación del valor de P, tal que hace la diferencia minima. Cuando acabe este programa, este valor guardara el valor de P tal que su diferencia es minima para todo P

        #Mostrar al usuario cual es el valor de P tal que genera la diferencia minima, para un isoterma T
        print("-La diferencia minima para el area del isoterma: T={}, es: {}, con: P={}".format(T,difmin,P_zero))

        #Ingresar dicho valor de P, en el arreglo P_null
        P_null.append(P_zero)

    #Graficar los puntos maximos y minimos de un isoterma.
    V_dots = [V_min,V_max]  #Arreglo que guarda los valores criticos de la función P para un isoterma T
    P_dots = [P_min,P_max]  #Arreglo que guarda los puntos criticos de la función P para un isoterma T
    plt.scatter(V_dots,P_dots,c="black")  #Grafica de los puntos V_dots vs P_dots

    #Grafica de la recta P=P_0, con P_0 la recta que dividide a la curva P en dos regiones con areas iguales
    P_line = P_zero*np.ones(1000)  #Creación de un arreglo con 1000 elementos iguales (Esto crea la recta)
    plt.plot(V,P_line,c=Colors[i],linestyle='--')  #Grafica de la recta: P=P_0, vs V. Se agrego el parametro: Lynestyle="--", para que las rectas fueran punteadas (no continuas)
    
    plt.plot(V,P,c=Colors[i],label="T={}".format(T))  #Grafica de la funcion P: V vs P
    
plt.title("Isotermas de un Gas Real")  #Titulo de la primera grafica
plt.xlabel("V_red") , plt.ylabel("P_red")  #Titulo de los ejes
plt.xlim(0.4,4),plt.ylim(0,2)  #Delimitación de la imagen mostrada

plt.legend()  #Esta linea pide al programa que muestre los nombres de las graficas

plt.savefig("IsotermasDeUnGasReal")  #Guardar la imagen obtenida

plt.show()  #Mostrar la grafica

#---------------------------Curvas Modificadas----------------------------------------------

#Sección que determina las curvas modificadas

#Grafica de los isotermas los cuales no seran modificados (T>1)
for i in range(4,len(T_data)):
    T = T_data[i]  #Valor de T para el isoterma
    P = presion(T,V)  #Creación del arreglo: P(T,v), para todo v en V
    
    plt.plot(V,P,c=Colors[i],label="T={}".format(T))  #Grafica de la funcion P: V vs P

#Grafica de los isotermas modificados (T<=1). Esta función es de la forma: P={P_0, si: v1<v<v2}+{P, si: v<v1 o v>v3}, con v1,v2,v3 las intersecciones con P_null[i]
for i in range(0,len(P_null)):
    P_0,T_0 = P_null[i],T_data[i]  #P_null[i] es el valor de la presión que divide el isoterma P(T[i]) en dos regiones con misma area
    
    P_new = [] #Arreglo que guarda la curva de la presión modificada

    r = raices(T_0,P_0)  #Obtención de las raices del P_null[i], para el isoterma T.

    #Ingreso de los elementos del arreglo: P_new. 
    for v in V:
        #Si: v<v1 o v>v3, entonces la curva se mantenda segun la función: P=P(t,v)
        if (v<r[0] or v>r[2]):
            P_new.append(presion(T_0,v))

        #Si: v1<v<v3, entonces la curva permanecera constante: P=P_0
        else:
            P_new.append(P_0)

    plt.plot(V,P_new,c=Colors[i],label="T={}".format(T_0))  #Grafica de la función P modificada: V vs P_new


plt.title("Isotermas modificados")  #Titulo de la primera grafica
plt.xlabel("V_red") , plt.ylabel("P_red")  #Titulo de los ejes
plt.xlim(0.4,4),plt.ylim(0,2)  #Delimitación de la imagen mostrada

plt.legend()  #Esta linea pide al programa que muestre los nombres de las graficas

plt.savefig("IsotermaModificado")  #Guardar la imagen obtenida

plt.show()  #Mostrar la grafica
