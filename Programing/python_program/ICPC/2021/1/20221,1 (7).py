A = list(map(int, input().split()))
B = [1,5,10,20,50,100]
C = []

m = 0

for i in range(0,6):
    s = B[i]*A[i]

    if (s>m):
        m = s
        n = A[i]
        k = B[i]

for i in range(0,6):
    if ((B[i]*A[i] == m) and A[i]<n):
        n = A[i]
        k = B[i]

print(k)
