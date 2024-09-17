def saludo ():
    print ("holamundo")
saludo()

def saludo2(nombre="Mundo"):
    print(f"¡Hola, {nombre}!")
saludo2()  # Imprime: ¡Hola, Mundo!
saludo2("Alice")  # Imprime: ¡Hola, Alice!

def mostrar_info(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos keyword:", kwargs)

mostrar_info(9, 6, 5, nombre="Alice", edad=30)

numero = 15
print (f'nombre: \n{numero}')
print ("hola" , "tunombre", sep='\n')

if (True == True): 
    print("hola")

class anidada():
    def funcopop1(a,b):
        return a+b

print(anidada.funcopop1(3,4))
