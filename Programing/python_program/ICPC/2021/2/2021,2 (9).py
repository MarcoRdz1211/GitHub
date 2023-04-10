n = int(input())
A = []

for i in range(0,n):
    k = int(input())
    x,m,S = "2",0,[]
    while k!=1:
        m += 1
        if k%2==1:
            S.append(1)
            k -= 1
        else:
            S.append(0)
            k /= 2

    for j in range(1,m+1):
        if S[m-j]==1:
            x = "(2*"+x+")"
        else:
            x = "("+x+")^2"

    A.append(x)

for i in A:
    print(i)
