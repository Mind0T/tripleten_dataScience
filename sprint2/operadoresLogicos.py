#if statement is True thes this

'''
Operadores de comparacion
==
!=
>
<
>=
<=

Operadores logicos
and
or 
not


No se pueden comprar tipos de datos distintos a menos los numericos
como float e int

funcion de predicado

string.isalpha()
string.isdigit()
string.islower()

'''

text_entries = ['Hola', 'hola', '1234', "hola1234"]  # Lista de entradas de texto

for x in text_entries:
    print(f"Texto: '{x}':")
    condicion1=x.isalpha() or x.isdigit()
    condicion2=not condicion1
    print(f"Es alfabetico o tiene digitos: {condicion1}")
    print(f"No es alfabetixo ni son digitos: {condicion2}")


'''
salida esperada
Texto 'Hola':
Es alfabético o tiene dígitos True
No es alfabético ni son dígitos False
Texto 'hola':
Es alfabético o tiene dígitos True
No es alfabético ni son dígitos False
Texto '1234':
Es alfabético o tiene dígitos True
No es alfabético ni son dígitos False
Texto 'hola1234':
Es alfabético o tiene dígitos False
No es alfabético ni son dígitos True
'''