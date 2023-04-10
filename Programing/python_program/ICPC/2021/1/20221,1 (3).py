n = int(input())
A,B = [],[]
s = ["A","B","C","D","E","F"]
result = ""

for i in range(0,n):
    A.append(list(map(int, input().split())))
    A[i].pop(0)
    for j in A[i]:
        B.append(j)

B,count = sorted(B),len(B)


for i in range(0,count):
    for j in range(0,n):
        if (B[i] in A[j]):
            result += s[j]
            break

print(result)
