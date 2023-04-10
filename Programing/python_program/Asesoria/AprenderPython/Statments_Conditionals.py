#Statments condicionales: if and else
x = int(input("dame un numero "))
y = int(input("dame otro numero "))

if (x==y):
    print(x)

elif (x==y+1):
    print(y)

else:
    print(0)


if (x%2==0):
    print(x,"es un numero par")

else:
    print(x,"es un numero impar")
