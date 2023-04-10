a,b = map(int, input().split())
ans = []

for i in range(a,b+1):
    ans.append(i)

print(*ans)
