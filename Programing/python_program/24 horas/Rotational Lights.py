t,n = input().split()

n,t = int(n),int(t)
X = list(map(int,input().split()))
A,s = [],0

for i in X:
    s += 2**i

while s not in A:
    A.append(s+1)
    s = 2*s
    if s>(2**n):
        s = s%(2**n)
    print(s)

print(len(A)-2)
