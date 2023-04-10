#Listas y variables: in, and, or, is not, not in, is, not

A=[1,2,3,4,5,6,"hola"]

print(A)

print(2 in A)
print(10 in A)
print(A is A) #== es lo mismo a 'is'
print(2 is "2")
print(2 is not "2")
print(A is not A)

x= int(input("dame un numero "))

if (x+1==2) or (x==2) or (x>-10) and (type(x)==int):
     print(2)

if (x+1==3) and (x<10):
    print(3)
