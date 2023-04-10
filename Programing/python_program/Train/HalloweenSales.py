p,d,m,s = map(int, input().split())
c = 0
k = (p-m)/d

if s>p:
    s -= p
    c += 1

while s-p>0:
    c += 1
    if p-d>m:
        p -= d
    elif p-d<m:
        p = m
    s -= p

print(c)
