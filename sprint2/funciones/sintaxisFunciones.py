'''
Reutiliz\ar codigo y hacer el software modular para hacer mas eficiente
Esto se logra con el uso de funciones
'''

def miFuncion():
    print("hola desde la funcion")

def sumarNumeros(a,b):
    return a+b

miFuncion()

print("Ingresa dos numero y los sumare")

num1=int(input("opcion: "))
num2=int(input("opcion: "))

print(f"Este es el resultado de la funcion suma: {sumarNumeros(num1,num2)}")