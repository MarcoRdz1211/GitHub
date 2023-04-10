import math

s = str(input())
A = list(s)
n0 = len(A)
n = math.sqrt(n0)
k,l = math.floor(n),math.ceil(n)

B = []

a = ""
for i in range(0,n0):
    if i%l == l-1:
        B.append(list(a+A[i]))
        a = ""
    else:
        a += A[i]

B.append(list(a))

a = ""

for i in range(0,len(B[0])):
    for j in range(0,len(B)):
        if len(B[j])>i:
            a += B[j][i]
    a += " "

print(a)
