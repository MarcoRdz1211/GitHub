n = int(input())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

dif  = abs(min(A)-min(B))

for i in A:
    for j in B:
        if (abs(i-j)<dif):
            dif = abs(i-j)

        if dif==0:
            break

print(dif)
