n = int(input())
A = list(map(int, input().split()))
k = int(input())

mx = 0

if k<n:
    for i in range(0,n-k+1):
        s = 0

        for j in range(i,i+k):
            s += A[j]
        
        if s>mx:
            mx = s

    print(mx)

else:
    print("Invalid")
