import math

n = int(input())

if n>=3:
    r = n
else:
    r = math.ceil(n/2)

count = 0

while r!=0:
    p = math.factorial(r)

    if p<=n:
        count = count+int(n/p)
        n -= p*int(n/p)        
    r = r-1

print(count)
