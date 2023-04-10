n = int(input())
A = []

for i in range(0,n):
    k = int(input())

    if k==1:
        A.append(0)
    else:
        A.append(2**(k-1))

for i in A:
    print(i)
