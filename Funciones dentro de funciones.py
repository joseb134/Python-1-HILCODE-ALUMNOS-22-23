def inputs():
    n1 = int(input("Primer número: "))
    n2 = int(input("Segundo número: "))
    return n1, n2

def sumar():
    n1, n2 = inputs()
    suma = n1 + n2
    return suma

def bucle(num, resultado):
    if num > 0:
        num = int(input("NUM: "))
        resultado = bucle(num,resultado)
    return num

suma = sumar()
print(suma)

resultado = bucle(5,0)
print(resultado)
