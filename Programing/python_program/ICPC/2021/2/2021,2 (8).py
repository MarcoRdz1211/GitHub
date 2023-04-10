n = int(input())

L,A = [],[2,3,4,5,6]

for i in range(0,n):
    k = int(input())
    lista = []
    for j in A:
        if k%j==0:
            lista.append(j)

    if len(lista)==0:
        L.append([-1])
    else:
        L.append(lista)

for i in L:
    print(*i)
