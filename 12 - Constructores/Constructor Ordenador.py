def constructorOrdenadores(ram, procesador, tarjeta_grafica, rom, pantalla, teclado, raton):

    objeto = {  "tipo": "ordenador",
                "ram": ram,
                "procesador": procesador,
                "tarjeta_grafica": tarjeta_grafica,
                "rom": rom,
                "pantalla": pantalla,
                "teclado": teclado,
                "raton": raton}
    return objeto

def aumentaRam(cantidad, ordenador):
    if type(cantidad) != int and type(cantidad) != float:
        print("La cantidad no es de tipo numérico. Tipo informado: ",type(cantidad))
    elif cantidad < 0:
        print("La cantidad tiene que ser un valor positivo y no nulo.")
    elif type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ordenador["ram"] = ordenador["ram"] + cantidad
    return ordenador

def getRam(ordenador):
    ram = None
    if type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ram = ordenador["ram"]
    return ram

def setRam(cantidad, ordenador):
    if type(cantidad) != int and type(cantidad) != float:
        print("La cantidad no es de tipo numérico. Tipo informado: ",type(cantidad))
    elif cantidad < 0:
        print("La cantidad tiene que ser un valor positivo y no nulo.")
    elif type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ordenador["ram"] = cantidad
    return ordenador

def getProcesador(ordenador):
    procesador = None
    if type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        procesador = ordenador["procesador"]
    return procesador

def setProcesador(procesador, ordenador):
    if type(procesador) != str:
        print("El procesador informado es invalido: ",type(procesador))
    elif type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ordenador["procesador"] = procesador
    return ordenador

def getTarjetaGrafica(ordenador):
    tarjeta_grafica = None
    if type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        tarjeta_grafica = ordenador["procesador"]
    return tarjeta_grafica

def setTarjetaGrafica(procesador, ordenador):
    if type(tarjeta_grafica) != str:
        print("El procesador informado es invalido: ",type(tarjeta_grafica))
    elif type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ordenador["tarjeta_grafica"] = tarjeta_grafica
    return ordenador

def getRom(ordenador):
    rom = None
    if type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        rom = ordenador["rom"]
    return rom

def setRom(cantidad, ordenador):
    if type(cantidad) != int and type(cantidad) != float:
        print("La cantidad no es de tipo numérico. Tipo informado: ",type(cantidad))
    elif cantidad < 4:
        print("La cantidad tiene que ser un valor mayor que 4.")
    elif type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ordenador["rom"] = cantidad
    return ordenador

def getPantalla(ordenador):
    pantalla = None
    if type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        pantalla = ordenador["pantalla"]
    return pantalla

def setPantalla(cantidad, ordenador):
    if type(cantidad) != int and type(cantidad) != float:
        print("La cantidad no es de tipo numérico. Tipo informado: ",type(cantidad))
    elif cantidad < 10:
        print("La cantidad tiene que ser un valor mayor que 10.")
    elif type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ordenador["pantalla"] = cantidad
    return ordenador

def getTeclado(ordenador):
    teclado = None
    if type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        teclado = ordenador["teclado"]
    return teclado

def setTeclado(teclado, ordenador):
    if type(teclado) != str:
        print("El teclado informado es invalido: ",type(teclado))
    elif type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ordenador["teclado"] = teclado
    return ordenador

def getRaton(ordenador):
    raton = None
    if type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        raton = ordenador["raton"]
    return raton

def setRaton(raton, ordenador):
    if type(raton) != str:
        print("El raton informado es invalido: ",type(raton))
    elif type(ordenador) != dict:
        print("La variable no es un objeto. Tipo informado: ",type(ordenador))
    elif "tipo" not in ordenador:
        print("El objeto no tiene dipo definido.")
    elif ordenador["tipo"] != "ordenador":
        print("Objeto de tipo incompatiple: ", ordenador["tipo"])
    else:
        ordenador["raton"] = raton
    return ordenador

ordenador3 = {"edad": 18, "altura": 1.65}
ordenador3 = aumentaRam(cantidad = -16, ordenador = ordenador3)
print(ordenador3)
print("RAM del ordenador3: ", getRam(ordenador3))


ordenador1 = constructorOrdenadores(ram=24,
                                    tarjeta_grafica="NVIDIA GEFORCE GTX 950M",
                                    procesador="Intel Core i7",
                                    rom="1TB",
                                    pantalla="16 Pulgadas",
                                    teclado="Estandar Español",
                                    raton="Touchpad")

ordenador2 = constructorOrdenadores(ram=8,
                                    tarjeta_grafica="Intel Graphics",
                                    procesador="Intel Core i7",
                                    rom="500GB",
                                    pantalla="16 Pulgadas",
                                    teclado="Estandar Español",
                                    raton="Touchpad")

print("Ordenador1: ", ordenador1)
print("\nOrdenador2: ", ordenador2)

print("RAM Ordenador1: ", ordenador1["ram"])

ordenador1 = aumentaRam(cantidad = 8, ordenador = ordenador1)
print("RAM Ordenador1: ", ordenador1["ram"])
ordenador1 = setRam(cantidad = 12, ordenador = ordenador1)
print("RAM Ordenador1 despues de setRam: ", ordenador1["ram"])
print("\nOrdenador1: ", ordenador1)
print("\nOrdenador2: ", ordenador2)

print("RAM del ordenador1: ", getRam(ordenador1))
print("RAM del ordenador2: ", getRam(ordenador2))

x = input("Cual la RAM ")
ordenador2 = setRam(cantidad = x, ordenador = ordenador2)
print("\nOrdenador2: ", ordenador2)
