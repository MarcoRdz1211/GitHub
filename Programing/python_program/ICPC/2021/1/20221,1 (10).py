n=int(input())
W=list(map(int, input().split()))

tot=0
for i in range(0,n):
	tot=tot+W[i]

if(tot%3==0):
	print("yes")
else:
	print("no")