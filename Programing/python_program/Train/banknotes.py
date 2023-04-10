a,b,s,n = input().split()
a,b,s,n = int(a),int(b),int(s),int(n)

x,y = (n*b-s)/(b-a),(s-a*n)/(b-a)

if (x>=0 and y>=0):
    print(int(x))
else:
    print(-1)
