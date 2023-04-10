import math

A = input().split()
n,m = len(A),4
ans = 0

for i in range(0,n):
    A[i] = A[i].split(",")

for i in range(0,n):
    for j in range(0,m):
        A[i][j] = float(A[i][j])

for i in range(0,n):
    s = 2*A[i][0]/(A[i][1]*A[i][2]*A[i][3])
    
    ans += math.sqrt(s)/n

print(math.ceil(ans))
