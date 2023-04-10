import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x)

n = 0

print("This program are gonna give you an approximation to one root of: f(x)=sin(x)")
x0,x1 = input("Give an initial interval ").split()
x0,x1 = int(x0),int(x1)

while f(x0)*f(x1)>0:
    x0,x1 = int(input("Give an initial interval such that has a root in ").split)
    x0,x1 = int(x0),int(x1)

x = (x0+x1)/2

A,B = [x0,x1,x],[f(x0),f(x1),f(x)]

while (abs(f(x))>=10**(-10)):
    n += 1
    if f(x0)*f(x)>0:
        x0 = x
    else:
        x1 = x

#    print("The iteration {} has an approximated value of: {}".format(n,x))

    x = (x0+x1)/2
    A.append(x),B.append(f(x))

print("\n An approximation of the root of: f(x)=sin(x), is: {};".format(x),
      "that has an approximated value: f({})={}, with {} iterations.".format(x,f(x),n))

X = np.arange(min(A)-5,max(A)+5,0.01)

plt.title("f(x)=sin(x)")
plt.xlabel("X"),plt.ylabel("Y")
plt.plot(X,np.zeros(len(X)))
plt.plot(X,np.sin(X))
plt.scatter(A,B)
plt.show()
