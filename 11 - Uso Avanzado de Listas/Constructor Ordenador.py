# Escribe tu código aquí :-)

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
    ordenador["ram"] = ordenador["ram"] + cantidad

    return ordenador

ordenador3 = {"edad": 18, "altura": 1.65}
ordenador3 = aumentaRam(cantidad = 16, ordenador = ordenador3)
print(ordenador3)

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
print("\nOrdenador1: ", ordenador1)
print("\nOrdenador2: ", ordenador2)






