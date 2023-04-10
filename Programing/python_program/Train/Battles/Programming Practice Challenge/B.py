n = int(input())
A = list(map(int, input().split()))
s,m = sum(A),n

for i in set(A):
    r = A.count(i)
    if (n-r < m) and (i*n > s):
        m = n-r

print(m)
