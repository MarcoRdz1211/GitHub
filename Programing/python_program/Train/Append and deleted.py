A = list(input())
B = list(input())
k = int(input())

n = 0

while (n<len(A) and n<len(B)):
    if (A[n]!=B[n]):
        break
    else:
        n += 1

if (len(B)+len(A)-2*n>k):
    print("No")

else:
    print("Yes")
