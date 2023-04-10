n = int(input())
A = []

for i in range(0,n):
    A.append([])
    for j in range(0,n):
        A[i].append("")

for i in A:
    print(i)

for i in range(0,n):
    A[i][i],A[i][n-i-1] = "@","@"

for i in range(0,n):
    print(*i)
