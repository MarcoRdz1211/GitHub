import random

n = random.randint(1,1000)
A = []

for i in range(1,n+1):
    if (i%3==0) and (i%5!=0):
        A.append("Fizz")

    elif (i%3!=0) and (i%5==0):
        A.append("Buzz")

    elif (i%3==0) and (i%5==0):
        A.append("FizzBuzz")

    else:
        A.append(i)

for i in A:
    print(i)
