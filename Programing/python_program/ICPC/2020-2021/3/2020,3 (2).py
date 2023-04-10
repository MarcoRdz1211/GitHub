T=int(input())
 
A=[]
 
for i in range(0,T):
    n,k=input().split()
    n,k=int(n),int(k)+1
    A.append(str(((n**2+3*n+2)*(k+1)/2)%1000000007))
 
for i in A:
    print(int(i))
