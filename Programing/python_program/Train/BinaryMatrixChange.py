def multh(A,n,i):
    s = 1

    for j in range(0,m):
        s *= A[i][j]

    return s

def multv(A,m,j):
    s = 1

    for i in range(0,n):
        s *= A[i][j]

    return s

n,m = map(int, input().split())

A,B = [],[]

for i in range(0,n):
    A.append(list(map(int, input().split())))
    B.append([])

for i in range(0,n):
    for j in range(0,m):
        B[i].append(min(multh(A,n,i),multv(A,m,j)))

for i in B:
    print(*i)
