n = int(input())
A = []

for i in range(0,n):
    t,d = map(int, input().split())
    A.append([t,d])

velmax = 0

for i in range(0,n-1):
    x = (A[i+1][1]-A[i][1])/(A[i+1][0]-A[i][0])
    if (x>velmax):
        velmax = x

print(int(velmax))
