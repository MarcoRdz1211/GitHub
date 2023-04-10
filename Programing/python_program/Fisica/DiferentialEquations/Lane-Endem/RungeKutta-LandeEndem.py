import math
import random
import numpy as np
import matplotlib.pyplot as plt

def x1(t,x,v):
    return v

def x2(t,x,v):
    return -x

def fx1(t):
    return 1.32*np.cos(t)-3.491*np.sin(t)

def fx2(t):
    return -1.32*np.sin(t)-3.491*np.cos(t)

e,pi = math.exp(1),math.pi

t0,x0,vx0 = input("Dar el valor inicial del tiempo (t0), la funcion x(t) en ese tiempo, y su respectiva derivada en ese punto: x'(t) ").split()
t0,x0,vx0 = float(t0),float(x0),float(vx0)

tf,n = float(input("Dar el valor buscado de la funcion ")),200
t,x,vx = [t0],[x0],[vx0]

h = abs(tf-t[0])/n

TextFile = open("WaveEquation-RungeKutta.txt","w+")

TextFile.write("    t         x(real)      x(num)      x'(real)     x'(num)   \n")
#print("    t         x(real)      x(num)      x'(real)     x'(num)   \n")

for i in range(0,n+1):
    t.append(t[0]+h*i)
    Kx,Kvx = 5*[0],5*[0]
    Kx[1],Kvx[1] = x1(t[i],x[i],vx[i]),x2(t[i],x[i],vx[i])
    Kx[2],Kvx[2] = x1(t[i]+h/2,x[i]+(h/2)*Kx[1],vx[i]+(h/2)*Kvx[1]) , x2(t[i]+h/2,x[i]+(h/2)*Kx[1],vx[i]+(h/2)*Kvx[1])
    Kx[3],Kvx[3] = x1(t[i]+h/2,x[i]+(h/2)*Kx[2],vx[i]+(h/2)*Kvx[2]) , x2(t[i]+h/2,x[i]+(h/2)*Kx[2],vx[i]+(h/2)*Kvx[2])
    Kx[4],Kvx[4] = x1(t[i]+h,x[i]+h*Kx[3],vx[i]+h*Kvx[3]) , x2(t[i]+h,x[i]+h*Kx[3],x[i]+h*Kvx[3])
    x.append(x[i]+(h/6)*(Kx[1]+2*Kx[2]+2*Kx[3]+Kx[4]))
    vx.append(vx[i]+(h/6)*(Kvx[1]+2*Kvx[2]+2*Kvx[3]+Kvx[4]))
        
    TextFile.write("{:.8f}  {:.8f}  {:.8f}  {:.8f}  {:.8f}  \n".format(t[i+1],fx1(t[i+1]),x[i+1],fx2(t[i+1]),vx[i+1]))
#   print("{:.8f}  {:.8f}  {:.8f}  {:.8f}  {:.8f}  \n".format(t[i],fx1(t[i]),x[i],fx2(t[i]),vx[i]))

TextFile.close()

print("El valor analitico de: x({})={:.8f}, x'({})={:.8f} \n".format(t[i],fx1(t[i]),t[i],fx2(t[i])),
      "mientras que el valor numerico es: x({})={:.8f}, x'({})={:.8f} \n".format(t[i],x[i],t[i],vx[i]),
      "con un error porcentual aproximado de: {:.8f}%, {:.8f}%, respectivamente".format(abs(x[i]-fx1(t[i]))*100,abs(vx[i]-fx2(t[i]))*100))

plt.title("Solution of the Wave Equation: d^2 phi(x,t)/dt^2=c^2 d^2 phi(x,t)/dx^2")
plt.xlabel("t")
plt.plot(t,x,c="blue",label="x_num(t)",linewidth=2.5)
plt.plot(t,fx1(t),c="green",label="x_real(t)",linewidth=2.5)
plt.plot([min(t),min(t),max(t)],[max(x),min(x),min(x)],c="black")

plt.legend()

plt.savefig("Wave-Equation.png")

plt.show()
