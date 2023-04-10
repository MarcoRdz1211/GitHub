n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
s = 0

for i in range(0,n):
    s += A[i]*B[i]

print(s)
