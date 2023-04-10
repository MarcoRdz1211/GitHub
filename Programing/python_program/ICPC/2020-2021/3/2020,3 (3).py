T = int(input())
B = []

for i in range(0,T):
    a,b = input().split()
    A,b = list(str(a)),int(b)
    suma,l = 0,""
    for j in range(0,len(A)):
        try:
            A[j] = int(A[j])
        except:
            A[j] = str(A[j])

    if type(A[0]) is not int:
        A.insert(0,1)

    for j in range(0,len(A)-1):
        if (type(A[j]) is str) and (type(A[j+1]) is str):
            A.insert(j+1,1)

    print(A)        

    l = ""
    for j in range(0,len(A)/2):
        l += A[j]*A[j+1]
        suma += A[j]
    
    if suma>b:
        B.append("unexpected")
    else:
        B.append(l)
    print(a,b,A)

print(B,l,"\n ----")

for i in B:
    print(i)
