n,m = map(int, input().split())
A,B = [(m+2)*[0]],[(m+2)*[0]]

for i in range(0,n):
    aux = list(map(int, input().split()))
    aux.insert(0,0),aux.insert(m+1,0)
    A.append(aux),B.append((m+2)*[0])

A.append((m+2)*[0]),B.append((m+2)*[0])

for i in range(1,n+1):
    for j in range(1,m+1):
        B[i][j] += A[i-1][j-1]+A[i-1][j]+A[i-1][j+1]
        B[i][j] += A[i+1][j-1]+A[i+1][j]+A[i+1][j+1]
        B[i][j] += A[i][j-1]+A[i][j]+A[i][j+1]

B.pop(n+1),B.pop(0)

for i in B:
    i.pop(m+1),i.pop(0)

for i in B:
    print(*i)
