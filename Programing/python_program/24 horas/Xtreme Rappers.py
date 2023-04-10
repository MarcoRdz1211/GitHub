k,j = input().split()
count = 0

while (k>0 and j>0):
    if k>=j and k!=1:
        k,j,count += -2,-1,1
    elif k<j:
        k,j,count += -1,-2,1
    else:
        break

print(count)
