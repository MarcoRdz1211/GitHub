n = int(input())
A = list(map(int, input().split()))
k = int(input())
L = []

for i in A:
    if (i%k == 0):
        L.append(i)
    else:
        L.append("X")

print(*L)
