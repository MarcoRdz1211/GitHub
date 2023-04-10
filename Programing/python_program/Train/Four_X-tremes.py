A = list(map(int,input().split()))

A.sort()
print(A[len(A)-1]-A[0])
