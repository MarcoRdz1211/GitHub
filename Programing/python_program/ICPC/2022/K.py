n,k = map(int, input().split())
A = list(map(int, input().split()))

def minimun(A,s):
    mult = []

    for a in A:
        mult.append(s//a+1)

    print(mult)
    
    return mult

for i in range(0,n):
    s = int(input())
    taste = minimun(A,s)
    

#for a in Ans:
#    print(a)
