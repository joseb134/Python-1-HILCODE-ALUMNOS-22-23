# Escribe tu código aquí :-)
# 8 filas, 20 columnas
# sala["A-12"] --> True // False

def crear_sala(n_filas, n_columnas):
    filas = ["A", "B", "C", "D", "E", "F", "G", "H"]
    sala = dict()  # es lo mismo que    sala = {}

    for i in range(len(filas)):
        for j in range(1,21):
            sala[filas[i] + "-" + str(j)] = False
    return sala

def check_asiento(sala):
    claves = list(sala.keys())
    filas = list()     # hace lo mismo que filas = []
    ultimo = int(claves[-1].split("-")[1])  # coge el ultimo elemento de las claves, separa siempre que aparece "-" y coge el segundo elemento de cada separación
    for i in range(0,len(claves),ultimo):
            filas.append(claves[i][0])

    print("Introduzca una filade A a H y una columna de 1 a 20")
    fila = input("¿Cuál fila? ").upper()
    while fila not in filas:
        fila = input("Valor inválido, indique otro.\nIndique una fila entre A y H\n").upper()

    columna = input("¿Cuál columna? ")
    while int(columna) < 1 or int(columna) > ultimo:
        columna = input("Valor inválido, indique otro.\nIndique una columna entre 1 y 20\n")

    asiento = fila + "-" + columna
    if sala[asiento] == False:
        print(f"El asiento {asiento} está libre.")
    else:
        print(f"El asiento {asiento} está ocupado.")


sala = crear_sala(0,0)
print(sala)
check_asiento(sala)




