import matplotlib.pyplot as plt
import random
import numpy as np
import math

def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count += 1
            if count > 2:
                break

    if count == 2:
        return 1
    else:
        return 0

def count_primes(n):
    count = 0
    for i in range(0,n+1):
        count += prime(i)

    return count

#n=random.randrange(10**2,10**4)
n=int(input("Give the number under to verify the number of primes "))
print(n)

X,PRIMES = [[],[]],[]
#Y_x = np.aray(1,n)
#Y_y = Y_x/np.log(Y_x)
count = 0
abcd = 0

for i in range(0,n+1):
    if i<=2:
        count += prime(i)
        X[0].append(i)
        X[1].append(count)

        if prime(i)==1:
            PRIMES.append(i)

    if i>2:
        subcount = 0
        for j in PRIMES:
            if i%j==0:
                subcount += 1
                if subcount > 0:
                    break

        if subcount == 0:
            count += 1
            PRIMES.append(i)

    X[0].append(i)
    X[1].append(len(PRIMES))

    if i%10000==0:
        print(i)

x_axis=[[0,n],[0,0]]
y_axis=[[0,0],[0,count]]

plt.plot(X[0],X[1])
#plt.plot(Y_x,Y_y)
plt.plot(x_axis[0],x_axis[1]),plt.xlabel("number")
plt.plot(y_axis[0],y_axis[1]),plt.ylabel("count_prime")
plt.text(n,count-count/15,"({},{})".format(n,count))
plt.text(n/4,count,"Prime distribution from 0 to {}".format(n))

plt.show()
