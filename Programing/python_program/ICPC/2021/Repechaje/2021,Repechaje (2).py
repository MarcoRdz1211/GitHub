n = int(input())
A = []
lis = [0,2,6,9,13,16,20]

for i in range(0,n):
    x = str(input())
    ans = list([0,0,':',0,0,':',0,0])
    B = []
    while "*" in x:
        aux = x.index("*")
        B.append((aux-1)/2)        
        x = x.replace("*","",1)

    s = 0
    for j in B:
        if j in range(0,2):
            s = int(ans[0])+2**(1-j)
            ans[0] = int(s)

        if j in range(2,6):
            s = int(ans[1])+2**(5-j)
            ans[1] = int(s)

        if j in range(6,9):
            s = int(ans[3])+2**(8-j)
            ans[3] = int(s)

        if j in range(9,13):
            s = int(ans[4])+2**(12-j)
            ans[4] = int(s)

        if j in range(13,16):
            s = int(ans[6])+2**(15-j)
            ans[6] = int(s)

        if j in range(16,20):
            s = int(ans[7])+2**(19-j)
            ans[7] = int(s)

    A.append(''.join(map(str,ans)))

for i in range(0,n):
    print("Case {}: {}".format(i+1,A[i]))
