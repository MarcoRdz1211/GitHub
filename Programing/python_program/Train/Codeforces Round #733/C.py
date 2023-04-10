def ceil(x):
    if x%1==0:
        return int(x)
    else:
        return int(x+1)

t = int(input())
ans = []

for i in range(0,t):
    n = int(input())
    Y = list(map(int, input().split()))
    L = list(map(int, input().split()))
    Y,L = sorted(Y,reverse=True),sorted(L,reverse=True)
    sumY,sumL = 0,0
    k = n-int(n/4)
    
    for i in range(0,k):
        sumY += Y[i]
        sumL += L[i]

    if sumY>=sumL:
        ans.append(0)
    else:
        ans.append(ceil((sum(L)-sumY)/100))

for i in ans:
    print(i)
