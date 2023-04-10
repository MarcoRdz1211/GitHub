n = int(input())
m = int(input())
ans = "S"

for i in range(0,n-1):
    x = int(input())
    if x>m:
        ans = "N"

print(ans)
