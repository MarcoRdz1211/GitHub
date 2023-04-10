n = int(input())
A = list(map(int, input().split()))
B = sorted(set(A))

for i in B:
    print(i,A.count(i))
    
