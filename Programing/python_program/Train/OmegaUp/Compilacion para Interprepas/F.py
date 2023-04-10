n = int(input())
A = list(map(int, input().split()))
q = int(input())
B = list(map(int, input().split()))
ans = []

for i in B:
    count = 0
    while i in A:
        A.remove(i)
        count += 1
        
    ans.append(count)

for i in ans:
    print(i)
