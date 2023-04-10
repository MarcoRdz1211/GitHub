def factorial(n):
    s = 1
    for i in range(1,n+1):
        s *= i

    return s

f = open("taste.txt","w")

f.write("Numbers "," Factorial \n")

for i in range(0,100):
    f.write(str(i),str(factorial(i)),"\n")

f.close()
