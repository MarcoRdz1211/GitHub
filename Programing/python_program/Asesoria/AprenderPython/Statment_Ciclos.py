#Statments ciclos: for and while

#For simple
for i in range(-10,11):
    print(i)

print("------------------------------")

#For con arrreglos
A=[2,4,5,6,10]

for i in A:
    x = i**2
    print(i,"^2=",x)
    print("Sigue el programa")

print("Finalizo el programa")

print("------------------------------")

#While simple

i = 1.5

while i<10:
    print(i)
    
    i += 1

print("------------------------------")

A=[2,4,5,6,10,"3",3.23123,3.1416]

for i in A:

    if (type(i)==int):
        continue
    
    print(i**2)
        


