'''
Para finalizar de esta etapa, crearemos una función que generalice todo lo anterior de modo que siempre que sea necesario crear una caja,
podemos convocar esta funcion usando los parametros necesarios. Este será uno de los primeros usos avanzados de una función que
tendremos en Python.

La función debe recibir como parametros de entrada las dimensiones de la caja (longitud y número de líneas), el texto que debe
ser usado en el mensaje (Hola, Buenos dias, Buenas tardes, Buenas noches, ¿Qué tal?, etc..) y el nombre a ser puesto junto al texto.
Dados los inputs indicados, la función realizará la tarea de juntar el texto al nombre, crear y mostrar en pantalla la caja
en las dimensiones indicadas por medio de los parametros con el texto ya centralizado. Para hacerlo, podemos usar como base el código
que ya esta hecho en el archivo "2 - Caja con Saludo Tamaño Variable" que ya habéis hecho anteriormente.

Ejemplo de llamada para la función con su respectiva salida:

crear_caja(33, 7, 'Buenos días', 'Clóvis') #(MAX_HORIZONTAL, MAX_VERTICAL, saludo, nombre)

# caja creada:
 _________________________________
|                                 |
|                                 |
|                                 |
|      Buenos días, Clóvis.       |
|                                 |
|                                 |
|_________________________________|

'''
