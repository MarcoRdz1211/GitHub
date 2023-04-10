y,n = map(int, input().split())

x = list(map(int, input().split()))

solutions = []

for i in range(0,n):
  a,p,f = map(int, input().split())
  ans,s = 0,0

  if x[a-1]>=p:
    s = 0
  else:
    for j in range(a,a+f):
      if x[j]>=p:
        s +=1

  solutions.append(s)

  
for i in solutions:
  print(i)
