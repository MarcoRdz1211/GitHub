n,m = input().split()
A = list(input())
S = set(input())

B = []
for i in range(0,len(A)+len(S)):
    B.append(0)

for i in range(0,len(S)):
    for j in range(0,len(A)):
        if A[i]
