n,t = input().split()

n,t = int(n),int(t)
X = list(map(int, input().split()))
A,s = [],0

for i in X:
    s += 2**i

mod = 2**t-1

while s not in A:
    A.append(s),A.append(mod-s),
    s = (2*s)%mod

count = int(len(A)/2-1)
if count==0:
    print(1)
else:
    print(count)
