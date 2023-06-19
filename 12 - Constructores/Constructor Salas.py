# Escribe tu código aquí :-)

def constructorSalas(n_filas, n_columnas, nombre):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    filas = list()   # es lo mismo que    filas = []   (crea una lista vacía)
    asientos = dict()  # es lo mismo que    sala = {}   (crea un diccionario vacio)

    filas = letras[0:n_filas]

    for i in range(len(filas)):
        for j in range(1,n_columnas+1):
            asientos[filas[i] + "-" + str(j)] = False

    objeto = {  "tipo": "sala",
                "nombre":nombre,
                "filas": n_filas,
                "columnas": n_columnas,
                "asientos": asientos}
    return objeto

n_filas = int(input("¿Cuántas filas? "))
while n_filas < 0 or n_filas > 26:
    n_filas = int(input("Indique un valor válido. "))

n_columnas = int(input("¿Cuántas columnas? "))
while n_columnas < 1 or n_columnas > 50:
    n_columnas = int(input("Indique un valor válido.\nEscriba un valor entre 1 y 50."))

nombre = input("Nombre de la sala: ")
sala1 = constructorSalas(n_filas,n_columnas,nombre)
print(sala1)
print(f'\n{sala1["asientos"]}')
print(f'\n{sala1["asientos"]["A-3"]}')

sala1["asientos"]["A-3"] = True
print(f'\n{sala1["asientos"]}')
print(f'\nA-3:{sala1["asientos"]["A-3"]}')
