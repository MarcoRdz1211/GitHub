G,T = 1024,1024**2
n,data = input().split()
n = int(n)

if data[len(data)-1]=="G":
    count = int(data[:len(data)-1])*G

else:
    count = int(data[:len(data)]-1)*T

A = list(map(int, input().split()))

maxi,num = 0,0

for i in range(0,len(A)):
    suma,j = count,i

    while count>0 and j<len(A):
        suma -= A[j]
        j += 1

    R = max(maxi,j-i)
    if R!=maxi:
        L = j+1

print(R,L)
