import math
n,a,b = input().split()
n,a,b = int(n),int(a),int(b)

r = math.ceil(n/a)*a
if r>n:
    print("NO")
elif (n-r)<a and (n-r)!=0:
    print("NO")
else:
    c = b
    N = n
    for i in range(a,b+1):
        n = N
        b = c
        A = []        
        while (n>=a):
            print(n)
            if n-b<a:
                n -= b
                b -= 1
            else:
                n -= b
                A.append(b)
        A.append(b+1)
        c -= 1
        if n==0:
            print("YES")
#            print(A)
            break
        else:
            print("NO")
