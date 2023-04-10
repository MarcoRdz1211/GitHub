a,b = map(int, input().split())
A = []

for i in range(a,b+1):
    if (i%a==0):
        A.append(i)

print(*A)
