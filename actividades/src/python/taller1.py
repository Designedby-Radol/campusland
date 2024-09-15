"""
Hola, este archivo van todas los ejercicios del taller 1 de python clase j1
hey, this file contains all the exercises of python workshop 1 class j1.
"""
import random
import string


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

# Ejercicio 12: Calculadora de IMC (Índice de Masa Corporal)
## Escribe un programa que calcule el IMC y determine el estado de peso.
### Solicita al usuario su peso (en kg) y su altura (en metros). Calcula el IMC y clasifícalo en bajo peso(<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9), o obesidad (>=30).

def calculadorIMC(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return 'Bajo peso.\n'
    elif 18.5 <= imc <= 24.9:
        return 'Peso normal.\n'
    elif 25 <= imc <= 29.9:
        return 'Sobrepeso.\n'
    else:
        return 'Obesidad.\n'
    

print(calculadorIMC(
    float(
        input('coloque su peso: ')
        ),
    float(
        input('coloque su altura: ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 13: Comparación de tres números 
## Escribe un programa que determine el mayor de tres números usando if .

def comparacionNumeros(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return f'{numero1} es el mayor.\n'
    elif numero2 > numero1 and numero2 > numero3:
        return f'{numero2} es el mayor.\n'
    elif numero3 > numero1 and numero3 > numero2 :
        return f'{numero3} es el mayor.\n'
    
print(comparacionNumeros(
    int(
        input('coloque el primer numero: ')
        ),
    int(
        input('coloque el segundo numero: ')
        ),
    int(
        input('coloque el tercer numero: ')
        )
    )
)

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 14: Adivinanza de letras
## Escribe un programa que permita al usuario adivinar una letra secreta usando match .

def adivinanzaLetra():
    letraSecreta = random.choice(string.ascii_lowercase)
    print(letraSecreta)
    while True:
        letraUsuario = input('Adivina una letra: ').lower()
        matc = letraUsuario == letraSecreta
        match matc:
            case True:
                return 'La letra secreta es correcta.\n'
                break
            case False:
                return 'La letra secreta es incorrecta.\n'
                continue

print(adivinanzaLetra())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 15: Cálculo del salario neto
## Solicita al usuario su salario bruto y su país de residencia. 
## Calcula el salario neto aplicando impuestos: el 20% para residentes de "País A", el 15% para "País B" y el 10% para "País C". Si el país no está en la lista, aplica un 25% de impuestos.


def calculoSalarioNeto():
    salarioBruto = float(
        input('coloque su salario bruto: ')
        )
    print('Coloque su pais de residencia', 'a: País A', 'b: País B', 'c: País C', sep = '\n')  # ejemplo: 'a' para País A, 'b' para País B, 'c' para País C, cualquier otro valor para País C
    paisResidencia = str(input().lower)
    match paisResidencia:
        case 'a':
            return salarioBruto * (1 - 0.20)
        case 'b':
            return salarioBruto * (1 - 0.15)
        case 'c':
            return salarioBruto * (1 - 0.10)
        case _:
            return salarioBruto * (1 - 0.25)

print(calculoSalarioNeto())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 16: Cálculo del tiempo de viaje
## Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h). 
## Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un mensaje de advertencia.

def calculoTiempoViaje():
    distancia = float(
        input('coloque la distancia a recorrer (en km): ')
        )
    velocidadPromedio = float(
        input('coloque la velocidad promedio del automovil (en km/h): ')
        )
    if velocidadPromedio > 120:
        print('ATENCION: La velocidad promedio del automovil es muy alta, puede causar accidentes.')
    tiempo = distancia / velocidadPromedio
    horas = int(tiempo)
    minutos = int((tiempo - horas) * 60)
    return f'El tiempo de viaje es {horas} horas y {minutos} minutos.'

print(calculoTiempoViaje())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 17: Sistema de calificaciones con bonificaciones
## Solicita la calificación del estudiante y pregunta si hizo tareas adicionales. Si la respuesta es "sí",
## añade un 5% extra a la calificación, pero si la calificación supera 100, ajústala a 100. Si la respuesta
## es "no", simplemente muestra la calificación original.

def sistemaCalificaciones():
    calificacion = float(
        input('coloque su calificacion: ')
        )
    while True:
        tareasAdicionales = input('¿Hizo tareas adicionales? (sí/no): ').lower()
        if tareasAdicionales == 'si':
            calificacion += calificacion * 0.05
            if calificacion > 100:
                calificacion = 100
            break
        elif tareasAdicionales == 'no':
            pass
            break
        else:
            print('Respuesta invalida, coloque "sí" o "no".')
    return f'Su calificacion es {calificacion}.'

print(sistemaCalificaciones())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 18: Sistema de evaluación de créditos universitarios
## Solicita al usuario ingresar el número de materias que ha cursado. Para cada materia, solicita el
## puntaje y determina si ha aprobado o no (>= 60). Luego, calcula el número total de créditos del
## estudiante (cada materia aprobada otorga 3 créditos).

def sistemaCreditos():
    numeroMaterias = int(
        input('coloque el numero de materias que ha cursado: ')
        )
    creditosTotales = 0
    i = 0
    for _ in range(numeroMaterias):
        i += 1
        puntaje = float(
            input(f'coloque el puntaje de la materia {i}: ')
            )
        if puntaje >= 60:
            creditosTotales += 3
            print('La materia ha sido aprobada.')
            continue
        elif creditosTotales <= 60:
            print('La materia ha sido reprobada.')
    return f'El estudiante ha cursado {numeroMaterias} materias, y ha acumulado {creditosTotales} créditos.'

print(sistemaCreditos())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 19: Conversión de calificaciones numéricas a letras
## Escribe un programa que convierta una calificación numérica en una letra de acuerdo a un sistema de calificación específico, usando match .

def calificacionLetra():
    calificacion = int(input('Introduce la calificacion numerica (0-100): '))
    match calificacion:
        case n if 90 <= n <= 100:
            return 'Tu calificación en letra es: A'
        case n if 80 <= n < 90:
            return 'Tu calificación en letra es: B'
        case n if 70 <= n < 80:
            return 'Tu calificación en letra es: C'
        case n if 60 <= n < 70:
            return 'Tu calificación en letra es: D'
        case n if 0 <= n < 60:
            return 'Tu calificación en letra es: F'
        case _:
            return 'Calificación inválida'

print(calificacionLetra())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 20: Sistema de estacionamiento con tarifas progresivas
## Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con tarifas progresivas.

def estacionamiento():
    HRS = int(input('digite las horas de estacionamiento: '))
    precio = int()
    if HRS >= 1: 
        precio +=5 
    if HRS >= 2:
        precio += 4
    if HRS >= 3:
        precio += 4
    if HRS >= 4:
        precio += 4
    if HRS > 4:
        for i in range(HRS-4):
            precio += 3
    return f'el costo del estacionamiento es: ${precio}'

print(estacionamiento())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 21: Clasificación de triángulos por sus ángulos
## Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos internos usando if

def trianguloAngulos():
    while True:
        ang1 = int(input('Ingrese el primer ángulo del triangulo: '))
        ang2 = int(input('Ingrese el segundo ángulo del triangulo: '))
        ang3 = int(input('Ingrese el tercer ángulo del triangulo: '))
        if ang1 + ang2 > ang3 and ang1 + ang3 > ang2 and ang2 + ang3 > ang1:
            if ang1 <= 90 and ang2 <= 90 and ang3 <= 90:
                return 'El triángulo es agudo.'
                break
            elif ang1 == 90 or ang2 == 90 or ang3 == 90:
                return 'El triángulo es rectangulo.'
                break
            elif  ang1 >= 90 or ang2 >= 90 or ang3 >= 90:
                return 'El triángulo es obtuso.'
                break
        else: 
            print('no es un triangulo')

print(trianguloAngulos())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 22: Suma de los primeros N números enteros
## Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los 
## primeros n números enteros. Utiliza un ciclo for para realizar la suma.

def sumaPrimerosN():
    n = int(input('Ingrese un número entero positivo: '))
    suma = 0
    for i in range(1, n+1):
        suma += i
        print(f'El {i}º número es {i} y la suma es {suma}')
    return suma

print(sumaPrimerosN())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 23: Contador de vocales en una cadena
## Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales (a, e, i, o, u)
## contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta.

def contarVocales():
    cadena = input('Ingrese una cadena de texto: ')
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
            print(f'La letra {letra} es una vocal.')
    return f'La cadena contiene {contador} vocales.'

print(contarVocales())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 24: Factorial de un número
## Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
## dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo.

def factorial():
    n = int(input('Ingrese un número entero positivo: '))
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        print(f'El {i}º número es {i} y el factorial es {factorial}')
        if factorial > 1000000:
            print('El factorial es demasiado grande para calcularlo a mano.')
            break
        elif factorial == 1000000:
            print('El factorial es demasiado grande para ser calculado exactamente.')
            break
    return f'El factorial de {n} es {factorial}.'

print(factorial())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 25: Números pares en un rango
## Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de fin. 
## El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa un ciclo for para recorrer el rango.

def numerosPares():
    inicio = int(input('Ingrese el número de inicio del rango: '))
    fin = int(input('Ingrese el número de fin del rango: '))
    for num in range(inicio, fin+1):
        if num % 2 == 0:
            print(num)

print(numerosPares())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 26: Adivina el número (con while ) 

def adivinaNúmero():
    numeroSecreto = random.randint(1, 100)
    intentos = 0
    while True:
        numeroUsuario = int(input('Adivina el número secreto (entre 1 y 100): '))
        intentos += 1
        if numeroUsuario == numeroSecreto:
            print(f'Felicidades! Adivinaste el número secreto en {intentos} intentos.')
            break
        elif numeroUsuario < numeroSecreto:
            print('Te has pasado de la respuesta. Prueba con un número mayor.')
            continue
        elif numeroUsuario > numeroSecreto:
            print('Te has quedado corto. Prueba con un número menor.')
            continue
        if intentos == 10:
            print(f'Perdiste. El número secreto era {numeroSecreto}.')
            break

print(adivinaNúmero())

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 27: Suma de números pares hasta que se introduce un impar

def sumaPares():
    suma = 0
    while True:
        numero = int(input('Introduce un número: '))
        if numero % 2 == 0:
            suma += numero
            print(f'La suma de los números pares introducidos hasta ahora es {suma}.')
            continue
        elif numero % 2 != 0:
            print('Se ha introducido un número impar.')
            break
    return f' la suma de los pares es: {suma}'

print(sumaPares())



