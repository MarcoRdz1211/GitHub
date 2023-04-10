N,CB,CP = input().split()
N,CB,CP = int(N),int(CB),int(CP)
x,y = 0,0

for i in range(0,N):
    a,b = input().split()
    x += int(a)
    y += int(b)

def ceil(x):
    if int(x)!=x:
        return int(x+1)
    else:
        return int(x)

cost = CB*ceil(x/10)+CP*ceil(y/10)
print(cost)
