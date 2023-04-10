A = list(str(input()))
s,n = 0,len(A)

for i in range(0,n):
    x = abs(ord(A[i])-ord(A[n-i-1]))
    if (x==0) or (x==32):
        s += 1

print(s)
