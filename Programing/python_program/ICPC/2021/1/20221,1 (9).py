n,p=input().split()
n,p=int(n),int(p)

S=[]
for i in range(0,n):
	s=int(input())
	S.append(s)

S.append(s+1)

P=list()
puntos=0
for i in range(0,n+1):
	if(S[n-1-i]==0):
		P.append(0)
	elif(S[n-1-i]<S[n-i]):
		q=puntos
		P.append(q)
	elif(S[n-1-i]==S[n-i]):
		p=-1
	else:
		puntos=puntos+1
		q=puntos
		P.append(q)

if(P[n-1]>p):
	print("ambiguous")
else:
	for i in range(0,n):
		if(i==n-1):
			print(P[n-1-i],end="")
		else:
			print(P[n-1-i])