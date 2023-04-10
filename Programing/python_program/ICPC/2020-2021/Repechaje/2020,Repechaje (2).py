n,m = input().split()
n,m = int(n),int(m)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

waste,s,j = 0,B[0],0

for i in range(0,n):
    if (s<A[j]):
        waste += s
        j += 1
    elif (s==A[i]):
        j += 1
    else:
        s -= A[i]

for i in range(j,m):
    waste += s
    s = B[i]

print(waste)
