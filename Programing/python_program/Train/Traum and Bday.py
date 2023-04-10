n = int(input())
A = []

for i in range(0,n):
    gift = list(map(int, input().split()))
    price = list(map(int, input().split()))

    if price[0]>price[1]:
        b,w = gift[0],gift[1]
        bc,wc,z = price[0],price[1],price[2]
    else:
        b,w = gift[1],gift[0]
        bc,wc,z = price[1],price[0],price[2]
        
    s0 = b*bc+w*wc
    s = bc-wc

    if wc+z>=bc:
        A.append(s0)
    else:
        A.append((w+b)*wc+b*z)


for i in A:
    print(i)
