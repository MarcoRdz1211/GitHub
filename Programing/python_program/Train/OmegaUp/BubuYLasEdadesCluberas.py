A = list(map(int, input().split()))
A = sorted(set(A),reverse=True)
B = []

for i in A:
    B.append(str(i))

print(B)
