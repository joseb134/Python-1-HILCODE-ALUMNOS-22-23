'''
Una vez hecha la caja con tamaño fijo, trabajaremos para que el tamaño de ésta
pueda ajustarse según las necesidades del proyecto.

Para hacerlo necesitaremos tener buen dominio sobre el uso de bucles, condicionales y
variables de tipo caracter. Se recomienda también el uso de variables para indicar
las dimensiones de la caja (altura y longitud).
'''

MAX_HORIZONTAL = 25
MAX_VERTICAL = 5

nombre = input("¿Cuál es tu nombre? ")
saludo = f"Hola, {nombre}."

tam = len(saludo)
espacios = (MAX_HORIZONTAL-tam)
mitad = espacios//2

linea_superior = " " + MAX_HORIZONTAL*"_"
linea_inferior = "|" + MAX_HORIZONTAL*"_" + "|"
linea_vacia = "|" + MAX_HORIZONTAL*" " + "|"
mensaje = "|" + mitad*" " + saludo + (mitad)*" " + "|"

if espacios%2 == 1:
    mensaje = "|" + mitad*" " + saludo + (mitad+1)*" " + "|"

for linea in range(-1,MAX_VERTICAL):
    if linea == -1:
        print(linea_superior)
    elif linea == MAX_VERTICAL - 1:
        print(linea_inferior)
    elif linea+1 == MAX_VERTICAL//2 and MAX_VERTICAL%2==0:
        print(mensaje)
    elif linea == MAX_VERTICAL//2 and MAX_VERTICAL%2==1:
        print(mensaje)
    else:
        print(linea_vacia)


