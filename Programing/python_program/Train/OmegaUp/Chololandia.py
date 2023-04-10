n,k = map(int, input().split())
ans = 0

for i in range(0,n):
    x = int(input())

    if (x<k):
        ans += 1

print(ans)
