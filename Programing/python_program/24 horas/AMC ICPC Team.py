T = int(input())
S = []

for i in range(0,T):
    M,N,K = input().split()
    M,N,K = int(M),int(N),int(K)
    A = []

    for j in range(0,M):
        a = int(input())
        A.append(a)

    A.sort()
    for j in range(0,K):
        A[j] = N-A[j]

    S.append(sum(A))

for i in S:
    print(i)
