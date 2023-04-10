N = int(input())
A = list(map(int, str(N)))

count = 0

for i in set(A):
    if (i!=0):
        if (N%i==0):
            count += A.count(i)

print(count)
