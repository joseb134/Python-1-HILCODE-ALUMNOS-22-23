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

posiciones = limpiarTabla()
tabla = crearTabla(posiciones)

print(tabla)

