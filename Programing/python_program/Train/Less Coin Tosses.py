import math

n = int(input())+1
A = []

while n>1:
    x = int(math.log(n,2))
    A.append(1)
    n -= 2**x
    print(n)
    input()

print(A)
