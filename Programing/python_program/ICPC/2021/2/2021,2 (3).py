def prime(a):
    ans,count = "yes",0
    m = int(a**(1/2))
    for i in range(1,m+1):
        if a%i==0:
            count += 1

    if count != 1 or a == 1:
        ans = "no"
    
    return ans

n = int(input())
count = []

for i in range(0,n):    
    a,b = list(map(int,input().split()))
    s = 0
    for i in range(a,b+1):
        if i>2 and i%2!=0:
            if prime(i)=="yes":
                s += 1
    
    count.append(s)

for i in count:
    print(i)
