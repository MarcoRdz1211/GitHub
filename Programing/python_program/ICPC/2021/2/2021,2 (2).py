n = int(input())
A = []

for i in range(0,n):
    X = str(input())
    Y,ans = [],-1

    for i in X:
        if i=="B":
            Y.append(-1)
        else:
            Y.append(1)

    Y,n = 2*Y,len(X)

    for r in range(0,n):
        suma,count = 0,0
        for j in range(r,r+n):
            suma1 += Y[j]
            count += 1
            if suma>0:
                break

        if count==n and suma<=0:
            ans = r
            break

    print(ans)

for i in A:
    print(i)
