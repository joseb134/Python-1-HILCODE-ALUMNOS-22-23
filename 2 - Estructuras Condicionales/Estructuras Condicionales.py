# Escribe tu código aquí :-)ç

'''
Condicionales:

    < Menor que
    > Mayor que

    == Igualdad
    !=  Diferente

    >= Mayor igual que
    <= Menor igual que
'''

numero = int(input("Escribe un numero: "))

if numero < 10:
    print("El numero es menor que diez.")

else:
    print("El numero es mayor o igual que diez.")

###############################################################
compras = ["Manzana", "Sandía", "Plátano", "Galleta", "Pasta", "Naranja", "Huevos"]

print(compras[2])

if compras[1] == "Manzana":
    print("La posición uno es la manzana.")

else:
    print("La posición uno no es la manzana.")

###############################################################

# conector and
numero = 15
if numero > 0 and numero < 10:
    print("El número está entre cero y diez.")
else:
    print("El número NO está entre cero y diez.")

# conector or
numero = 15
if numero > 0 or numero < 10:
    print("El número está entre cero y diez.")
else:
    print("El número NO está entre cero y diez.")

###############################################################

# compras = ["Manzana", "Sandía", "Plátano", "Galleta", "Pasta", "Naranja", "Huevos"]

compras = ["Manzana", "Sandía", "Plátano"]

iten = input("Escribe algún iten de la compra: ")

# OR // AND
if iten == compras[0] or iten == compras[1] or iten == compras[2]:
    print("El iten está en la lista de compras")
else:
    print("El iten NO está en la lista de compras")

###############################################################

if iten == compras[0]:
    print("El iten está en la lista de compras")

elif iten == compras[1]:
    print("El iten está en la lista de compras")

elif iten == compras[2]:
    print("El iten NO está en la lista de compras")

else:
    print("El iten NO está en la lista de compras")

###############################################################

numero = 0

while numero != 11:
    print(numero, "es diferente de 11.")
    numero = numero + 1






