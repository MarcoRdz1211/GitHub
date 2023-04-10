def rest(x):
    return (10*9**(x-1))%(10**9+7)

n = int(input())
A = []

for i in range(0,n):
    x = int(input())
    A.append(rest(x))

for i in A:
    print(i)
