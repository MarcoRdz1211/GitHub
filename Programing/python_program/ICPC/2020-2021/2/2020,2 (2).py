m,n,k = input().split()
m,n,k = int(m),int(n),int(k)
 
num = list(map(int, input().split()))
A = []

for i in range(0,k):
    a,b,c = input().split()

for i in range(0,n):
    a = 2
    while num[i]!=1:
        while num[i]%a!=0:
            a += 1
            
        if a not in A:
            A.append(a)
        num[i] /= a

r = ""
A = sorted(set(A))
for i in A:
    r += str(i)+" "

print(r)
