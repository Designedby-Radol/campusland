# print

print("hola mundo")

# consulta de tipo de dato (type)

print(type(52)) # int
print(type(1.5)) # float
print(type(True)) # boolean
print(type("hola mondu")) # string
print(type(5 + 2j)) # complex number

# variables 
sara = 5 
print(sara)

sara2 = str(sara) # str cambia el tipo de dato a string 
print(sara2)

print(len(sara2)) # len nos otorga el largo de la cadena de datos


# input
coloca = input("hola coloca algo ")
print(coloca)

input(str)
print(input(str)) 

talvez = (3 + 2 * 6 / 2) # espacios
print(talvez)

# Operadores logicos

julian = True
juliana = False

num1 # Esto no es lo indicado, es mejor asignar un valor por defecto a las variables que se van a usar con input,
# para evitar errores en caso de que el usuario no ingrese nada
num2 = 0 # asi 
# input(num1) es incorrecto
num1 = input() # es correcto
input(num2)

suma = int(num1) + int(num2) 
print(suma)
