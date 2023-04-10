T = int(input())

solutions = []

for i in range(T):
  a = input().split()
  C = int(a[0])
  R = int(a[1])
  S = int(a[2])

  M = C//S
  if R == 0 and C%S != 0:
    M += 1
  b = (C - R*(S-1))
  if b >= 0:
    m = b//S
    if b%S != 0:
      m += 1
  else: m = 0

  solutions.append((M,m))

for sol in solutions:
  print(sol[0],sol[1])