"""
Hola, este archivo van todas los ejercicios del taller 1 de python clase j1
hey, this file contains all the exercises of python workshop 1 class j1.
"""
import random
import time
# Ejercicio 1:Verificación de números pares e impares
## Escribe un programa que verifique si un número es par o impar utilizando if .

def verificar(numero):
    if numero % 2 == 0:
        return 'El número es par. ☜(⌒▽⌒)☞\n'
    else:
        return 'El número es impar. •`_´•\n'  
    
print(verificar(
    int(
        input('coloque un numero para saber si es par o impar: ')
        )
    )
)
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 2: Calificación de una nota
## Escribe un programa que determine si una nota numérica es "Aprobado" o "Reprobado" usando if .

def calificacion(nota):
    if nota >= 60:
        return 'Aprobado ƪ(ړײ)\n'
    elif nota < 60:
        return 'Reprobado \n'

print(calificacion(
    int(
        input('coloque la calificacion para saber si es aprobado o reprobado: ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 3: Calculadora básica
## Utiliza match para implementar una calculadora simple.

def calculadora(a: int, b: int, operacion: str) :
    match operacion:
        case 1 : 
            return   f'{a} + {b} = {a + b}\n'
        case 2 : 
            return   f'{a} * {b} = {a * b}\n'
        case 3 : 
            return   f'{a} - {b} = {a - b}\n'
        case 4 :
            return   f'{a} / {b} = {a / b}\n'
        case _ :                 
            return 'operacion invalida\n'
    

a = int(input('asigne un valor que nececite operar: '))
b = int(input('asigne otro valor: '))
print(' ','elija la operacion que desea realizar: ', '1_+suma', '2_*multiplicacion', '3_-resta', '4_/divicion',sep = '\n' )
operacion = int(input())
print(calculadora(a , b , operacion))

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 4: Determinación del tipo de triángulo
## Escribe un programa que determine el tipo de triángulo en función de sus lados usando if .

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

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 5: Días de la semana
## Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la semana usando match .

def diaSemana(dia):
    match dia:
        case 1: return 'lunes\n'
        case 2: return 'martes\n'
        case 3: return 'miercoles\n'
        case 4: return 'jueves\n'
        case 5: return 'viernes\n'
        case 6: return 'sabado\n'
        case 7: return 'domingo\n'
        case _: return 'numero invalido, coloque un numero del 1 al 7\n'

print(diaSemana(
    int(
        input('coloque un numero del 1 al 7 para saber el dia de la semana: ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 6: Juego de adivinanza de números
## Escribe un programa que implemente un juego de adivinanza de números.

def adivinanza():
    numeroSecreto = random.randint(1, 100)
    intentos = 0
    while True:
        if intentos > 5:
            print('Has superado el numero de intentos permitidos.\n')
            print(f'Intento {intentos}: No adivinaste el numero, intentalo de nuevo.\n')
            break
        intentos += 1
        numeroUsuario = int(input('Adivina un numero del 1 al 10: '))
        if numeroUsuario == numeroSecreto:
            print('Felicidades! Adivinaste el numero secreto.\n')
            break
        elif numeroUsuario < numeroSecreto:
            print('El numero que ingresaste es menor.\n')
            continue
        elif numeroUsuario > numeroSecreto:
            print('El numero que ingresaste es mayor.\n')
            continue

print(adivinanza())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 7: Número positivo, negativo o cero
## Escribe un programa que determine si un número es positivo, negativo o cero usando if .

def numeroPositivoNegativoCero(numero):
    if numero > 0:
        return 'El número es positivo.\n'
    elif numero < 0:
        return 'El número es negativo.\n'
    elif numero == 0:
        return 'El número es cero.\n'
    
print(numeroPositivoNegativoCero(
    int(
        input('coloque un numero para saber si es positivo, negativo o cero: ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 8: Determinación de año bisiesto
## Escribe un programa que determine si un año es bisiesto o no.

def Bisiesto(año):
    if año % 4 == 0 and (año % 100!= 0 or año % 400 == 0):
        return 'El año es bisiesto.\n'
    else:
        return 'El año no es bisiesto.\n'
    

print(Bisiesto(
    int(
        input('coloque un año para saber si es bisiesto: ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 9: Clasificación de edades
## Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o anciano (65 años o más).

def clasificacionEdad(edad):
    if edad <= 12:
        return 'Niño.\n'
    elif edad >= 13  or edad <= 17 :
        return 'Adolescente.\n'
    elif edad >= 18 or edad <= 64 :
        return 'Adulto.\n'
    elif edad >= 65:
        return 'Anciano.\n'
    
print(clasificacionEdad(
    int(
        input('coloque su edad para saber su categoria: ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 10: Clasificación de notas
## Escribe un programa que asigne una calificación basada en una nota numérica. Solicita una nota numérica y clasifícala como A (90-100), B (80-89), C (70-79), D (60-69), o F (<60).

def clasificacionNota(nota): 
    if 90 <= nota <= 100:
        return 'A\n'
    elif 80 <= nota <= 89:
        return 'B\n'
    elif 70 <= nota <= 79:
        return 'C\n'
    elif 60 <= nota <= 69:
        return 'D\n'
    else:
        return 'F\n'

print(clasificacionNota(
    int(
        input('coloque una nota para saber su calificacion: ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 11: Conversión de temperaturas
# #Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando match .

def conversionTemperatura(temperatura, unidad):
    match unidad:
        case 1:
            return f'{temperatura * 9/5 + 32} grados Fahrenheit.'
        case 2:
            return f'{(temperatura - 32) * 5/9} grados Celsius.'
        case _:
            return 'unidad invalida, coloque C para Celsius o F para Fahrenheit.'

print(conversionTemperatura(
    float(
        input('coloque la temperatura: ')
        ),
        int(
        input('coloque la unidad (1 para Celsius, 2 para Fahrenheit): ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 12: 


