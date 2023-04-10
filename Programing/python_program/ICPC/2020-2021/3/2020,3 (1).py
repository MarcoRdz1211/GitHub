T,P = input().split()
T,P = int(T),int(P)

E = list(map(int, input().split()))
D = list(map(int, input().split()))
S = list(map(int, input().split()))

score,k = 0,0

for i in range(0,T):
    for j in range(k,P):
        if E[i]>=D[j]:
            E[i] = E[i]-D[j]
            score += S[j]
            k += 1
        else:
            break

print(score)
