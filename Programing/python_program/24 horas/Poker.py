n,k = input().split()
a = list(input())
b = list(input())

n,k = int(n),int(k)

card = set(a)
A = []

for i in range(0,len(b)):
    if b[i]=="y" and a.count(a[i])==1:
        A.append(a[i])

if len(A)>k:
    print("imposible")
else:
    print(A)
