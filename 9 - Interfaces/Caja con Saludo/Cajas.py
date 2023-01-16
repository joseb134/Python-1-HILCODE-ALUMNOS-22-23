nombre = input("¿Cuál es tu nombre?")
MAX = 25
saludo = f"Hola, {nombre}"
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
