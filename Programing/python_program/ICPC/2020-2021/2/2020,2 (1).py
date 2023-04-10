n = int(input())

m,s = 100,100

for i in range(0,n):
    x = int(input())
    s += x
    if s>m:
        m = s

print(m)
