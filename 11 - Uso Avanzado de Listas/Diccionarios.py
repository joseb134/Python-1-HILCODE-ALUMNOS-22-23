'''
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
hermanos = int(input("¿Cuántos hermanos tienes? "))
ciudad = input("¿De qué ciudad eres? ")
color = input("Cuál es tu color favorito? ")

persona_1 = []
persona_1.append(nombre)
persona_1.append(edad)
persona_1.append(hermanos)
persona_1.append(ciudad)
persona_1.append(color)

print(persona_1)
print(persona_1[2])

personas = {"nombre": nombre, "edad": edad, "hermanos": hermanos,
            "ciudad": ciudad, "color": color}

print(personas["color"])
'''

ordenador_1 = {"procesador": "intel i7 7th Generacion", "RAM": "24 GB",
                "GPU": "NVIDIA GEFORCE GTX 950M", "HD": 1000, "SSD": 128}

print(ordenador_1["RAM"])
ram = ordenador_1["RAM"]
ram = ram[0:2]
print(type(ram))
ram = int(ram)
print(type(ram))
print(ram)

ordenadores = {"procesador": ["intel i7 7th Generación","intel i5 7th Generación"],
                "RAM": [24, 32], "GPU": ["NVIDIA GEFORCE GTX 950M","NULL"],
                "HD": [1000,500], "SSD": [128,256]}

print(ordenadores["GPU"])
print(ordenadores["HD"])

ordenador_1 = {"procesador": "intel i7 7th Generacion", "RAM": "24 GB",
                "GPU": "NVIDIA GEFORCE GTX 950M", "HD": 1000, "SSD": 128}
ordenador_1["pantalla"] = 16
print(ordenador_1)
ordenador_1["RAM"] = "32 GB"
print(ordenador_1)
##################################################################

lista_nombres = []
lista_edades = []
lista_hermanos = []
lista_ciudades = []
lista_colores = []

for i in range(2):
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuántos años tienes? "))
    hermanos = int(input("¿Cuántos hermanos tienes? "))
    ciudad = input("¿De qué ciudad eres? ")
    color = input("Cuál es tu color favorito? ")

    lista_nombres.append(nombre)
    lista_edades.append(edad)
    lista_hermanos.append(hermanos)
    lista_ciudades.append(ciudad)
    lista_colores.append(color)

personas = {"nombre": lista_nombres, "edad": lista_edades, "hermanos": lista_hermanos,
            "ciudad": lista_ciudades, "color": lista_colores}

print(personas)
print(personas["nombre"])
print(personas["edad"])
print(personas["nombre"][0])
print(personas["edad"][0])
print(personas["nombre"][1])
print(personas["edad"][1])

# otra manera
personas = {"nombre": [], "edad": [], "hermanos": [], "ciudad": [], "color": []}

for i in range(2):
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuántos años tienes? "))
    hermanos = int(input("¿Cuántos hermanos tienes? "))
    ciudad = input("¿De qué ciudad eres? ")
    color = input("Cuál es tu color favorito? ")

    personas["nombre"].append(nombre)
    personas["edad"].append(edad)
    personas["hermanos"].append(hermanos)
    personas["ciudad"].append(ciudad)
    personas["color"].append(color)

print(personas)

# otra manera
personas = {"nombre": [], "edad": [], "hermanos": [], "ciudad": [], "color": []}

for i in range(2):
    personas["nombre"].append(input("¿Cuál es tu nombre? "))
    personas["edad"].append(int(input("¿Cuántos años tienes? ")))
    personas["hermanos"].append(int(input("¿Cuántos hermanos tienes? ")))
    personas["ciudad"].append(input("¿De qué ciudad eres? "))
    personas["color"].append(input("Cuál es tu color favorito? "))

print(personas)
