R,C,E = 1,1,1

while [R,C,E] != [0,0,0]:
    R,C,E = map(int, input().split())
    A = []

    for j in range(0,R):
        x = list(input())
        A.append(x)

    AUX = [()]
    
