import math
import matplotlib.pyplot as plt
import random

def rev(n):
    A = list(map(int,str(n)))
    s = 0
    for i in range(0,len(A)):
        s += A[i]*10**(i)

    return s

A,n = [],random.randint(100,10000)

for i in range(2,n):
    s = 2
    for j in A:
        if i%j==0:
            s += 1
        if s>2:
            break
    
    if s==2:
        A.append(i)

X = [[],[]]

for i in A:
    if rev(i) in A:
        X[0].append(i),X[1].append(rev(i))

x_axis=[[0,max(X[1])],[0,0]]
y_axis=[[0,0],[0,max(X[1])]]

plt.scatter(X[0],X[1])
for i in range(0,len(X[1])):
    plt.plot([X[0][i],X[1][i]],[X[1][i],X[0][i]])

plt.plot(x_axis[0],x_axis[1]),plt.xlabel("x")
plt.plot(y_axis[0],y_axis[1]),plt.ylabel("y")
plt.text(max([1]),1.05*max(X[1]),"Simetric of the first{} prime numbers".format(n))

plt.show()
