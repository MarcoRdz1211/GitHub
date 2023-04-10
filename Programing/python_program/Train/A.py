t = int(input())
ans = []

for i in range(0,t):
    n = int(input())
    A = list(map(int, input().split()))
    count = 0
    
    for j in A:
        if j%2==0:
            count += 1
    
    if count==n:
        ans.append("Yes")
        
    else:
        ans.append("No")

for i in ans:
    print(i)
