# Escribe tu código aquí :-)

def calculadora(num_1, num_2, operacion):
    if operacion == "+":
        resultado = num_1 + num_2
    elif operacion == "-":
        resultado = num_1 - num_2
    elif operacion == "/":
        resultado = num_1 / num_2
    elif operacion == "*":
        resultado = num_1 * num_2
    return resultado

num_1 = int(input("Informe el primer numero: "))
num_2 = int(input("Informe el segundo numero: "))
operacion = input("¿Cuál operación? ")

resultado = calculadora(num_1, num_2, operacion)

print(num_1, operacion, num_2, "vale: ", resultado)
