A = []
r = int(input())

while (r!=0):
    s = r*(r+1)/2

    if (s%r==0):
        A.append("SI")

    else:
        A.append("NO")

    r = int(input())

for i in A:
    print(i)
