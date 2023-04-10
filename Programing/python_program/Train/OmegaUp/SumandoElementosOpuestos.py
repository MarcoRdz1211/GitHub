n = int(input())
A = list(map(int, input().split()))
ans = []

for i in range(0,n//2):
    ans.append(A[i]+A[n-i-1])

print(*ans)
