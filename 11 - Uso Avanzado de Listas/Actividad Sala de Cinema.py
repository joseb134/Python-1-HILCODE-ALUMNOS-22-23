# Escribe tu código aquí :-)
# 8 filas, 20 columnas
# sala["A-12"] --> True // False

def crear_sala(n_filas, n_columnas):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    filas = list()
    sala = dict()  # es lo mismo que    sala = {}   (crea un diccionario vacio)

    filas = letras[0:n_filas]
    """
    filas = letras[0:n_filas]

    Este código coge un trozo de la variable letras a partir de los valores que están dentro de los corchetes.
    Coge el trozo que va de 0 hasta el valor indicado por "n_filas".
    Demostraciones del funcionamento están en el archivo de listas avanzado.
    """

    '''
    El codigo abajo hace lo mismo que el anterior pero usando bucles
    for i in range(0,n_filas):
        filas.append(letras[i])
    '''

    for i in range(len(filas)):
        for j in range(1,n_columnas+1):
            sala[filas[i] + "-" + str(j)] = False
    return sala

def check_asiento(sala):
    claves = list(sala.keys())
    filas = list()     # hace lo mismo que filas = []   (crea una lista vacía)
    ultimo = int(claves[-1].split("-")[1])  # coge el ultimo elemento de las claves, separa siempre que aparece "-" y coge el segundo elemento de cada separación
    for i in range(0,len(claves),ultimo):
        filas.append(claves[i][0])

    print("Introduzca una fila.")
    fila = input("¿Cuál fila? ").upper()
    while fila not in filas:
        fila = input("Valor inválido, indique otro.\nIndique una fila entre A y H\n").upper()

    columna = input("¿Cuál columna? ")
    while int(columna) < 1 or int(columna) > ultimo:
        columna = input("Valor inválido, indique otro.\nIndique una columna\n")

    asiento = fila + "-" + columna
    if sala[asiento] == False:
        print(f"El asiento {asiento} está libre.")
    else:
        print(f"El asiento {asiento} está ocupado.")


n_filas = int(input("¿Cuántas filas? "))
while n_filas < 0 or n_filas > 26:
    n_filas = int(input("Indique un valor válido. "))

n_columnas = int(input("¿Cuántas columnas? "))
while n_columnas < 1 or n_columnas > 50:
    n_columnas = int(input("Indique un valor válido.\nEscriba un valor entre 1 y 50."))

sala = crear_sala(n_filas,n_columnas)
print(sala)
check_asiento(sala)




