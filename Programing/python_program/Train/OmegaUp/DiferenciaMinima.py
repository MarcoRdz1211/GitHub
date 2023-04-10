n = int(input())
A = list(map(int, input().split()))

A.sort()
ans = A[n-1]-A[0]

for i in range(0,n-1):
    if (A[i+1]-A[i])<ans:
        ans = A[i+1]-A[i]

print(ans)
