def ceil(x):
    if int(x)==int(x+0.5):
        return int(x)
    else:
        return int(x+1)

def bitcount(x):
    bit = 0
    while x!=1:
        x = int(x/2)
        bit += 1

    return bit

x = int(input())
print(bitcount(x))
