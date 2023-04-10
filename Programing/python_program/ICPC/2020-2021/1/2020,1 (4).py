t = int(input())

A = []

for i in range(0,t):
    n = int(input())
    s,r = 0,0
    B = list(map(int,input().split()))
    for i in range(0,n):
        if i%2==0:
            s += B[i]
        if i%2==1:
            r += B[i]

    if r>s:
        print(r)
    else:
        print(s)
