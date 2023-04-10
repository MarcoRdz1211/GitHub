def fac(x):
    s = 1
    for i in range(2,x+1):
        s = s*i

    return s

n = int(input())
L = []

for i in range(0,n):
    a,b = map(int, input().split())
    a = fac(a)

    while b!=0:
        a,b = b,a%b

    L.append(a)

for i in L:
    print(i)
