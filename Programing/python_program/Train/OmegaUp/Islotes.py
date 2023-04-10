A = list(str(input()))
n,count = len(A),0

for i in range(1,n-1):
    if (A[i-1]==A[i+1]) and (A[i]!=A[i+1]):
        count += 1

print(count)
