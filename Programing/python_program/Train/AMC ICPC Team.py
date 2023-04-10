import math

def binary(a,b):
    if (a+b)>=1:
        return 1
    else:
        return 0

n,m = input().split()
n,m = int(n),int(m)

X,Y = [],[]

for i in range(0,n):
    X.append(int(input()))
    if X[i]>=10**(m-1):
        X[i] = X[i]+10**int(math.log(X[i],10)+1)
        
    else:
        X[i]=X[i]+10**m

    X[i]=list(map(int,str(X[i])))
    X[i].pop(0)

maxi,count_max = sum(X[0]),1
for i in range(0,n-1):
    for j in range(i+1,n):
        suma = 0
        for k in range(0,m):
            suma += binary(X[i][k],X[j][k])
#            print("{}+{}={}".format(X[i][k],X[j][k],binary(X[i][k],X[j][k])))
#        print("{}+{}={}".format(X[i],X[j],suma),"\n")
        if suma>maxi:
            maxi = suma
            count_max = 1
        elif suma==maxi:
            count_max += 1

#print("------")
print(maxi)
print(count_max)
