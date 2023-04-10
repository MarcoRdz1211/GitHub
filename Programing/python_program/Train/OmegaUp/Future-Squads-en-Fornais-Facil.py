def fac(n):
    s = 1
    for i in range(2,n+1):
        s = s*i

    return s

A = list(input().split())
n = len(A)

if ("Ricardo" in A):
    n -= 1

if ("Mirón" in A):
    n -= 1

print(int(fac(n)/(fac(4)*fac(4-n))))
