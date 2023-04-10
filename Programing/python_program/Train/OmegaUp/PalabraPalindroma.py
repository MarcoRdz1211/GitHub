A = list(str(input()))
ans,n = "SI",len(A)

for i in range(0,n//2+1):
    if (A[i]!=A[n-i-1]):
        ans = "NO"
        break

print(ans)
