t = int(input())
ans = []

for i in range(0,t):
    n,a,b = input().split()
    n,a,b = int(n),int(a),int(b)
    S = {n}
    Sn = {n}
    Sb = {}

    while (1 not in S) or (Sn!=Sb):
        Sb = Sn.copy()
        for i in S:
            if i/a==int(i/a):
                Sn.add(i/a)
            if i-b>0:
                Sn.add(i-b)
        print(Sn)

        S.update(Sn)

    print(S,Sb,Sn)
    if (1 in S):
        ans.append("Yes")
    else:
        ans.append("No")

for i in ans:
    print(i)
