# Escribe tu código aquí :-)
import random

def numero_aleatorio():
    dado = random.randint(1,6)
    return dado

def j1(jugador_1, dado):
    jugador_1 = jugador_1 + dado # jugador_1 += dado
    print("Número sorteado: ",dado)
    print("Jugador 1, tienes", jugador_1, "puntos, ¿deseas continuar?")
    stop = int(input("Pulse 1 para 'sí' y 2 para 'no' "))

    while(jugador_1 < 21 and stop == 1):
        dado = random.randint(1,6)
        print("\nNúmero sorteado: ",dado)
        jugador_1 += dado

        if jugador_1 < 21:
            print("Jugador 1, tienes", jugador_1, "puntos, ¿deseas continuar?")
            stop = int(input("Pulse 1 para 'sí' y 2 para 'no' "))

    print("\nJugador 1 ha terminado su jugada con", jugador_1, "puntos.\n\n")

    return jugador_1

def j2(jugador_2, dado):
    jugador_2 += dado
    print("Jugador 2, tienes", jugador_2, "puntos, ¿deseas continuar?")
    stop = int(input("Pulse 1 para 'sí' y 2 para 'no' "))

    while(jugador_2 < 21 and stop == 1):
        dado = random.randint(1,6)
        print("\nNúmero sorteado: ",dado)
        jugador_2 += dado

        if jugador_2 < 21:
            print("Jugador 2, tienes", jugador_2, "puntos, ¿deseas continuar?")
            stop = int(input("Pulse 1 para 'sí' y 2 para 'no' "))

    print("\nJugador 2 ha terminado su jugada con", jugador_2, "puntos.\n\n\n")

    return jugador_2

def ganador(jugador_1, jugador_2):
    if jugador_2 > 21 and jugador_1 <= 21:
        print("Jugador 1 es el ganador. Resultado:\nJugador 1:",jugador_1,"puntos.")
        print("Jugador 2:",jugador_2,"puntos.")

    elif jugador_1 > 21 and jugador_2 <= 21:
        print("Jugador 2 es el ganador. Resultado:\nJugador 1:",jugador_1,"puntos.")
        print("Jugador 2:",jugador_2,"puntos.")

    elif jugador_1 > jugador_2:
        print("Jugador 1 es el ganador. Resultado:\nJugador 1:",jugador_1,"puntos.")
        print("Jugador 2:",jugador_2,"puntos.")
    elif jugador_1 < jugador_2:
        print("Jugador 2 es el ganador. Resultado:\nJugador 1:",jugador_1,"puntos.")
        print("Jugador 2:",jugador_2,"puntos.")
    else:
        print("¡Empate! Resultado:\nJugador 1:",jugador_1,"puntos.")
        print("Jugador 2:",jugador_2,"puntos.")

jugador_1 = 0
jugador_2 = 0

dado = numero_aleatorio()
jugador_1 = j1(jugador_1, dado)

dado = numero_aleatorio()
jugador_2 = j2(jugador_2, dado)
ganador(jugador_1, jugador_2)

