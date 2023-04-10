n = int(input())
A = list(map(int, input().split()))
a0 = int(input())
s,count = 0,0

for i in A:
    s += i
    if (s==a0):
        count += 1

print(count)
