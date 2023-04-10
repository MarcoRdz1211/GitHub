n = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(1,10):
    while A[i-1]!=0:
        if (i in n):
            n.remove(i)
        else:
            A[i]=0
        print(A[i],n)
        input()
