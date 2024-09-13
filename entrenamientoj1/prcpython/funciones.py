def saludo(): # No coloques espacio entre el nombre de la variable y los parentesis
    print("holamundo") # Otra vez

# Coloca una linea blanca despues de terminar una funcion

saludo()

def saludo2(nombre = 'Mundo'): # Espacios a ambos lados del igual
    print(f'¡Hola, {nombre}!')

saludo2()  # Imprime: ¡Hola, Mundo!
saludo2('Alice')  # Imprime: ¡Hola, Alice!

def mostrar_info(*args, **kwargs):
    print('Argumentos posicionales:', args)
    print('Argumentos keyword:', kwargs)

mostrar_info(9, 6, 5, nombre = 'Alice', edad = 30)

numero = 15
print(f'nombre: \n{numero}')
print('hola', 'tunombre', sep = '\n') # No coloques un espacio antes de la coma de separacion de argumentos, solo despues.

if (True == True): 
    print("hola")

"""
Desarrollador:  Raul Santiago Ramirez Puyo
Problema: crear un programa que me permita tener los colores a partir de los primarios
"""

# Cuando vas a separar secciones de un codigo, pon una linea en blanco despues de que acaba la seccion, igual que como con una funcion

# definir los tres colores primarios
rojo = int(1)
amarillo = int(2)
azul = int(3)

# definir que colores se pueden obtener
verde = int(amarillo + azul)  # 5
morado =int (azul + rojo) # 4
naranja = int(amarillo + rojo) # 3

# darle al cliente los colores que tenemos disponibles y imprimir en pantalla el color que quiera
print('Hola buenas tardes', 'Tenemos estos colores', '1 rojo', '2 amarillo', sep = '\n')
descicion = int(input())
for(i = True): # Este for no es correcto
    if (): # ???
