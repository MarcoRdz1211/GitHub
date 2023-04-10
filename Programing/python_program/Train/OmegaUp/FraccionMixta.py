n,m = map(int, input().split())

if (n%m!=0):
    print("{} {}/{}".format(n//m,n%m,m))

else:
    print("{}".format(n//m))
