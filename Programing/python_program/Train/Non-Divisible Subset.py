n,k = input().split()

n,k = int(n),int(k)
A = list(map(int,input().split()))
B = []

for i in range(0,n):
    A[i] = A[i]%k
    B.append(0)

A.sort()
print(A)

while 
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (A[i]+A[j])%k == 0:
                B[i],B[j] = B[i]+1,B[j]+1

    print(B)
