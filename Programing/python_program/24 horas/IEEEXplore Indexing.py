def multi_input():
    try:
        while True:
            data=input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return
    
A = input().split(";")
B = input().split(";")
C = list(multi_input())

print(A)
print(B)
print(C)

for i in range(0,len(C)):
    X,a,b = list(C[i]),0,0

    for j in range(0,len(X)):
        if X[j]=="<":
            a=j
        elif X[j]==">":
            b=j

    for j in range(a,b):
        X.pop(a)

    if X[a]==">":
        X.pop(a)
        
    s = ""
    for j in range(0,len(X)):
        s += X[j]

    C[i]=s

for i in range(0,len(C)):
    input()
    for j in ["!",",",".","?"]:
        C[i].replace(j,"")
