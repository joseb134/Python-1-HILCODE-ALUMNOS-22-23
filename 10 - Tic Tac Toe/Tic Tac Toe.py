"""
Lo primero que hacemos en cualquier proyecto es la parte visual/interfaz de interacción.
Las dos funciones abajo trabajan juntas para generar dicha interfaz, en nuestro caso, generan
la tabla del juego y la muestran por pantalla.
"""

# limpiarTabla() crea y limpia la lista de posiciones que almacenan los valores de las jugadas
def limpiarTabla():
    posiciones = ["#"," "," "," "," "," "," "," "," "," "]
    return posiciones

# crearTabla() recibe de parametro la lista de posiciones y genera una variable con
# el dibujo de la tabla del juego donde también se enseña que hay en cada casilla de la tabla
# a través de los valores guardados en la lista de posiciones.
def crearTabla(posiciones):
    tabla = f"""
         |     |
      {posiciones[7]}  |  {posiciones[8]}  |  {posiciones[9]}
         |     |
    -----------------
         |     |
      {posiciones[4]}  |  {posiciones[5]}  |  {posiciones[6]}
         |     |
    -----------------
         |     |
      {posiciones[1]}  |  {posiciones[2]}  |  {posiciones[3]}
         |     |
    """
    return tabla


def pregunta():
    jugador_1 = input("¿Que eliges, la 'X' o la 'O'? ")
    jugador_1 = jugador_1.upper() # jugador_1.lower() --> pasa toda una string a minusculas

    while jugador_1 != "O" and jugador_1 != "X":
        print("INVALIDO.\n¿'X' o 'O'? ")
        jugador_1 = input("¿Que eliges, la 'X' o la 'O'? ")
        jugador_1 = jugador_1.upper()

    if jugador_1 == "X":
        print("Jugador 1 ha elegido la X.")
        jugador_2 = "O"

    elif jugador_1 == "O":
        print("Jugador 1 ha elegido la O.")
        jugador_2 = "X"

    return jugador_1, jugador_2


posiciones = limpiarTabla()
tabla = crearTabla(posiciones)
print(tabla)

jugador_1, jugador_2 = pregunta()
print("JUGADOR 1: ", jugador_1)
print("JUGADOR 2: ", jugador_2)










