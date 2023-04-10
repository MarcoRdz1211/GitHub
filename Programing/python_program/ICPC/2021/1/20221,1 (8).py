n,m = input().split()
n,m = int(n),int(m)
A,B = [],[]
r = 0

for i in range(0,n):
    x = int(input())
    A.append(x),B.append(0)

B[0],s = m,m

for i in range(0,n-1):
    if (A[i]==0):
        B[i]==0
    elif (A[i]>A[i+1]):
        s -= 1
        B[i+1] = s
    elif (A[i]<A[i+1]):
        B[i+1] = s        

    if (s<0):
        r = 1
        break

    if (A[i]==A[i+1] and A[i]!=0):
        r = 1
        break


if (r==1):
    print("ambiguous")
else:
    for i in B:
        print(i)
    
