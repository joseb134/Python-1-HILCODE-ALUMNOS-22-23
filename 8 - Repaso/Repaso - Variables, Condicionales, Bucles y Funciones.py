# 1 - Variables

# Crear y definir variables
nombre = "Clóvis Magno"
edad = 25
altura = 1.80

# Entradas por teclado
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
altura = float(input("¿Cuál es tu altura? "))

# Enseñando valores en pantalla
print("El nombre es " + nombre)  #solo funciona para variables de tipo string (tipo texto) 
print("El nombre es", nombre)
print("El nombre es", nombre,"la edad es", edad,"la altura es", altura,".")
print(f"El nombre es {nombre} la edad es {edad} y la altura es {altura}.")
print("El nombre es {} la edad es {} y la altura es {}!".format(nombre, edad, altura))

#################################################################################
# 2 - Condicionales

temperatura = float(input("Cuál la temperatura? "))

if temperatura > 37.5:
    print("Tienes fiebre.")
else:
    print("No tienes fiebre.")

'''
SÓLIDO: MENOS QUE 0ºC
LÍQUIDO: 0ºC HASTA 100ºC
GASEOSO: MÁS QUE 100ºC
'''

temperatura_agua = float(input("¿Cuál la temperatura del agua? "))

if temperatura_agua < 0:
    print("El agua está en estado sólido.")
elif temperatura_agua >= 0 and temperatura_agua < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso.")

'''
Otra manera de hacer lo mismo seria usando dos elif
Es importante recordar que los elif y los else solo se ejecutan si todas las
condiciones anteriores a éstos son falsas. Si hay una que sea verdadera, todos los elif
y los else que estén por debajo serán ignorados en la ejecución. Así, usar elif y else es
una manera de asegurarnos que solo una opción se ejecutará cuando así se desea o sea necesário.

En la opción abajo, por ejemplo, no hace falta usar un condicional compuesto como antes en la
segunda condición, ya que si temperatura_agua > 100, el if se ejecuta, y todo lo de abajo
será ignorado. Entonces, aunque una temperatura mayor que 100 sea también mayor que 0, usando los
elif ahorramos el uso de condicionales como 'temperatura_agua > 0 and temperatura_agua < 100', ya que si 
el programa llega en este bloque esto indicaría que el primer if es falso, por lo cual, la temperatura
ya es menor que 100. 
'''


if temperatura_agua > 100:
    print("El água está en estado gaseoso.")
elif temperatura_agua > 0:
     print("El água está en estado líquido.")
elif temperatura_agua < 0:
   print("El água está en estado sólido.")

#################################################################################
# 3 - Bucles

# escribir los números del 0 al 10 (el ultimo valor no está incluido)
print("FOR")
for numero in range(0,10):
    print(numero)

# escribir los números del 0 al 10 (el ultimo valor no está incluido)
print("WHILE")
numero = 0
while numero < 10:
    print(numero)
    numero = numero + 1

# añadiendo un número en una lista cuando éste sea par
pares = []
numero = 6
if numero%2 == 0:
    print(f"{numero} es par")
    pares.append(numero)
else:
    print(f"{numero} es impar")
print(pares)

# añadiendo todos los números pares entre el 0 y 51 en una lista usando while
pares = []
numero = 0
while numero < 51:
    if numero%2 == 0:
        pares.append(numero)
    numero = numero + 1
print(pares)

# otra manera de hacer lo mismo sería la siguiente:
pares = []
numero = 0
while numero < 51:
    pares.append(numero)
    numero = numero + 2
print(pares)

print("-------------------------------")

# añadiendo todos los números pares entre el 0 y 51 en una lista usando for
pares = []
for numero in range(0,51):
    if numero%2 == 0:
        pares.append(numero)
print(pares)

# otra manera de hacer lo mismo sería la siguiente:
pares = []
for numero in range(0,51,2):
    pares.append(numero)
print(pares)

#################################################################################
# 4 - Funciones
'''
Explicación con más detalles sobre las funciones 
disponible en https://drive.google.com/file/d/1SB7ff6AB1jaTidw4kcyQAo0D3b21PbbJ/view
'''


# FUNCIÓN SIN PARAMETROS O RETURN
def contar_letras():
    nombre = input("¿Cuál es tu nombre? ")
    letras = len(nombre) # el comando len indica el tamaño de una lista o de una string
    print(f"Tu nombre tiene {letras} letras.")

contar_letras()

# FUNCIÓN CON PARAMETRO
def contar_letras(nombre):
    letras = len(nombre)
    print(f"Tu nombre tiene {letras} letras.")

nombre = input("¿Cuál es tu nombre? ")
contar_letras(nombre)

# FUNCIÓN CON PARAMETRO Y RETURN
def contar_letras(nombre):
    letras = len(nombre)
    return letras

nombre = input("¿Cuál es tu nombre? ")
letras = contar_letras(nombre)
print(f"Tu nombre tiene {letras} letras.")