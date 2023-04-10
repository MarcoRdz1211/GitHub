import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**2+math.exp(x)-2
    return y

def g(x):
    y = math.log(2-x**2)
    return y


print("This program are gonna give you an approximation to one root of: f(x)=x^2+e^x-2")
x = int(input("Give an initial value "))
n = 0

A,B = [x],[f(x)]

while (abs(f(x)) >= 10**(-10)):
    n += 1
    x = g(x)
#    print("The iteration {} has an approximated value of: {}".format(n,x))

    A.append(x),B.append(f(x))

print("\n An approximation of the root of: f(x)=x^2+e^x-2, is: {};".format(x),
      "that has an approximated value: f({})={}, with {} iterations.".format(x,f(x),n))

X = np.arange(min(A)-2,max(A)+2,0.01)

plt.title("f(x)=e^(2x)-1")
plt.xlabel("X"),plt.ylabel("Y")
plt.plot(X,np.zeros(len(X)))
plt.plot(X,np.exp(2*X)-1)
plt.scatter(A,B)
plt.show()
