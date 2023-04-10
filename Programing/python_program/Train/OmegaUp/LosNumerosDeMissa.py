n = int(input())
A = list(map(int, str(n)))

ans,s = -1,0

while (ans==-1):
    m = 0

    for i in A:
        m += i**s
    
    if (m==n):
        ans = s

    elif (m>n):
        break

    else:
        s += 1

print(ans)
