"""
def triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
        if lado1 == lado2 == lado3:
            return 'El triangulo es equilatero.\n'
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return 'El triangulo es isosceles.\n'
        elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            return 'El triangulo es escaleno.\n'
    else: 
        return 'no es un triangulo.\n'

print('elija el tamaño de los lados del triangulo para saber que tipo de triangulo es\n')
lado2 = int(input('lado 1: '))
lado1 = int(input('lado 2: '))
lado3 = int(input('lado 3: '))
print(triangulo(lado1, lado2, lado3))

"""


"""
ejercicio 21
si paso 5 hrs
    entonces 1 de esas hrs vale $5 
    osea precio = $5
    las otras 4hrs valen $4 cada una $4*4
    osea precio = $5 + $16
"""

