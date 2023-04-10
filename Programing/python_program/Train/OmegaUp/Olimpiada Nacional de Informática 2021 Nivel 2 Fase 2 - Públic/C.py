n = int(input())
m = int(input())
x = list(input())
ans = ""

for i in range(0,m):
    ans += chr(ord(x[i])+n)

print(ans)
