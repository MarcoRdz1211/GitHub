n,c = input().split()

t = int(input())
n,c = int(n),int(c)

trash = []
ans = []
for i in range(0,c):
    box.append([])
    trash.append([])

for i in range(0,t):
    A = list(input())
    if A[0]=="m":
        for i in range(int(A[1])-1,int(A[2])):
            box[A[3]-1].append(i)
    if A[0]=="b":
        trash(A[i]-1)=box(A[i]-1)
    if A[0]=="s":
        if ((A[1] and A[2]) in box) or ((A[1] and A[2]) in trash) or ((A[1] and A[2]) not in box): 
            Ans.append("si")
        else:
            Ans.append("Para que quieres saber eso")

for i in Ans:
    print(i)
