n = int(input())
A = []
L = ["0","1","2","3","4","5","6","7","8","9"]
M = ["O","I","Z","E","A","S","G","T","B","P"]

for i in range(0,n):
    x = list(input())
    p = len(x)

    for j in range(0,p):
        if x[j] in L:
            x[j]=M[int(x[j])]
            
    A.append(''.join(map(str,x)))

for i in A:
    print(i)
