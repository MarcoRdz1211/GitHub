n = int(input())
A = input().split()
gen = [A[0]]

print(A)

for i in range(0,n):
    print(A[i])
    if A[i] not in gen:
        gen.append(A[i])
        l = list(A[i]*2)
        print(gen,l)
        for j in range(0,len(A[i])):
            k = ""
            for s in range(j,len(A[i])+j):
                k += l[s]

print(gen)
