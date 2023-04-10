n = int(input("Until what number do you wanna taste? "))
A = [[0],[0]]

def collatz(n):
    if n%2==0:
        n /= 2
    else:
        n = 3*n+1

    return n

for i in range(1,n):
    r = i
    count = 0
    B = []
    while r!=1:
        if r in A:
            count += A[1][r]
            r = 1
        else:
            A[0].append(r)
            B.append(count-1)
            count += 1
            r = collatz(r)

    A[1].append(count)

for i in range(0,len(A)):
    print(A[0][i],A[1][i])
