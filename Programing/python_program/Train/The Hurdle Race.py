n,k = input().split()
n,k = int(n),int(k)

A = list(map(int, input().split()))

if k>max(A):
    print(0)
else:
    print(max(A)-k)
