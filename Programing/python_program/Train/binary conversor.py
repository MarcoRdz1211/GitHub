import math

def binary(n):
    r,A,i = 0,[],0
    if n==0:
        return r
    else:
        while n>0:
            A.append(math.floor(math.log(n,2)))
            n -= 2**A[i]
            r += 10**A[i]
            i += 1
        
        return r

def decimal(n):
    A,s = list(map(int, str(n))),0
    for i in range(0,len(A)):
        if A[i]==1:
            s += 2**(len(A)-i-1)

    return s

def bcd(n):
    A = list(map(int, str(n)))
    s = ""
    for i in range(0,len(A)):
        s += "0"*(4-len(list(map(int,str(binary(A[i]))))))+str(binary(A[i]))
    return s

def bcd_sum(a,b):
    A = str(binary(a+b))
    A += "0"*(4-len(A))
    B = list(map(int,A))
    print(B)
    r = int(A)
    if ((B[1] == 1 or B[2] == 1) and B[0]==1) or len(B)==5:
        r = binary(decimal(int(A))+6)

    return r
