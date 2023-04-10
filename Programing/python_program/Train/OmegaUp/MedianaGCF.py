n = int(input())
A = list(map(int, input().split()))

if (n%2==1):
    print(A[n//2])

else:
    print((A[n//2]+A[n//2+1])/2)
