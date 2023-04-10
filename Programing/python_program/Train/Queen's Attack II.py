n,k = input().split()
x0,y0 = input().split()

n,k,x0,y0 = int(n),int(k),int(x0),int(y0)

count= 2*(n-1)+min(x0-1,y0-1)+min(x0-1,n-y0)+min(n-x0,y0-1)+min(n-x0,n-y0)

print(count)

