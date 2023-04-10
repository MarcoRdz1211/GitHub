n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 1

for i in range(0,n):
    if (A[i]<=B[i]):
        ans = 0

print(ans)
