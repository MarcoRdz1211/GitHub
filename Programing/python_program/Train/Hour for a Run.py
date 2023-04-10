def ceil(x):
    if x!=int(x):
        return int(x+1)
    else:
        return int(x)

v,n = input().split()
v,n = int(v),int(n)

s,A = n*v/10,[]

for i in range(1,10):
    A.append(ceil(i*s))

print(*A)
