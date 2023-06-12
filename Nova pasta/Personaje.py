# Escribe tu código aquí :-)
'''
jugador, monstruo
si es jugador: vida, velocidad, comida, armas, sprite

si es monstruo: vida, velocidad, armas, sprite
'''

def constructorPersonaje(tipo, sprite):
    velocidad = 10
    armas = []
    vida = 100
    comida = 50

    objeto = {  "vida": vida,
                "velocidad": velocidad,
                "armas": armas,
                "sprite": sprite}

    if tipo == "jugador":
        objeto["comida"] = comida
        objeto["tipo"] = tipo
    elif tipo == "monstruo":
        objeto["tipo"] = tipo
    else:
        return "TIPO INVÁLIDO"

    return objeto

def getVida(objeto):
    vida = None
    if type(objeto) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(objeto))
    elif "tipo" not in objeto:
        print("El objeto no tiene dipo definido.")
    elif objeto["tipo"] != "jugador" and objeto["tipo"] != "monstruo":
        print("Objeto de tipo incompatiple: ", objeto["tipo"])
    else:
        vida = objeto["vida"]
    return vida



p1 = constructorPersonaje(tipo = "jugador", sprite = "")
m1 = constructorPersonaje(tipo = "monstruo", sprite = "")
print(p1)
print(m1)
print("Vida p1: ", getVida(p1))

p2 = {"edad": 20, "altura": 1.7}
print("Vida p2: ", getVida(p2))





