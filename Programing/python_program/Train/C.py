t = int(input())
ans = []

for i in range(0,t):
    n = int(input())
    f = 5
    
    if n==1:
        ans.append(f-3)
    elif n==2:
        ans.append(f)
    else:
        for j in range(3,n+1):
            if j%2==1:
                f += 2
            else:
                a = 1
                r = 3
                while a!=0:
                    if j/r != int(j/r):
                        f += r
                        a = 0
                    else:
                        r += 1
                        
        ans.append(f)

for i in ans:
    print(i%(10**9+7))
