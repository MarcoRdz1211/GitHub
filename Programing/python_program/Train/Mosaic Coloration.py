n,m,r,c = input().split()
n,m,r,c = int(n),int(m),int(r),int(c)

X = []
for i in range(0,r):
    X.append([])
    Y = list(map(int,input().split()))
    for j in range(0,m):
        X[i].append(Y[j%c])

for i in range(r,n):
    X.append(X[i%r])

if not (n%r == 0 and m%c == 0):
    for i in range(0,r):
        for j in range(0,c):
            


s = 0
for i in range(0,n):
    s += sum(X[i])

for i in X:
    print(i)

print(s)
