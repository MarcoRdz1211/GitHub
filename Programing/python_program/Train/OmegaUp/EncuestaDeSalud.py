n = int(input())
A = []

for i in range(0,n):
    ident = int(input())
    name = str(input())
    weight = float(input())
    heigh = float(input())

    imc = weight/(heigh)**2

    A.append([ident,name,"{:.1f}".format(imc)])

for i in range(1,n+1):
    print(*A[n-i])
