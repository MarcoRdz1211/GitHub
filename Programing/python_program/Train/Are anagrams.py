import time

t0 = time.time()

w1 = list(str(input()))
w2 = list(str(input()))

w1.sort(),w2.sort()

if w1==w2:
    print("YES")

else:
    print("NO")

print("---- %s seconds ---- " % (time.time()-t0))
