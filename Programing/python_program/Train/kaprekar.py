x_min,x_max = map(int, input().split())
s = 0

for i in range(x_min,x_max+1):
    n = i**2
    print(n)
    l = len(str(n))
    z = 0
    for j in range(1,l):
        a,b = int(n/10**j),n%(10**(j))
        if a+b==i:
            print(i)
            s += 1
            break

    input()

if s==0:
    print("INVALID RANGe")
else:
    print(s)
