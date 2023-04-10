n = int(input())
ans = ""

for i in range(0,n):
    x = input()
    A = sorted(x)
    ans += A[0]

print("".join(sorted(ans)))
