A = list(map(int,input().split()))
B = []
Array = [["hole in one","condor","albatross","eagle","birdie","par","bogey","double bogey","triple bogey"],
         [1,-4,-3,-2,-1,0,1,2,3]]

for i in range(0,18):
    B.append(str(input()))

s = 0
for i in range(0,18):
    if B[i]==Array[0][0]:
        s += 1
    else:
        s += A[i]+Array[1][Array[0].index(B[i])]

print(s)
