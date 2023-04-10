A = list(input().split())
n = len(A)

if ord(A[0][0])<=97:
  s,r = list(A[0]),""
  s[0] = chr(ord(A[0][0])+32)
  for i in s:
    r += i
  
A[0] = r

for i in range(0,n):
  if (i%2==1):
      s,r = list(A[i]),""

      for j in s:
          r += chr(ord(j)-32)

      A[i] = r

print(*A)
