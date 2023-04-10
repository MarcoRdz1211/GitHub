import math
import random
import numpy as np
import matplotlib.pyplot as plt

def f(A,x):
    s = 0
    for i in range(0,len(A)):
        s += float(A[i])*x**i

    return s

def comb(n,k):
    s = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

    return s

A,X,A1 = [],[],""

n = int(input("The polinomial of wich degree do you want? "))

while (n<0):
    n = int(input("The order of the polinomial have to be a Natural Number: "))

for k in range(0,n+1):
    a = comb(n,k)*(-1)**(n-k)/(math.factorial(n)*2**n)
    A.append("{}".format(a))
    A.append("0")
    X.append("x^{}".format(2*k+1))
    X.append("x^{}".format(2*k))

X.pop(0),A.pop(len(A)-1)

D0,D,P=[],[],[]

for i in range(0,len(A)+1):
    D0.append([]),D.append([]),P.append([])
    for j in range(0,len(A)+1):
        if i==j+1:
            D0[i].append(j+1),D[i].append(j+1)
        else:
            D0[i].append(0),D[i].append(0)

        P[i].append(0)

for r in range(0,n-1):
    for k in range(0,len(A)+1): 
        for j in range(0,len(A)+1): 
            for i in range(0,2*n+1):
                P[k][j] += D0[k][i] * D[i][j]

    for i in range(0,len(A)+1):
         for j in range(0,len(A)+1):
            D[i][j] = P[i][j]
            P[i][j] = 0

#print("\n Basic derivative polinomial matrix of degree {} ".format(n))

#for i in range(0,len(A)+1):
#    print(D0[i])

#print("\n Derivative polinomial matrix of degree {}, wich order is {}".format(n,n))

#for i in range(0,len(A)+1):
#    print(D[i])

S,S1,pol = [],[],""

for j in range(0,len(A)):
    for i in range(0,len(A)):
        if (D[i][j] != 0):
            S.append("{}".format(D[i][j]*float(A[i])))

for i in range(0,len(S)):
    if (float(S[i])!=0):
        if (i+1<len(S) and i*S[i] !=0):
            pol += "{}x^{}+".format(float(S[i]),i)
        elif (i+1==len(S) and i*S[i] !=0):
            pol += "{}x^{}".format(float(S[i]),i)


print("The Lagendre Polynomial of order {}, is: \n P_{}(x)={}".format(n,n,pol))

a = 1

X_data = np.linspace(-a,a,100)
Y_data = f(S,X_data)
Y_axis = np.linspace(-max(abs(Y_data))-2,max(abs(Y_data))+2,100)

plt.title("P_{}={}".format(n,pol))
plt.plot(X_data,np.zeros(len(X_data)),c="black")
plt.plot(np.zeros(len(Y_axis)),Y_axis,c="black")
plt.plot(X_data,Y_data,c="red")
plt.xlim([-a,a])
plt.grid()
plt.show()
