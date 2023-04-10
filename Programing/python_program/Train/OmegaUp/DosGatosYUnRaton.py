a,b,c = map(int, input().split())

d1 = abs(c-a)
d2 = abs(c-b)

if (d1<d2):
    print("gato A")

elif (d2<d1):
    print("gato B")

else:
    print("raton C")
