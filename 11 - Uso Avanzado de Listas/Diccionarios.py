# Ejemplo 1

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
hermanos = int(input("¿Cuántos hermanos tienes? "))
ciudad = input("¿De qué ciudad eres? ")
color = input("Cuál es tu color favorito? ")

'''
Al usar listas, necesitamos saber siempre el orden en el cual los datos han sido guardados en la variable
si despues los queremos usar. En este ejemplo, el orden ha sido "nombre, edad, hermanos, ciudad, color",
entonces, si queremos saber el nombre de la persona, debemos consultar siempre la primera posición de la lista.
Esto hace el uso de lista para estas situaciones poco práctico, entonces, cuando tenemos que guardar en una variable
datos que representan cosas diferentes, lo mejor sería usar los diccionarios.
'''
persona_1 = []
persona_1.append(nombre)
persona_1.append(edad)
persona_1.append(hermanos)
persona_1.append(ciudad)
persona_1.append(color)

print(persona_1)
print(persona_1[2])


'''
Con los diccionarios ya no dependemos del orden que los datos han sido guardados en la variable, si no de la clave que usamos para
guardar estos datos.
Cada clave de un diccionario se asocia con un valor, entonces podemos separar por claves los diferentes valores que queremos guardar en
la misma variable, así, cuando tengamos que usar los valores, solo tendríamos que llamar a la clave en la que está asociado, sin depender
del orden en que se ha guardado, como en las listas.
'''
personas = {"nombre": nombre, "edad": edad, "hermanos": hermanos,
            "ciudad": ciudad, "color": color}

print(personas["color"])

##################################################################################

# Ejemplo 2
ordenador_1 = {"procesador": "intel i7 7th Generacion", "RAM": "24 GB",
                "GPU": "NVIDIA GEFORCE GTX 950M", "HD": 1000, "SSD": 128}

print("Ordenador 1: ", ordenador_1["RAM"])
ram = ordenador_1["RAM"]
ram = ram[0:2]
print("Tipo de dato de la variable ram:", type(ram))
ram = int(ram) # convierte la ram a entero
print("Tipo de dato de la variable ram:", type(ram))
print(ram)

# en el diccionario ordenadores, se guardan 2 ordenadores diferentes.
# En cada clave del diccionario hay una lista con dos valores, cada valor corresponde al dato de uno de los ordenadores
ordenadores = {"procesador": ["intel i7 7th Generación","intel i5 7th Generación"],
                "RAM": [24, 32], "GPU": ["NVIDIA GEFORCE GTX 950M","NULL"],
                "HD": [1000,500], "SSD": [128,256]}

print(ordenadores["GPU"])
print(ordenadores["HD"])

ordenador_1 = {"procesador": "intel i7 7th Generacion", "RAM": "24 GB",
                "GPU": "NVIDIA GEFORCE GTX 950M", "HD": 1000, "SSD": 128}
ordenador_1["pantalla"] = 1
print(ordenador_1)
ordenador_1["RAM"] = "32 GB"
print(ordenador_1)
##################################################################
# Hacer un diccionario que guarde datos de 5 personas diferentes
# cada "tipo" de dato deberá ser almacenado en listas, y éstas, estarán dentro del diccionario

# 1ª manera:
lista_nombres = []
lista_edades = []
lista_hermanos = []
lista_ciudades = []
lista_colores = []

for i in range(5):
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

# 2ª manera:
personas = {"nombre": [], "edad": [], "hermanos": [], "ciudad": [], "color": []}

for i in range(5):
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

# 3ª manera:
personas = {"nombre": [], "edad": [], "hermanos": [], "ciudad": [], "color": []}

for i in range(5):
    personas["nombre"].append(input("¿Cuál es tu nombre? "))
    personas["edad"].append(int(input("¿Cuántos años tienes? ")))
    personas["hermanos"].append(int(input("¿Cuántos hermanos tienes? ")))
    personas["ciudad"].append(input("¿De qué ciudad eres? "))
    personas["color"].append(input("Cuál es tu color favorito? "))

print(personas)

#################################################################################

ordenadores = {"procesador": ["intel i7 7th Generación","intel i5 7th Generación"],
                "RAM": [24, 32], "GPU": ["NVIDIA GEFORCE GTX 950M","NULL"],
                "HD": [1000,500], "SSD": [128,256]}


claves = ordenadores.keys() # coge las claves del diccionario y las guarda en la variable "claves"
print(claves)
print(type(claves))

valores = ordenadores.values() # coge los valores del diccionario y los guarda en la variable "values"
print(valores)

