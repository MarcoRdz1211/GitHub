#Listas:
A = [1,2,3,"hola mundo",True,False,4,5,6,"Adios mundo",100,100,100]
copiaA = A.copy() #A.copy(), crea una copia del arreglo A

print(len(A)) #Imprimir cantidad de elementos en el arreglo

print(A[1],A[-2]) #Imprimir el segundo y penultimo elemento del arreglo

print(A)
A.append(False) #A.append(x), agregar al final del arreglo el elemento x
print(A)
A.remove("hola mundo") #A.remove(x), elimiar el elemento llamado: x
print(A)
A.pop(5) #A.pop(i), Eliminar elementos en el espacio i
print(A)
A[7] = 100 #A[i]=x, cambiar el elemento i del arreglo por el elemento x
print(A)
A[3] = False
print(A)

n100 = 0
for i in range(0,len(A)):
    if A[i]==100:
        n100 = i
        break

print(n100)

print(A.index(100,0,11)) #A.index(x,a,b), da el lugar del primer elemento x en el intervalo[a,b]

print("-------------------------------------")

#Funciones de las listas: copy, clear, count, sum, sort, reverse,insert
print(A)
print(copiaA)

copiaA.clear() #A.clear(), elimina todos los elementos de un arreglo
print(copiaA)

cantidad100 = A.count(100) #A.count(x), regresa la cantidad de elementos x en el arreglo
print(cantidad100)

C = [1,-10,15,32.2,2.5,-1000]
print(sum(C))   #sum(X), suma todos los elementos del arreglo numerico
promedio = sum(C)/len(C) #Calculo del promedio de un arreglo numerico
print(promedio)

print(C)
C.sort(reverse=True) #C.sort(reverse=True or False), ordenar mi arreglo numerico.
print(C)

C.insert(3,"hola mundo") #C.insert(i,x), inserta el elemento x en el lugar i
print(C)

LISTANUEVA = A+C #A+B, combina las listas A y B
print(LISTANUEVA)

print("-------------------------------------")

#Creacion de listas: B=[1,2,3,4,5,...,100]
B = []

for i in range(1,101):
    B.append(i**(1/2)+1)

C = []

for i in B:
    C.append((i-1)**2)

print(B)
print("-------------------------------------")
print(C)

print("-------------------------------------")
print(set(C)) #Crear conjuntos de datos no repetidos.

print("-------------------------------------")

#Creacion de matrices: B=[1,2,3,4,5,...,100]

X=[
    [1,2,3,5,6,7],
    [4,5],
    [7],
    [],
    [13,14,15,1,2,3,4,5]] #En python, las matrices son listas de listas, y no tienen que tener los mismos elementos cada una.

for i in X:
    print(i)
