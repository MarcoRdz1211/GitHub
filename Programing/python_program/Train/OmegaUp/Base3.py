n = int(input())
A,ans = [],""

while (n>0):
    x = n%3
    A.append(x)

    n = int((n-x)/3)

k = len(A)

for i in range(0,k):
    ans += str(A[k-i-1])
    
print(ans)
