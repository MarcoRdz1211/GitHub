n,a,q = input().split()
A = list(map(int, input().split()))

n,a,q = int(n),int(a),int(q)
x = []

for i in range(0,q):
    s = int(input())
    x.append(A[(s-a)%n])

for i in range(0,len(x)):
    print(x[i])
