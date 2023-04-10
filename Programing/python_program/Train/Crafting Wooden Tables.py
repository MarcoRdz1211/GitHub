c,n,p,w=input().split()

c,n,p,w = int(c),int(n),int(p),int(w)
A,t = [],0
k = int(w/n)

for i in range(0,n-1):
    A.append(k)

A.append(w-sum(A))
A.sort(reverse=True)

if A[0]>p:
    for i in range(0,n-1):
        if A[i]>p:
            A[i+1] += A[i]-p
            A[i] = p


A.sort()
count = 0

for i in range(0,n-1):  
    if A[i]>c:
        break
    else:
        count += 1
        if A[i+1]>c-A[i]:
            A[i+1] -= c-A[i]
        else:
            a,b = A[i+1],A[n-1]
            A[i+1],A[n-1] = b,a
            if A[i+1]>c-A[i]:
                A[i+1] -= c-A[i]
            else:
                A[i+1] = 0
        A[i] = 0

    if A[i+1]==0:
        break
    A.sort()

if c>w:
    print(0)
else:
    print(count)
