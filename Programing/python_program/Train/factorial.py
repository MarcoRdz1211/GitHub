import math

n = int(input())

if n>=3:
    r = n
else:
    r = math.ceil(n/2)

s,k = 0,n

while k!=0:
    p = math.factorial(r)
    if p<=n:
        print(r,p*int(n/p),n-p*int(n/p))
        n = n-p*int(n/p)
        s = s+int(n/p)
        print(s)
    r = r-1
    if n==0:
        k = 0
        n = k

print(s)
