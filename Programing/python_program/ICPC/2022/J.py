n,m = map(int, input().split())
A = []

for i in range(n):
    aux = list(map(int, input().split()))
    A.append(aux)

B = list(range(1,m+1))

print(sorted(A),B)

for i in range(n):
    if A[i]!=0:
        A[i][1]
