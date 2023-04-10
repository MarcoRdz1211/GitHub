n = int(input())
A = []

for i in range(0,n):
    x = list(map(int, input().split()))
    ans,p = "Ordered",len(x)

    if x[0]>x[p-1]:
        for j in range(0,p-1):
            if x[j]<x[j+1]:
                ans = "Unordered"
                break
    else:
        for j in range(0,p-1):
            if x[j]>x[j+1]:
                ans = "Unordered"
                break            

    A.append(ans)

for i in A:
    print(i)
