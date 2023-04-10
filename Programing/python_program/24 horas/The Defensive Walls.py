import matplotlib.pyplot as plt

n = int(input())
A = [[],[]]

for i in range(0,n):
    x1,y1,x2,y2 = input().split()
    A[0].append(int(x1)),A[0].append(int(x2))
    A[1].append(int(y1)),A[1].append(int(y2))
    
for i in A:
    print(i)

plt.plot(A[0],A[1])

plt.show()
