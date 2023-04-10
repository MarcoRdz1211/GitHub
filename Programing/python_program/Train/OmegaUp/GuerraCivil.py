n = int(input())
ans,A = -1,[]

for i in range(0,n):
    aux = list(map(int, input().split()))
    A.append(aux)

for i in range(1,n-1):
    if (A[i][1]<=A[i-1][1]) and (A[i][1]<=A[i+1][1]):
        ans = A[i][0]
        break

print(ans)
    
