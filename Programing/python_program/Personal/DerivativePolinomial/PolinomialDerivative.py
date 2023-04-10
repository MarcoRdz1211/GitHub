import math
import random
import numpy as np
import matplotlib.pyplot as plt

def f(A,x):
    s = 0

    for i in range(0,len(A)):
        s += float(A[i])*x**i

    return s

A,X,A1,Pn= [],[],[],""

ans = str(input("Do you want: a) general polinomial; b) given polinomial "))

while (ans!="a" and ans!="b"):
    ans = str(input("Select one of the given options: a) or b) "))

n = int(input("The polinomial of wich degree do you want? "))

while (n<0):
    n = int(input("The order of the polinomial have to be a Natural Number: "))

x0 = "x"

if (ans=="a"):
    a = "a"
    for i in range(0,n+1):
        A.append(a+"{}".format(i))
        X.append(x0+"^{}".format(i))
        A1.append(random.uniform(-5,5))
        if (i<n):
            Pn += a+"{}".format(i)+x0+"^{}".format(i)+"+"
        else:
            Pn += a+"{}".format(i)+x0+"^{}".format(i)

else:
    for i in range(0,n+1):
        a = str(input("Write the value of the term: {} ".format(i)))
        A.append("{}".format(a))
        X.append(x0+"^{}".format(i))
        if (i<n):
            Pn += a+x0+"^{}".format(i)+"+"
        else:
            Pn += a.format(a)+x0+"^{}".format(i)

m = int(input("\n What is the order of the derivative? "))

while (m<0):
    m = int(input("The order of the derivative have to be a Natural number: "))

D0,D,P=[],[],[]

for i in range(0,n+1):
    D0.append([]),D.append([]),P.append([])
    for j in range(0,n+1):
        if i==j+1:
            D0[i].append(j+1),D[i].append(j+1)
        else:
            D0[i].append(0),D[i].append(0)

        P[i].append(0)

if m>0:
    for r in range(0,m-1):
        for k in range(0,n+1): 
            for j in range(0,n+1): 
                for i in range(0,n+1):
    #                print("D0[{},{}]*D[{},{}]=".format(k+1,i+1,i+1,j+1),D0[k][i],D[i][j],"=",P[k][j])
                    P[k][j] += D0[k][i] * D[i][j]

        for i in range(0,n+1):
            for j in range(0,n+1):
                D[i][j] = P[i][j]
                P[i][j] = 0

else:
    for i in range(0,n+1):
        for j in range(0,n+1):
            if (i==j):
                D[i][j],D0[i][j] = 1,1
            else:
                D[i][j],D0[i][j] = 0,0

print("\n Basic derivative polinomial matrix of degree {} ".format(n))

for i in range(0,n+1):
    print(D0[i])

print("\n Derivative polinomial matrix of degree {}, wich order is {}".format(n,m))

for i in range(0,n+1):
    print(D[i])

S,S1,pol = [],[],""

if (ans=="a"):
    for j in range(0,n+1):
        for i in range(0,n+1):
            if (D[i][j] != 0):
                S.append("{}({})".format(str(D[i][j]),A[i]))
                S1.append(D[i][j] * A1[i])

else:
    for j in range(0,n+1):
        for i in range(0,n+1):
            if (D[i][j] != 0):
                S.append("{}".format(D[i][j]*float(A[i])  ))

if (ans=="a"):
    for i in range(0,len(S)):
        if (i+1<len(S)):
            pol += "{}({})+".format(S[i],X[i])
        else:
            pol += "{}({})".format(S[i],X[i])

else:
    for i in range(0,len(S)):
        if (i+1<len(S) and i*S[i] !=0):
            pol += "{}{}+".format(float(S[i]),X[i])
        elif (i+1==len(S) and i*S[i] !=0):
            pol += "{}{}".format(float(S[i]),X[i])

print("\n The general polinomial of degree {} is: \n Pn(x):={}".format(n,Pn))

if m>n:
    pol = "0"

print("\n The derivative of the polinomial of degree {} is: \n D^{} Pn(x)={}".format(m,m,pol))


a,b = input("\n In which interval do you want the graph? ").split()
a,b = float(a),float(b)

lim = 10

X_data = np.linspace(a,b,100)

if (ans=="a"):
    Y_data = f(A1,X_data)
    Y1_data = f(S1,X_data)

else:
    Y_data = f(A,X_data)
    Y1_data = f(S,X_data)

Y_axis = np.linspace(-max(abs(Y1_data))-2,max(abs(Y1_data))+2,100)
Y1_axis = np.linspace(-max(abs(Y1_data))-2,max(abs(Y1_data))+2,100)

fig, axs = plt.subplots(2)
axs[0].set_title("Pn={}".format(Pn))
axs[0].plot(X_data,np.zeros(len(X_data)),c="black")
axs[0].plot(np.zeros(len(Y_axis)),Y_axis,c="black")
axs[0].plot(X_data,Y_data,c="blue")
axs[0].set_xlim([a,b])
axs[0].set_ylim([-lim,lim])


axs[1].set_title("D^{} Pn={}".format(m,pol))
axs[1].plot(X_data,np.zeros(len(X_data)),c="black")
axs[1].plot(np.zeros(len(Y1_axis)),Y1_axis,c="black")
axs[1].plot(X_data,Y1_data,c="red")
axs[1].set_xlim([a,b])
axs[1].set_ylim([-lim,lim])
plt.show()
