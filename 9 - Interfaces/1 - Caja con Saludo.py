'''
Empezaremos a trabajar ahora con las interfaces de interacción en Python. Primero
haremos interfaces manualmente usando simbolos del teclado. El primer proyecyo es
el siguiente: Crear una caja de texto donde se muestre un saludo (Hola, buenos días, buenas tardes, etc)
junto al nombre del usuario que será introducido por teclado.

La mensaje final tiene que estar centralizada en la caja tanto verticalmente como horizontalmente y la caja
debe adaptarse a diferentes nombres y mantener su forma independiente de cuantos caracteres tenga el nombre
desde que el nombre junto al saludo no resulten en un texto mayor que la longitud horizontal de la caja.

Ejemplos de outputs validos:

1)
 ______________________________
|                              |
|                              |
|     Hola, Clóvis Magno.      |
|                              |
|______________________________|


2)
 ______________________________
|                              |
|                              |
|        Hola, Clóvis.         |
|                              |
|______________________________|


3)
 ______________________________
|                              |
|                              |
|  Buenos días, Clóvis Magno.  |
|                              |
|______________________________|
'''

nombre = input("¿Cuál es tu nombre? ")
MAX = 25
saludo = f"Hola, {nombre}."
tam_texto = len(saludo)
espacios = MAX - tam_texto
espacios = espacios//2
texto_espacio = " "*espacios

print(" ________________________")
print("|                        |")
print("|                        |")
print(f"|{texto_espacio}{saludo}{texto_espacio}|")
print("|                        |")
print("|________________________|")
