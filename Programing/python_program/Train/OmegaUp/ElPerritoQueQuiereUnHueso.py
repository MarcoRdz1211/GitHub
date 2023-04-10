a1,b1 = map(int, input().split())
a2,b2 = map(int, input().split())

if (a1>a2) and (b1>b2):
    print("Hueso 1")
elif (a1<a2) and (b1<b2):
    print("Hueso 2")
else:
    print("Perrito confundido :(")
