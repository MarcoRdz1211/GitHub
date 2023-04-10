A = list(map(int, input().split()))

tot,suma = 0,0

if sum(A)<500:
    tot = sum(A)

else:
    sorted(A,reverse=True)
    for i in A:
        suma += i
        print(suma,tot)
        if suma>=500:
            tot += suma-100
            suma = 0

tot += A[2]
print(tot)
