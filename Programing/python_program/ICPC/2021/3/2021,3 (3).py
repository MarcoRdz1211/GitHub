n,k = map(int, input().split())
A = []

for i in range(0,n):
    x,y = map(int, input().split())
    A.append([x,y])

ans = "Y"

for i in range(0,n):
    if A[i][1]!=A[A[i][0]-1][1]:
        ans = "N"

print(ans)
