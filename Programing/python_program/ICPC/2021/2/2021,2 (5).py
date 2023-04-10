def ceil(x):
    if int(x)!=x:
        return int(x+1)
    else:
        return x
    
n = int(input())
A = []

for i in range(0,n):
    C,R,S = input().split()
    C,R,S = int(C),int(R),int(S)

    ans1 = C//S
    ans2 = ((C-ans1*S+R)//S-2)%S

    A.append([ans1,ans2])

for i in range(0,len(A)):
    print(*A[i])
