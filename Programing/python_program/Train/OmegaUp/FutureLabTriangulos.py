n = int(input())
A = list(map(int, input().split()))
A.sort()

s = A[n-1]+A[n-2]+A[n-3]
print(s)
