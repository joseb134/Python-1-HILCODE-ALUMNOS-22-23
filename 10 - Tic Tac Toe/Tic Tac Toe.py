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

# la función pregunta() pide que los jugadores introduzcan por teclado el simbolo que quiere usar en el juego (X u O)
# si algún jugador escribe un valor inválido (algo diferente de X, x, O, o) el código pide otro valor
# la función debe pedir valores de manera continua hasta que un valor válido sea introducido
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

def jugada(posiciones, jugador):
    casilla = int(input("¿Dónde quieres jugar? Elija un número entre 1 y 9. "))
    while not(casilla >= 1 and casilla <= 9 and posiciones[casilla] == " "):
        if casilla < 1 or casilla > 9:
            print("VALOR INVALIDO!!\nIndique un número entre 1 y 9. ")
        elif posiciones[casilla] != " ":
            print("VALOR INVALIDO!!\nIndique una posición vacía. ")
        casilla = int(input("¿Dónde quieres jugar? Elija un número entre 1 y 9. "))
    posiciones[casilla] = jugador
    return posiciones

posiciones = limpiarTabla()
tabla = crearTabla(posiciones)
print(tabla)

jugador_1, jugador_2 = pregunta()
print("JUGADOR 1: ", jugador_1)
print("JUGADOR 2: ", jugador_2)

posiciones = jugada(posiciones, jugador_1)
print(crearTabla(posiciones))

posiciones = jugada(posiciones, jugador_2)
print(crearTabla(posiciones))
