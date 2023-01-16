# Escribe tu código aquí :-)
import random

num = random.randrange(0,10) # random.randrange(inicio, fin)
var = 0

numero = int(input("Escriba un numero entre 0 y 10. "))
while var == 0:
    if numero < num:
        print("El número del ordenador es más grande.")
        numero = int(input("Escriba un numero entre 0 y 10. "))

    elif numero > num:
        print("El número del ordenador es más pequeño.")
        numero = int(input("Escriba un numero entre 0 y 10. "))
    else:
        print("El número es igual.")
        var = 1


print("----------------------------------------------------------------")

'''
# OTRA POSIBILIDAD
num = random.randrange(0,10) # random.randrange(inicio, fin)

numero = int(input("Escriba un numero entre 0 y 10. "))

while numero != num:
    if numero < num:
        print("El número del ordenador es más grande.")
        numero = int(input("Escriba un numero entre 0 y 10. "))

    elif numero > num:
        print("El número del ordenador es más pequeño.")
        numero = int(input("Escriba un numero entre 0 y 10. "))

print("Los dos números son iguales.")
'''















