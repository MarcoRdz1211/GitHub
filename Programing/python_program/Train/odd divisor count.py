def divisor(a):
    count = 2
    
    for i in range(1,a+1):
        if a%i==0:
            count += 1
            
    return count

a,b = input().split()
a,b = int(a),int(b)

odds = 0

for i in range(a,b+1):
    if (divisor(i)%2==1):
        odds += 1

print(odds)
