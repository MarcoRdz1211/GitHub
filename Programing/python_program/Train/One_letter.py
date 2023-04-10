n = int(input())

s = []
for i in range(0,n):
    x = list(str(input()))
    x.sort()
    s.append(x[0])

s.sort()
r = ""
for i in s:
    r += i

print(r)
