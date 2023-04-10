n = int(input())
A = list(map(int, input().split()))
count = 0

for i in range(0,n):
    B = []
    for j in range(i,n):
        if (A[j] not in B):
            B.append(A[j])
            count += 1

        else:
            break

print(count)
