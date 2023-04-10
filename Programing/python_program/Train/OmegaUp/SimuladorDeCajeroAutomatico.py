A,C,s = [""],[],1000

while  (A[0]!="S"):
    A = input().split()
    if len(A)>1:
        A[1] = int(A[1])
    if A[0]=="C":
        C.append(s)
    elif A[0]=="D":
        s += A[1]
    elif A[0]=="R":
        s -= A[1]

for i in C:
    print("${}".format(i))
