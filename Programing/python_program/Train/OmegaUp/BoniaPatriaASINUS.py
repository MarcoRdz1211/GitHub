n = int(input())

if (n in range(1,40)):
    val,ans = 0,0

    for i in range(1,n+1):
        x = int(input())

        if (x>val):
            val,ans = x,i

    print(ans)

else:
    print("ERROR")
