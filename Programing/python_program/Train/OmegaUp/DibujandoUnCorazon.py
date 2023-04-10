s = str(input())
A = []

for i in range(0,4):
    A.append((3-i)*" "+(6+2*i)*s+(6-2*i)*" "+(5+2*i)*s)

for i in range(0,12):
    A.append(i*" "+(23-2*i)*s)

for i in A:
    print(i)
