a,b = input().split(";")
x = list(map(int,a))
y = list(map(int,b))

n,t = input().split()
n,t = int(n),int(t)
A = []

for i in range(0,n):
    A.append(list(map(int,input())))

for i in range(0,n):
    A[i][0].append(A[i][len(A)-2]),A[i][0].append(A[i][len(A)-1])
    A[i][len(A)-1].append(A[i][]),A[i][len(A)-1].append(A[i][])

for i in A:
    print(i)
