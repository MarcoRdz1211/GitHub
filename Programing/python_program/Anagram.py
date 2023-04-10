n = int(input())
A = []

for i in range(0,n):
    x = input()
    A.append(x)

A = sorted(A)

count = 0
count_max = 0

print(A)

for i in range(0,n-1):
    print(sorted(A[i]),sorted(A[i+1]))
    if  sorted(A[i])==sorted(A[i+1]):
        count += 1

    else:
        count = 0

    if count>count_max:
        count_max = count

    
print(count_max)
