import time

t0 = time.time()

A = list(input())
B = list("abcdefghijklmnopqrstuvwxyz")
s = "YES"

for i in B:
    if A.count(i)==0:
        print("0")
        s = "NO"
        break

print(s)
print(time.time()-t0)
