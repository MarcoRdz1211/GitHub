def justify(v, k):
    r = ""
    contador = 0
    
    for i in range(0,len(v)):
        print(r)
        if contador+len(v[i])<=k:
            r += v[i]
            contador += len(v[i])
        else:
            r += "\n"
            contador = 0

        print(r)

    return r

n, k = input().split(' ')
n = int(n)
k = int(k)
v = []

for i in range(n):
    v.append(input())

justified = justify(v, k)

for line in justified:
    print(line)
