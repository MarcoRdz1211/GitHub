m,n = map(int, input().split())
A,ans = [],[]

for i in range(0,m):
    aux = list(map(int, input().split()))
    A += aux

B = set(A)

for i in B:
    ans.append(A.count(i))

print(*ans)
