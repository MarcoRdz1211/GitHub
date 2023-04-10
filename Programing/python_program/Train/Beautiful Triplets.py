n,d = map(int, input().split())
A = list(map(int, input().split()))
s = 0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if (A[j]-A[i]==d) and (A[k]-A[j]==d):
                s += 1

print(s)
