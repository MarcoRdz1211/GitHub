def prime(x):
    count = 2
    for i in range(2,int(x**(1/2))+1):
        if (x%i==0):
            count += 1
            break

    if (count==2 and x!=1):
        return x
    else:
        return 0.001


n=int(input())
K=[]
 
for i in range(0,n):
    L = []
    a,b=input().split()
    a,b=int(a),int(b)

    if (a==prime(a)):
        L.append(a)

    else:
        for j in range(2,int(a**(1/2))+1):
            if (a%j==0 and prime(j)==j):
                L.append(j)
                
            if (a%int(a/j)==0 and prime(a/j)==a/j):
                L.append(a/j)

    if (b==prime(b)):
        L.append(b)

    else:
        for j in range(2,int(b**(1/2))+1):
            if (b%j==0 and prime(j)==j):
                L.append(j)

            if (b%int(b/j)==0 and prime(b/j)==b/j):
                L.append(b/j)

    K.append(len(set(L)))

for i in range(0,n):
    print(K[i])
