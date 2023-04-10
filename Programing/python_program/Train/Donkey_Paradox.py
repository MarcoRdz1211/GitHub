n,m = input().split()
n,m = int(m),int(n)

x1,y1 = input().split()
x2,y2 = input().split()

x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)

c = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        if (abs(x1-i)+abs(y1-j)==abs(x2-i)+abs(y2-j)):
            c += 1

print(c)
