a = int(3)
b = int(5)

total = a + b
resta = a - b
producto =  a * b
division = a / b
mod = a % b
entera = a // b
exponencial =  a ** b

print(total)
print('a + b = ', total)
print('a - b = ', resta)
print('a * b = ', producto)
print('a / b = ', division)
print('a % b = ', mod)
print('a // b = ', entera)
print('a ** b = ', exponencial ,'\n\n') # No seas manco bro, no necesitas separar los \n

nombre = str('Raul')
print (f'el nombre ke ingreso es "{nombre}"', '\n\n')

print (f'nombre: \n{nombre}\n')
print ('el nombre que ingreso es', 'holaa' , 'si', sep = '\n') # Tienes q ser consistente, o vas a usar ' o vas a usar ", no uses los dos al azar
print ('\n')
print (f'Fundamentos', 'Programacion', 'en', sep = '***', end = '...Python') # espacios bro por favor, hay q poner espacios


print(type(52)) # int
print(type(1.5)) # float
print(type(True)) # boolean
print(type('hola mondu')) # string
print(type(5 + 2j)) # complex number
