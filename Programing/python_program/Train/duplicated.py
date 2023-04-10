k = int(input())
A = list(map(int, input().split()))

ans,i = "False",0

while i<=len(A)-k:
    for j in range(i+1,i+k):
        if A[i] == A[j]:
            ans,i = "True",len(A)+2
            break
    i += 1

print(ans)
            
