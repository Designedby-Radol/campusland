import os
# hola = ['postobon','cocacola',[],[]]
# print(hola)
# print(hola[0])
# print(len(hola))
# i = 0
# hola.insert(2,'pepsi')
# print(hola.index('cocacola'))
# for valor in hola:
#     print('valor',valor)

# leer los nombres de n cantidad de personas y cuando el usuario tome la descicion de no ingresar mas nombres mostras los nomnbres ingresados

def arrayPersonas():
    personas = []
    personas.append(input('ingrese un nombre: '))
    os.system('clear')
    if (bool(input('desea poner otro nombre?: S(Si), Enter(no)'))):
        os.system('clear')
        arrayPersonas()
    for i in personas:
        print(i)

if __name__  == '__main__':
    arrayPersonas()  