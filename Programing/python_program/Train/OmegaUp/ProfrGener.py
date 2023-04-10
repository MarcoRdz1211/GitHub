n = int(input())
A = list(map(int, input().split()))
h,m = 0,0

for i in A:
    if (i%2==0):
        h += 1

    else:
        m += 1

print(h,m)
