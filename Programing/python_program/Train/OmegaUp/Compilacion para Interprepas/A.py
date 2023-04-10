k,n,w = map(int, input().split())

s = int(w*(w+1)*k/2)
if s<n:
    print(0)
else:
    print(s-n)
