n = int(input())

A=[]

for i in range(0,n):
    r = list(str(input()))
    A.append(sorted(r))

mx = 1
A.sort()

for i in range(0,n):
    count = 1
    for j in range(i+1,n):
        if A[i]==A[j]:
            count += 1
        if len(A[i])!=len(A[j]):
            break


    if mx<=count:
        mx = count

print(mx)
