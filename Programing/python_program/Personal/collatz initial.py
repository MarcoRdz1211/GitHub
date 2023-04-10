n = int(input(""))

def collatz(n):
    if n%2==0:
        n /= 2
    else:
        n = 3*n+1

    return n

print(collatz(n))
