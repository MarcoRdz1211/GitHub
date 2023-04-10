A = []
X = []
Pn = ""

n = int(input("The polinomial of wich degree do you want? "))
a = "a"
x0 = "x"

for i in range(0,n+1):
    A.append(a+"{}".format(i))
    X.append(x0+"^{}".format(i))
    if (i<n):
        Pn += a+"{}".format(i)+x0+"^{}".format(i)+"+"
    else:
        Pn += a+"{}".format(i)+x0+"^{}".format(i)

m = int(input("\n What is the order of the derivative? "))

D0,D,P=[],[],[]

for i in range(0,n+1):
    D0.append([]),D.append([]),P.append([])
    for j in range(0,n+1):
        if i==j+1:
            D0[i].append(j+1),D[i].append(j+1)
        else:
            D0[i].append(0),D[i].append(0)

        P[i].append(0)

if m>0:
    for r in range(0,m-1):
        for k in range(0,n+1): 
            for j in range(0,n+1): 
                for i in range(0,n+1):
    #                print("D0[{},{}]*D[{},{}]=".format(k+1,i+1,i+1,j+1),D0[k][i],D[i][j],"=",P[k][j])
                    P[k][j] += D0[k][i] * D[i][j]

        for i in range(0,n+1):
            for j in range(0,n+1):
                D[i][j] = P[i][j]
                P[i][j] = 0

else:
    for i in range(0,n+1):
        for j in range(0,n+1):
            if (i==j):
                D[i][j],D0[i][j] = 1,1
            else:
                D[i][j],D0[i][j] = 0,0

print("\n Basic derivative polinomial matrix of degree {} ".format(n))

for i in range(0,n+1):
    print(D0[i])

print("\n Derivative polinomial matrix of degree {}, wich order is {}".format(n,m))

for i in range(0,n+1):
    print(D[i])

S = []

for j in range(0,n+1):
    for i in range(0,n+1):
        if (D[i][j] != 0):
            S.append("{}({})".format(str(D[i][j]),A[i]))

pol = ""    

for i in range(0,len(S)):
    if (i+1<len(S)):
        pol += "{}({})+".format(S[i],X[i])
    else:
        pol += "{}({})".format(S[i],X[i])

print("\n The general polinomial of degree {} is: \n Pn(x):={}".format(n,Pn))

if m<n:
    print("\n The derivative of the polinomial of degree {} is: \n Pn'(x)={}".format(n,pol))

else:
    print("\n The derivative of the polinomial of degree {} is: \n Pn'(x)=0".format(n,))
    
