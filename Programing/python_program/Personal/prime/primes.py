A = [2,3]
n = int(input("until what number do you want the primes? "))

for i in range(0,n):
    s = 1
    for j in A:
        s *= j
    A.append(s+1)

for i in range(0,len(A)):
    print("Prime_{}={}".format(i+1,A[i]))
