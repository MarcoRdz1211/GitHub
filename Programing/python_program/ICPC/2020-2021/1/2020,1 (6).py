n = int(input())

Arr = ".#$%/(&)"
Brr = "0123456789"

C,L = ["Strong","Good","Weak","Rejected"],[]

for i in range(0,n):
    s = 0
    r = str(input())
    A = list(r)
    if len(r)>=10:
        s += 1
    if any (j in r for j in r.lower()):
        s += 1
    if any (j in r for j in r.upper()):
        s += 1
    if any (j in r for j in Arr):
        s += 1
    if any (j in r for j in Brr):
        s += 1
        for j in range(0,len(r)):
            if type(r[j])==int and j<len(r):
                if type(r[j+1])==int:
                    s -= 1
                    break

    L.append(s)

count = 0
for i in L:
    count += 1
    if i>2:
        print("Assertion number #{}: {}".format(count,C[5-i]))
    else:
        print("Assertion number #{}: {}".format(count,C[5-2]))
