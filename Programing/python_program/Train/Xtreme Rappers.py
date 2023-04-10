import math

k,j = input().split()
k,j = int(k),int(j)
count = 0

if j>0 and k>0:
    count = math.floor(k/3+j/3)

print(count)
