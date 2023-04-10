import math
import random
import numpy as np
import matplotlib.pyplot as plt

def y1(t,y,v):
    return v

def y2(t,y,v):
    e= math.exp(1)
    t0 = 0.0001
    return e**(-y)-(2/(t+t0))*v

def r(t,c):
    return c*math.exp(-t)

def miu(t,y,v):
    return (1/math.sqrt(4*math.pi))*(math.exp(-y/2))*v*y**2

def f1(t):
    return (1/6)*np.power(t,2)

def f2(t):
    return (1/3)*np.exp(np.power(t,1))

e,pi = math.exp(1),math.pi

t0,y0,v0 = input("Dar el valor inicial de la variable dependiente (x), la funcion y(x) en ese tiempo, y su respectiva derivada en ese punto: y'(x) ").split()
t0,y0,v0 = float(t0),float(y0),float(v0)

tf,n = float(input("Dar el valor buscado de la funcion ")),200
t,y,v = [t0],[y0],[v0]
m = [miu(t[0],y[0],v[0])]

h,rho_c = abs(tf-t[0])/n,1
rho = [r(0,rho_c)]

TextFile = open("LaneEndem-Equation.txt","w+")

TextFile.write("    xi       psi(num)    psi'(num)   rho(num)     m(num)  \n")
#print("    xi       psi(num)    psi'(num)   rho(num)     m(num)  \n")

for i in range(0,n+1):
    t.append(t[0]+h*i)
    Ky,Kv = 5*[0],5*[0]
    Ky[1],Kv[1] = y1(t[i],y[i],v[i]),y2(t[i],y[i],v[i])
    Ky[2],Kv[2] = y1(t[i]+h/2,y[i]+(h/2)*Ky[1],v[i]+(h/2)*Kv[1]) , y2(t[i]+h/2,y[i]+(h/2)*Ky[1],v[i]+(h/2)*Kv[1])
    Ky[3],Kv[3] = y1(t[i]+h/2,y[i]+(h/2)*Ky[2],v[i]+(h/2)*Kv[2]) , y2(t[i]+h/2,y[i]+(h/2)*Ky[2],v[i]+(h/2)*Kv[2])
    Ky[4],Kv[4] = y1(t[i]+h,y[i]+h*Ky[3],v[i]+h*Kv[3]) , y2(t[i]+h,y[i]+h*Ky[3],v[i]+h*Kv[3])
    y.append(y[i]+(h/6)*(Ky[1]+2*Ky[2]+2*Ky[3]+Ky[4]))
    v.append(v[i]+(h/6)*(Kv[1]+2*Kv[2]+2*Kv[3]+Kv[4]))
    rho.append(r(y[i],rho_c))
    m.append(miu(t[i],y[i],v[i]))
        
    TextFile.write("{:.8f}  {:.8f}  {:.8f}  {:.8f}  {:.8f} \n".format(t[i+1],y[i],v[i],rho[i],m[i]))
#    print("    xi       psi(num)    psi'(num)   rho(num)     m(num)  \n")

TextFile.close()

plt.title("Solution of the equation: xi*phi''+2phi'-xi*e^{-phi}=0")
plt.xlabel("xi")
plt.plot(t,y,c="blue",label="phi(t)",linewidth=2.5)
plt.plot(t,rho,c="green",label="rho(t)",linewidth=2.5)
plt.plot([min(t),min(t),max(t)],[max(y),min(y),min(y)],c="black")

plt.legend()

plt.savefig("LaneEndem-Equation.png")

plt.show()

plt.title("Solution of the equation: m=1/sqrt(4pi)*e^{-phi/2}(phi^2)phi'")
plt.xlabel("xi")
plt.plot(t,m,c="blue",label="m(t)",linewidth=2)
plt.plot([min(t),min(t),max(t)],[max(m),min(m),min(m)],c="black")

plt.legend()

plt.savefig("LaneEndem-Equation-Mass.png")

plt.show()
