n,m = input().split()
n,m = int(n),int(m)
A,B,P=[],[],[]

for i in range(0,n):
    X = list(map(float, input().split()))
    A.append(X),B.append(X)
    P.append([])
    for j in range(0,n):
        P[i].append(0)

for i in range(0,m-1):
    for i in range(0,n): 
        for j in range(0,n): 
            for k in range(0,n): 
                P[i][j] += B[k][j] * A[i][k] 

    for i in range(0,n):
        for j in range(0,n):
            B[i][j] = P[i][j]
            P[i][j] = 0
    

for i in range(0,n):
    print(B[0][i])
