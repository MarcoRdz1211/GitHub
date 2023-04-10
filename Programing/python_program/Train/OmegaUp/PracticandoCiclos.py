n,a,b = map(int, input().split())
s = 0

if (n%2==0):
    s = a*(a+1)/2

else:
    s = b*(b+1)/2

print(s)
