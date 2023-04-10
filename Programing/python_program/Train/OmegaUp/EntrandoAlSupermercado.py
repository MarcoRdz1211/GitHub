n,m = map(int, input().split())
ans,count = [],0

for i in range(0,n):
    x = int(input())

    if (x+count)>m:
        ans.append("espera")

    else:
        ans.append("pasa")
        count += x

for i in ans:
    print(i)
