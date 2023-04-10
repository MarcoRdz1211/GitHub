r = int(input())
n = int(input())
X,Y = [0],[0]
maxcount = 0

for i in range(0,n):
    x1,y1 = input().split()
    X.append(int(x1)),Y.append(int(y1))

for i in range(0,n+1):
    count = 0
    for j in range(1,n+1):
        if ((X[i]-X[j])**2+(Y[i]-Y[j])**2<r**2):
            count += 1

    if (count>maxcount):
        maxcount = count

print(count)
