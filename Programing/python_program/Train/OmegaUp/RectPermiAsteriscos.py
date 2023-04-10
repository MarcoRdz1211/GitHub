h = int(input())
w = int(input())

print(w*"* ")

if h>1:
    for i in range(1,h-1):
        if w>1:
            print("* "+(w-2)*"  "+"*")
        else:
            print("*")

    print(w*"* ")
