a,b = map(int, input().split())

if (a+b==5):
    b += 3
    print(2*a+b)

else:
    a -= 1
    
    if ((7*a+b)%2==0):
        print(a-b)

    else:
        print(a*b)
