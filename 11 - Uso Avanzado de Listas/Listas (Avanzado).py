import random

# añadir elementos a una lista
numeros = []
print(numeros)
numeros.append(10)
print(numeros)
numeros.append(15)
print(numeros)

# añadir varios elementos a una lista de forma automática
numeros = []
for i in range(0,51):
    numeros.append(i)
print(numeros)

# añadir elementos a una lista usando inputs del teclado
numeros = []
for i in range(0,5):
    num = int(input("NUM: "))
    numeros.append(num)
print(numeros)

# enseñar/usar cada elemento de manera individual
tam = len(numeros)
for i in range(tam):
    print(numeros[i])

# comando .pop() -> elimina el último elemento de la lista
# este comando posibilita guardar el elemento eliminado en una variable
print(numeros)
num = numeros.pop() # elimina el último elemento de la lista "numeros" y lo guarda en "num"
print(numeros)
print(num)

# comando .remove(x) -> elimina el elemento cuyo VALOR sea "x" de la lista
# NO posibilita guardar ese valor como el .pop()
print(numeros)
numeros.remove(2) # elimina el elemento cuyo valor sea igual a 2. Si hay más de uno, eliminará solo el primero que aparezca
print(numeros)    # si no hay ningún elemento cuyo valor sea 2, el programa devolve un error

# comando .pop(x) -> elimina el elemento en la POSICIÓN de INDEX "x"
print(numeros)
num = numeros.pop(2) # elimina el elemento ubicado en el index 2 de la lista, lo guarda en "num"
print(numeros)
print(num)

# generar vários numeros aleatorios y guardarlos en una lista
numeros = []
for i in range(0,50):
    num = random.randint(0,10)
    numeros.append(num)
print(numeros)

# comando .count(x) -> cuenta el número de veces que el elemento "x" aparece en la lista
cantidad_ceros = numeros.count(0) # cuenta la cantidad de ceros y lo guarda en la variable
print(cantidad_ceros)

# elimina todos los elementos con un valor especifico, va enlazado con la parte de contar la cantidad
for i in range(cantidad_ceros):
    numeros.remove(0)

# otra manera de eliminar todos los elementos con un determinado valor dentro de la lista
while 0 in numeros:
    numeros.remove(0)
print(numeros)

# generar vários numeros aleatorios y guardarlos en una lista
numeros = []
for i in range(0,10):
    num = random.randint(-80,80)
    numeros.append(num)
print(numeros)

# sumar todos los elementos de la lista sin usar comandos
suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]
print(suma)

# comando sum(lista) -> suma todos los elementos de la lista y los guarda en una variable
suma = sum(numeros)

# identificar el mayor elemento de la lista sin usar comandos
mayor = numeros[0]
for i in range(len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]
print(mayor)

# identificar el menor elemento de la lista sin usar comandos
menor = numeros[0]
for i in range(len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]
print(menor)

# comando max(lista) -> devuelve el elemento de mayor valor en la lista y lo guarda en una variable
# comando min(lista) -> devuelve el elemento de menor valor en la lista y lo guarda en una variable
mayor = max(numeros)
menor = min(numeros)
print(mayor)
print(menor)

# bucles for anidados
for i in range(0,5):
    for j in range(0,3):
        print("FOR J:", j)
    print("FOR I:", i)

# ordenar los elementos de una lista en orden creciente sin usar comandos
for i in range(0,len(numeros)):
    for j in range(0,len(numeros)):
        if numeros[i] < numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print("Creciente:", numeros)

# ordenar los elementos de una lista en orden decreciente sin usar comandos
for i in range(0,len(numeros)):
    for j in range(0,len(numeros)):
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux
print("Decreciente:", numeros)

# comando .sort() -> pone los elementos de la lista en orden creciente
numeros.sort()
print(numeros)

# comando .sort(reverse = True) -> pone los elementos de la lista en orden decreciente
numeros.sort(reverse=True)
print(numeros)
