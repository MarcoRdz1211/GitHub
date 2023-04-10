def capicua(n):
    A = list(str(n))
    aux,n = 1,len(A)
    
    for i in range(0,n):
        if (A[i]!=A[n-i-1]):
            aux = 0
            break

    return aux

n = int(input())

while (capicua(n)!=1):
    m,B = 0,list(str(n))

    for i in range(0,len(B)):
        m += int(B[i])*10**i

    n += m

print(n)
