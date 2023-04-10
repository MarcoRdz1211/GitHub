p,n = input().split()
p,n = list(str(p)),int(n)
l,ans = len(p),""

for i in range(0,n):
    ans += p[i]

for i in range(0,n):
    ans += p[l-n+i]

print(ans)
