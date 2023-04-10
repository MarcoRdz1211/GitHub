import math
import random
import numpy as np
import matplotlib.pyplot as plt

#Definicion de la función a utilizar en numpy para obtener el conjunto de datos
#Para su posterior grafica.
def f(A,B,L,x):
    y = 0
    pi = 4*math.atan(1)

    for i in range(0,len(A)):
        y += float(A[i])*np.sin(pi*i*x/L)+float(B[i])*np.cos(pi*i*x/L)

    return y

#Primera función: f(x) {-p<x<x0}
def f1(x):
    y = -1*x**0
    
    return y

#Segunda función: f(x) {x0<x<p}
def f2(x):
    y = 2*x**0

    return y

#Definición del valor del periodo: p {|x|<p}
p = float(input("Give the value of the period "))


#Indicación al usuario sobre la función a trabajar.
print("Let be the function: \n f(x)=-1: -{}<x<x0 \n f(x)=2: x0<x<{}".format(p,p))

#Obtención del valor a evaluar la serie de Fourier.
x = float(input("Give the value where do you want to evaluated the Fourier Serie: \n"
                "(That value has to be in the interval [-{},{}] ) ".format(p,p)))

#Verificación de que dicho valor a evaluar la serie este en el intervalo del periodo: {-1<x<1}
while (abs(x) > p):
    x = float(input("Give the value where do you want to evaluated the Fourier Serie: \n"
                "(That value has to be in the interval [-1,1]) "))

#Pregunta de hasta que termino se busca obtener la serie.
k = int(input("Give the number of terms that you want: "))

#Definición de elementos auxiliares: Arreglos que guardaran los coeficientes de la serie,
#El valor de las particiones para la integración numerica, el diferencial y el valor de pi.
A,B = [],[]

n,pi = 10**4,4*math.atan(1)
dx = [p/n,p/n]

#Inicio del ciclo iterativo para encontrar cada coeficiente desde el 0 hasta el k.
for r in range(0,k+1):
    A.append(0), B.append(0)
    for i in range(0,n+1):
        xi = [-p+i*dx[0],i*dx[1]]
        s = [r*pi*xi[0]/p,r*pi*xi[1]/p]
        A[r] += (f1(xi[0]+dx[0])+f1(xi[0]))*math.sin(s[0])*dx[0]/(2*p)+(f2(xi[1]+dx[1])+f2(xi[1]))*math.sin(s[1])*dx[1]/(2*p)
        B[r] += (f1(xi[0]+dx[0])+f1(xi[0]))*math.cos(s[0])*dx[0]/(2*p)+(f2(xi[1]+dx[1])+f2(xi[1]))*math.cos(s[1])*dx[1]/(2*p)

#Para los coeficientes A_0 y B_0, se dividen entre 2 dada la expresión de la serie de Fourier.
A[0],B[0] = A[0]/2,B[0]/2

#Inicialización de la variable que guardara la expresión de la serie de Fourier.
fourier = "{:.4f}".format(B[0])

#Inicio de un ciclo que guardara la expresión de la serie de Fourier.
for i in range(1,k+1):
    #Si el coeficiente A_i>10^{-3}, entonces se presupone que A_i no es igual a 0, por lo que se continua con la serie.
    if (abs(A[i]) > 10**(-3)):
        if (A[i] > 0):
            fourier += "+"
        else:
            fourier += "-"

        fourier += "{:.4f}sin({:.4f})".format(A[i],i*pi*x/p)

    #Si el coeficiente B_i>10^{-3}, entonces se presupone que B_i no es igual a 0, por lo que se continua con la serie.       
    if (abs(B[i]) > 10**(-3)):
        if (B[i] > 0):
            fourier += "+"
        else:
            fourier += "-"

        fourier += "{:.4f}cos({:.4f})".format(B[i],i*pi*x/p)            


#Evaluación e impresión de la serie de Fourier en el valor de x.
r = f(A,B,p,x)
print("Fourier general: f({:.3f})={} \n Aproximacion: f({:.3f})={:.3f}".format(x,fourier,x,r))

#Impresión del error porcentual de la serie. Se obtiene determinando la diferencia del valor real y el numerico, entre el real.
if (x < 0):
    print("The porcentual error of the value is: {:.5f}%".format(100*abs((r-f1(x))/f1(x))))

else:
    print("The porcentual error of the value is: {:.5f}%".format(100*abs((r-f2(x))/f2(x))))

#Inicio de la graficación. Se determina un conjunto de 100 datos en el intervalo de: x en [-p,p].
#Para cada conjunto de datos, se aplicara la función respectiva y la función de Fourier definida anteriormente.
X_data,X1_data,X2_data = np.linspace(-p,p,100),np.linspace(-p,0,100),np.linspace(0,p,100)
Y_data,Y1_data,Y2_data = f(A,B,p,X_data),f1(X1_data),f2(X2_data)

#Definición del limite en y maximo.
lim = 1.5*max(Y_data)

#Definición del eje Y.
Y_axis = np.linspace(-max(abs(Y_data))-2,max(abs(Y_data))+2,100)

#Graficación.
plt.title("f(x)=A0/2+sum_1^{} [Ansin(2pix/L)+Bncos(2pix/L)] \n f(x)=-1 (-{}<x<0) \n f(x)=2 (0<x<{})".format(k,p,p))
plt.xlabel("x"),plt.ylabel("y")
plt.plot(1.1*X_data,np.zeros(len(X_data)),c="black")
plt.plot(np.zeros(len(Y_axis)),Y_axis,c="black")
plt.scatter(x,r,c="black",label="Fourier({})".format(x))
plt.plot(X_data,Y_data,c="blue",label="Fourier approximation")
plt.plot(X1_data,Y1_data,c="red",label="f(x)=-1: -{}<x<0".format(p))
plt.plot(X2_data,Y2_data,c="red",label="f(x)=2: 0<x<p".format(p))
plt.xlim([-1.1*p,1.1*p])
plt.ylim([-lim,lim])
plt.legend()

#Comando que guarda la grafica en formato .png
plt.savefig("ConstantFunctionByFourier.png")

#Exposición de la grafica.
plt.show()
