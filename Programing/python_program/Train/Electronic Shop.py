b,n,m = input().split()
b,n,m = int(b),int(n),int(m)
A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxi = -1

for i in A:
    for j in B:
        if ((i+j)>=maxi and (i+j)<=b):
            maxi = i+j
            if (i+j)==b:
                break

print(maxi)
