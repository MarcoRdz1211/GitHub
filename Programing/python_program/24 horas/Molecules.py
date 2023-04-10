n = int(input())

def molecules(x,y,z):
    a = (x-4*y+2*z)/4
    b = (-x+2*z)/4
    c = (x+4*y-2*z)/24
    return a,b,c

A = []
for i in range(0,n):
    x,y,z = input().split()
    x,y,z = int(x),int(y),int(z)

    x,y,z = molecules(x,y,z)
    print(x,y,z)
