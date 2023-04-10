n,m = input().split()
n,m = int(n),int(m)
A = list(map(int,input().split()))
S = set(list(map(int,input().split())))

B = []
for i in range(0,len(A)+len(S)):
    B.append(0)

r = 0
for i in S:
    n += 1
    for j in range(0,n-1):
        if A[j]<=i:
            if j<n-1:
                B.append(A[j])
            else:
                B[j+1]=i
            k = 0
        else:
            B[j]=i
            for up in range(j+1,n):
                B[up]=A[up-1]
            break

    A = []
    for j in range(0,n):
        A.append(B[j])

p = ""
for i in A:
    p += str(i)+" "

print(p)
