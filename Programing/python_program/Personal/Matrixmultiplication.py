n = int(input("What is the dimensions of the matrix "))
m = int(input("What is the degree of the matrix "))
A,B,P=[],[],[]

for i in range(0,n):
    A.append([]),B.append([]),P.append([])
    for j in range(0,n):
        if i==j+1:
            A[i].append(j+1),B[i].append(j+1)
        else:
            A[i].append(0),B[i].append(0)

        P[i].append(0)

for r in range(0,m-1):
    for k in range(0,n): 
        for j in range(0,n): 
            for i in range(0,n):
#                print("A[{},{}]*B[{},{}]=".format(k+1,i+1,i+1,j+1),A[k][i],B[i][j],"=",P[k][j])
                P[k][j] += A[k][i] * B[i][j]

    for i in range(0,n):
        for j in range(0,n):
            B[i][j] = P[i][j]
            P[i][j] = 0

print("\n A".format(m))

for i in range(0,n):
    print(A[i])

print("\n A^{}".format(m))

for i in range(0,n):
    print(B[i])
