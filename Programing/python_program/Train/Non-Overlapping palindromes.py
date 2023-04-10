import math
T = int(input())

def palindromo(r):
    A = list(r)
    n = len(r)
    for i in range(0,math.ceil(n/2)):
        if A[i]!=A[n-i-1]:
            var = 0 #Paindromo
        else:
            var = 1 #No Palindromo
            break
    return var

for i in range(0,T):
    A = []
    C = []
    a = input()
    B = list(a)
    for j in range(0,len(a)):
        s,r = "",""
        for k in range(0,len(a)):
            if k<j:
                s += B[k]
            else:
                r += B[k]
            
        A.append(s),A.append(r)
        C.append([0,j]),C.append([j,len(a)-1])

    print(A)
    A.pop(0)
    B = []
    for j in range(0,len(A)-1):
        if palindromo(A[j])==0:
            B.append([C[j][0],C[j][1]])
    for j in B:
        print(j)

    max = 0
    for j in range(0,len(C)-1):
        for k in range(i+1,len(C)):
            if not (C[j][0]<=C[k][0] and C[k][0]<C[j][1]) or (C[j][0]<=C[k][0] and C[k][0]<C[j][1]):
                d = C[j][1]+C[k][1]-C[j][0]-C[k][0]
                if d>max:
                    max = d

    print(max)
    input()    
