m,n=input().split()
m,n=int(m),int(n)

A=[]
for i in range(0,m):
	a=input()
	A.append(a)

B=[]
for i in range(0,n):
	b=input()
	B.append(b)

C=[]
for i in range(0,m):
	if(A[i]=="?"):
		for j in range(0,n):
			if(B[j]!="?"):
				print(i-j+1)
				exit()

for i in range(0,n):
	if(B[i]!="?"):
		for j in range(0,m):
			if(A[j]==B[i]):
				print(i)