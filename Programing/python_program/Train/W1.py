n = int(input("Len of n "))

A = []

for i in range(0,n):
    A.append([])
    for j in range(0,n):
        A[i].append(i+j)

B = []

for i in range(0,n):
    B.append([])
    for j in range(0,n):
        s = 0
        X,Y = [i-1,i,i+1],[j-1,j,j+1]
        for a in X:
            for b in Y:
                try:
                    s += A[a][b]
                    print(A[a][b])

                except:
                    s += 0

        B[i].append(s)

for i in A:
    print(*i)

for j in B:
    print(*j)
