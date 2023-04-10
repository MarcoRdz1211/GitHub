t,n = input().split()

n,t = long(n),long(t)
X = list(map(long,input().split()))
A,s = [],0

for i in X:
    s += 2**i

while s not in A:
    A.append(s)
    s = 2*s
    if s>2**n:
        s += 1-2**n

print(len(A)-1)
