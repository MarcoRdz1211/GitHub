import random
import time

start_time = time.time()

def prime(x,s):
    count = 2
    for i in range(2,int(x**(1/2))+1):
        if (x%i==0):
            count += 1
            break

    if (count==2 and x!=1):
        return x
    else:
        return s+1

n=int(input())
K = []

for i in range(0,n):
    count = 0
    a,b = input().split()
    a,b = int(a),int(b)

    if (a==prime(a,a)):
        count += 1
    else:
        for j in range(2,int(a**(1/2))+1):
            if (a%prime(j,a)==0 and prime(j,a)%1==0):
                count += 1
            if (a%prime(a/j,a)==0 and prime(a/j,a)%1==0):
                count += 1

    if (b==prime(b,b)):
        count += 1
    else:
        for j in range(2,int(b**(1/2))+1):
            if (b%prime(j,b)==0 and prime(j,b)%1==0):
                count += 1
            if (b%prime(b/j,b)==0 and prime(b/j,b)%1==0):
                count += 1

    K.append(count)

for i in K:
    print(i)

print("--- %s seconds ---" % (time.time() - start_time))
