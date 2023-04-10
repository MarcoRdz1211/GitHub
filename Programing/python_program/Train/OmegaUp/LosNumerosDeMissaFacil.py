x,n = input().split()
x,A,n = int(x),list(str(x)),int(n)
s = 0

for i in A:
    s += int(i)**n

if (s==x):
    print("Simón Missa")

else:
    print("Nelpas Mijo")
