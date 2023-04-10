n = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(0,n):
    for j in range(i+1,n):
        if (A[i]+A[j])%3==0:
            count += 1

print(count)
