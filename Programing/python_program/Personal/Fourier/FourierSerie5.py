import math
import random
import numpy as np
import matplotlib.pyplot as plt

def f(A,B,L,x):
    y = 0
    pi = 4*math.atan(1)

    for i in range(0,len(A)):
        y += float(A[i])*np.sin(pi*i*x/L)+float(B[i])*np.cos(pi*i*x/L)

    return y

def f1(x,p):
    y = x**2
    
    return y

def f2(x,p):
    y = x/(2*p)+1/2

    return y

#Definición del valor del periodo: p=1 {|x|<p}
p = float(input("Give the value of the period "))

print("Let be the function: \n f(x)=x/(2p)+1/2: -{}<x<{}".format(p,p))

x = float(input("Give the value where do you want to evaluated the Fourier Serie: \n"
                "(That value has to be in the interval [-{},{}] ) ".format(p,p)))

while (abs(x) > p):
    x = float(input("Give the value where do you want to evaluated the Fourier Serie: \n"
                "(That value has to be in the interval [-{},{}]) ".format(p,p)))

k = int(input("Give the number of terms that you want: "))

A,B = [],[]

n,pi = 10**4,4*math.atan(1)
dx = [p/n,p/n]

for r in range(0,k+1):
    A.append(0), B.append(0)
    for i in range(0,n+1):
        xi = [-p+i*dx[0],i*dx[1]]
        s = [r*pi*xi[0]/p,r*pi*xi[1]/p]
        A[r] += (f1(xi[0]+dx[0],p)+f1(xi[0],p))*math.sin(s[0])*dx[0]/(2*p)+(f2(xi[1]+dx[1],p)+f2(xi[1],p))*math.sin(s[1])*dx[1]/(2*p)
        B[r] += (f1(xi[0]+dx[0],p)+f1(xi[0],p))*math.cos(s[0])*dx[0]/(2*p)+(f2(xi[1]+dx[1],p)+f2(xi[1],p))*math.cos(s[1])*dx[1]/(2*p)

A[0],B[0] = A[0]/2,B[0]/2

fourier = "{:.4f}".format(B[0])

for i in range(1,k+1):
    if ((abs(A[i]) > 10**(-3)) and (abs(math.sin(i*pi*x/p)) > 10**(-3))):
        if (A[i] > 0):
            fourier += "+"
        else:
            fourier += "-"

        fourier += "{:.4f}sin({:.4f})".format(abs(A[i]),i*pi*x/p)

            
    if ((abs(B[i]) > 10**(-3)) and (abs(math.cos(i*pi*x/p)) > 10**(-3))):
        if (B[i] > 0):
            fourier += "+"
        else:
            fourier += "-"

        fourier += "{:.4f}cos({:.4f})".format(abs(B[i]),i*pi*x/p)


r = f(A,B,p,x)
print("Fourier general: f({:.3f})={} \n Aproximacion: f({:.3f})={:.3f}".format(x,fourier,x,r))

if (x < 0):
    print("While, the real value is: f({:.3f})={:.3f}".format(x,f1(x,p)))
    print("The porcentual error of the value is: {:.5f}%".format(100*abs((r-f1(x,p))/f1(x,p))))

else:
    print("While, the real value is: {}".format(f2(x,p)))
    print("The porcentual error of the value is: {:.5f}%".format(100*abs((r-f2(x,p))/f2(x,p))))

X_data,X1_data,X2_data = np.linspace(-p,p,100),np.linspace(-p,0,100),np.linspace(0,p,100)
Y_data,Y1_data,Y2_data = f(A,B,p,X_data),f1(X1_data,p),f2(X2_data,p)

lim = 1.5*max(Y_data)

Y_axis = np.linspace(-max(abs(Y_data))-2,max(abs(Y_data))+2,100)

plt.title("f(x)=A0/2+sum_1^{} [Ansin(2pix/L)+Bncos(2pix/L)]".format(k))
plt.xlabel("x"),plt.ylabel("y")
plt.plot(1.1*X_data,np.zeros(len(X_data)),c="black")
plt.plot(np.zeros(len(Y_axis)),Y_axis,c="black")
plt.scatter(x,r,c="black",label="Fourier({})".format(x))
plt.plot(X_data,Y_data,c="blue",label="Fourier approximation")
plt.plot(X1_data,Y1_data,c="red",label="f(x)=x/(2{})+1/2: -{}<x<0".format(p,p))
plt.plot(X2_data,Y2_data,c="red",label="f(x)=x/(2{})+1/2: 0<x<{}".format(p,p))
plt.xlim([-1.1*p,1.1*p])
plt.ylim([-lim,lim])
plt.legend()

plt.savefig("FunctionByFourier5.png")

plt.show()
