n=int(input())
k=list(map(int, input().split()))
a=list(map(int, input().split()))
b=list(map(int, input().split()))

med=[]

for i in range(0,n):
	med.append(k[i])
	med.append(a[i])
	med.append(b[i])
	med.sort()
	if(i==n-1):
		print(int(med[1]))
	else:
		print(int(med[1]),end=" ")
	med=[]
