n = int(input())

A = list(map(int,input().split()))
B = []

for i in A:
    B.append(i)

B.sort()
count = 0

while A != B:
    for i in range(0,n-1):
        for j in range(0,i):
            if A[i]>A[i+1]:
                count += 1
                A[i+1],A[i] = A[i],A[i+1]
            if A==B:
                break

print(count)
