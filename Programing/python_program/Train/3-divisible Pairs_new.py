n = int(input())
A = list(map(int, input().split()))
count = [0,0,0]

for i in range(0,len(A)):
    if (A[i]%3==0):
        count[0] += 1
    elif (A[i]%3==1):
        count[1] += 1
    else:
        count[2] += 1

s = count[0]*(count[0]-1)/2 + count[1]*count[2]

print(int(s))
