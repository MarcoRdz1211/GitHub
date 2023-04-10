n = int(input())

if n>=1918:
    if (n%4==0 and n%100!=0) or (n%400==0):
        d = 1
    else:
        d = 0
else:
    if (n%4==0 ):
        d = 1
    else:
        d = 0

print("{}.09.{}".format(13-d,n))
