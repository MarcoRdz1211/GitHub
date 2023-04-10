t = int(input())
A = []

for i in range(0,t):
    n = int(input())
    A.append(int(5*n/2))

for i in A:
    if i<15:
        print(15)
    else:
        if i%5 == 0:
            print(i)
        else:
            print(i+5-i%5)
