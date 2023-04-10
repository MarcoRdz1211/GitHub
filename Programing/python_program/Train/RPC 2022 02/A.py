a,b = map(int, input().split())

a,b = max(a,b),min(a,b)
n = 0
while a!=b:
    a += 1
    n += 1

    if (a==b):
        break

    if (a%2 == 0):
        n += 1
        a = a/2

print(n)
