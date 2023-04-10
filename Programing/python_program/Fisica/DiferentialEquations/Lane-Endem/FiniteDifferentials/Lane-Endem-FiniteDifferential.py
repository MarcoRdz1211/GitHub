import math
import numpy as np
import matplotlib.pyplot as plt

def f1(x,y,v):
    return -math.exp(-y)

def f2(x,y,v):
    x0 = 0.001
    return 2/(x+x0)

def miu(x,y,v):
    return (1/math.sqrt(4*math.pi))*(math.exp(-y/2))*v*y**2

x0,y0,v0 = input("Dar el valor inicial de la variable dependiente (x), la funcion y(x) en ese tiempo, y su respectiva derivada en ese punto: y'(x) ").split()
x0,y0,v0 = float(x0),float(y0),float(v0)
yf,n = float(input("Dar el valor buscado de la funcion ")),200
h,rho_c = abs(yf-y0)/n,1

X,Y,V,rho,M = [x0],[y0],[v0],[rho_c*math.exp(-0)],[miu(x0,y0,v0)]

TextFile = open("LaneEndem-Equation-FiniteDiferentials.txt","w+")

TextFile.write("    xi       psi(num)    psi'(num)   rho(num)     m(num)  \n")
#print("    xi       psi(num)    psi'(num)   rho(num)     m(num)  \n")


for i in range(0,n+1):
    vnew = V[i]-h*(f2(X[i],Y[i],V[i])*V[i]+f1(X[i],Y[i],V[i]))
    ynew = Y[i]-h*f1(X[i],Y[i],V[i])/f2(X[i],Y[i],V[i])-(vnew-V[i])/f2(X[i],Y[i],V[i])
    X.append(X[0]+h*(i+1))
    Y.append(ynew)
    V.append(vnew)
    rho.append(rho_c*math.exp(-Y[i]))
    M.append(miu(X[i],Y[i],V[i]))

    TextFile.write("{:.8f}  {:.8f}  {:.8f}  {:.8f}  {:.8f} \n".format(X[i],Y[i],V[i],rho[i],M[i]))
#    print("{:.8f}  {:.8f}  {:.8f}  {:.8f}  {:.8f} \n".format(X[i],Y[i],V[i],rho[i],M[i]))

TextFile.close()


plt.title("Solution of the equation: xi*phi''+2phi'-xi*e^{-phi}=0")
plt.xlabel("xi")
plt.plot(X,Y,c="blue",label="phi(t)",linewidth=2.5)
plt.plot(X,rho,c="green",label="rho(t)",linewidth=2.5)
plt.plot([min(X),min(X),max(X)],[max(Y),min(Y),min(Y)],c="black")

plt.legend()

plt.savefig("LaneEndem-Equation-FiniteDiferentials.png")

plt.show()


plt.title("Solution of the equation: m=1/sqrt(4pi)*e^{-phi/2}(phi^2)phi'")
plt.xlabel("xi")
plt.plot(X,M,c="blue",label="m(t)",linewidth=2)
plt.plot([min(X),min(X),max(X)],[max(M),min(M),min(M)],c="black")

plt.legend()

plt.savefig("LaneEndem-Equation-Mass-FiniteDifferentials.png")

plt.show()
