"""
Lo primero que hacemos en cualquier proyecto es la parte visual/interfaz de interacción.
Las dos funciones abajo trabajan juntas para generar dicha interfaz, en nuestro caso, generan
la tabla del juego y la muestran por pantalla.
"""
import random

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

def victoria(casilla, jugador):
    ganador = 0
    if casilla[1] == jugador and casilla[2] == jugador and casilla[3] == jugador:
        ganador = jugador
    elif casilla[4] == jugador and casilla[5] == jugador and casilla[6] == jugador:
        ganador = jugador
    elif casilla[7] == jugador and casilla[8] == jugador and casilla[9] == jugador:
        ganador = jugador

    elif casilla[1] == jugador and casilla[4] == jugador and casilla[7] == jugador:
        ganador = jugador
    elif casilla[2] == jugador and casilla[5] == jugador and casilla[8] == jugador:
        ganador = jugador
    elif casilla[3] == jugador and casilla[6] == jugador and casilla[9] == jugador:
        ganador = jugador

    elif casilla[1] == jugador and casilla[5] == jugador and casilla[9] == jugador:
        ganador = jugador
    elif casilla[3] == jugador and casilla[5] == jugador and casilla[7] == jugador:
        ganador = jugador

    elif " " not in casilla:
        ganador = -1

    return ganador

if __name__ == "__main__":
    victorias_1 = 0
    victorias_2 = 0
    empates = 0
    reinicio = 1
    while reinicio == 1:
        posiciones = limpiarTabla()
        tabla = crearTabla(posiciones)
        print(tabla)

        jugador_1, jugador_2 = pregunta()
        print("JUGADOR 1: ", jugador_1)
        print("JUGADOR 2: ", jugador_2)

        ganador = 0
        i = 0
        jugadores = [jugador_1, jugador_2]
        while ganador == 0:
            posiciones = jugada(posiciones, jugadores[i%2])
            print(crearTabla(posiciones))
            ganador = victoria(posiciones, jugadores[i%2])
            i = i + 1

        if ganador == -1:
            print("EMPATE")
            empates += 1
        else:
            print("El ganador ha sido", ganador)
            if ganador == jugador_1:
                victorias_1 += 1
            else:
                victorias_2 += 1

        print("Victorias del jugador 1: ", victorias_1)
        print("Victorias del jugador 2: ", victorias_2)
        print("Empates: ", empates)
        reinicio = int(input("Volver a jugar?\n1 - SI\n2 - NO\n"))

'''
while ganador == 0:
    posiciones = jugada(posiciones, jugador_1)
    print(crearTabla(posiciones))
    ganador = victoria(posiciones, jugador_1)

    if ganador == 0:
        posiciones = jugada(posiciones, jugador_2)
        print(crearTabla(posiciones))
        ganador = victoria(posiciones, jugador_2)

'''
