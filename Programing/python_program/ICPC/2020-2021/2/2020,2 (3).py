n,a,b = input().split()

n,a,b = int(n),int(a),int(b)

if a!=b:
    k = 2*n/(b*(b+1)-a*(a-1))*(b+1-a)+1/(b+1-a)

else:
    k = n/b

print(k)
