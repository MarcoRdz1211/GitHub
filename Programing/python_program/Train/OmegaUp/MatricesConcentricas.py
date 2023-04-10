n = int(input())
A = []

for i in range(0,n):
    B = list(map(int, input().split()))
    A.append(B)

for i in A:
    print(*i)
