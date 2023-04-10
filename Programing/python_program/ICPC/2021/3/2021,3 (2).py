n = int(input())
A = []

for i in range(0,n):
    x,y = map(int, input().split())
    A.append([x,y])

A.sort(key=lambda x: x[1])
t,aux = A[0][0]+10,A[0][1]

#print(A[0][0],t)

for i in range(1,n):
    if A[i][1]==aux:
        if A[i][0]<=t:
            t = A[i][0]+t-A[i-1][0]

        else:
            t += 10
        
    else:
        if A[i][0]<=t:
            if A[i-1][1]==aux:
                t += 10
#                print("Auxiliar!",t)
            elif A[i][0]+10>t:
                t = A[i][0]+t-A[i-1][0]
#                print("ahora estamos aqui!",t)

        else:
            t += 10

#    print(A[i][0],t)
     
print(t)
