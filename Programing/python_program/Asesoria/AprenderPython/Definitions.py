#Programa que calcula las raices cuadradas:
def root(a,b,c):
    while (b**2-4*a*c<0):
        print("El discriminante debe ser mayor a 0")
        a = float(input())
        b = float(input())
        c = float(input())

    #Formula de ecuación cuadratica:
    x1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)

#    print("Las raices de la ecuación: ",a,"x^2+",b,"x+",c," son: ",x1,x2,"")
    return x1,x2

def suma(a,b,c):
    return a+b+c

x1,x2 = root(1,10,25)
print(x1*x2)
print(suma(1,2,3))
