import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.exp(2*x)-1

def df(x):
    return 2*math.exp(2*x)

n = 0

print("This program are gonna give you an approximation to one root of: f(x)=e^(2x)-1")
x = int(input("Give an initial value "))

A,B = [x],[f(x)]

while (abs(f(x))>=10**(-10) or df(x)==0):
    n += 1

    x = x-f(x)/df(x)

#    print("The iteration {} has an approximated value of: {}".format(n,x))

    A.append(x),B.append(f(x))

print("\n An approximation of the root of: f(x)=e^(2x)-1, is: {};".format(x),
      "that has an approximated value: f({})={}, with {} iterations.".format(x,f(x),n))

X = np.arange(min(A)-2,max(A)+2,0.01)

plt.title("f(x)=e^(2x)-1")
plt.xlabel("X"),plt.ylabel("Y")
plt.plot(X,np.zeros(len(X)))
plt.plot(X,np.exp(2*X)-1)
plt.scatter(A,B)
plt.show()
