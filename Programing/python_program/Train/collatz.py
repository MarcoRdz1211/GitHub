import time
def collatz(n):
    if n%2==0:
        n /= 2
    else:
        n = 3*n+1

    return n

n = int(input())
start_time = time.time()
count = 1
while collatz(n)!=1:
    n = collatz(n)
    count += 1

print(count)
print("--- %s seconds ---" % (time.time() - start_time))
