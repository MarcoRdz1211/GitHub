a,b = map(int, input().split())
count = 1
m = min(a,b)

for i in range(2,m+1):
    if (a%i == 0) and (b%i == 0):
        count += 1

print(count)
