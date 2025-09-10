# se puede usat comillas sencillas y dobles

print('Irving\'s') #es como usar \n

"""
\n agregar un espacio
\t tabulacion
"""
#strings de varia lineas con """"

ejemploVariaLineas="""Hola
Mi nombre es Irving
Tengo 33 anios
Soy Estudiante
Bye"""

print(ejemploVariaLineas)

#Longitud

soneto="""
En el jardín de un tiempo ya fugado,
una tarde de luz y brisa quieta,
la eternidad en un perfil sujeta,
dejó tu risa el eco anacarado.

Aquel instante, puro y anhelado,
se niega a ser ceniza u hoja escueta,
y vive en la memoria del poeta,
como un tesoro oculto y resguardado.

Mas no hay poder que pueda aniquilar
la luz que nace de un recuerdo vivo;
pues basta un verso para hacer volver

tu rostro, tu presencia y tu mirar,
y hacer que el tiempo muerto, fugitivo,
en esta estrofa vuelva a florecer."""

print(f"Tamanio del soneto: {len(soneto)}")

print()


#slices
"""
Obtener una cadena dentro de otra cadena mas grande
Por ejemplo:
"""
city='Rio de Janeiro, Brasil'
substring=city[7:14]
print(substring)

# String formateados f-strings metodo format

"""
"""
print()
#normal estatico
message="Victoria tiene 23 anios y mide 157 cm"
print(message)

nombre="Victoria"
edad=23
estatura=157

#como lo suelo hacer
print(f"{nombre} tiene {edad} anios y mide {estatura} cm")

#f-string
mensaje=f"{nombre} tiene {edad} anios y mide {estatura} cm"  #se puede hacer operaciones dentro de las llaves
print(mensaje)

#format
mensaje2="{} tiene {} anios y mide {} cm".format(nombre,edad,estatura)
print(mensaje2)

#format mamon
mensaje3="{a} tiene {b} anios y mide {c} cm".format(b=edad,c=estatura,a=nombre)
print(mensaje3)


#Metodos de string
"""
string.upper()
string.lower()
string.replace()
string.strip()

"""


saludo="Hola"
print()
print(saludo)
print(f"{saludo.upper()}")
print(f"{saludo.lower()}")

#replace
listaSuper='''
aciete de colza
aceite de girasol
aceite de aguacate
aciete de cacahuete
'''
print(listaSuper)
print()

print(f"{listaSuper.replace('aciete','aceitito')}") # primero va la palabra a cambiar y por cual la cambiabos


user_ids="_151234_, _792051_, _955247_"
user_ids=user_ids.replace("_","") # "" asi se deja vacio
print(user_ids)

#strip
column_name='        fecha de de compra   '
print(column_name)
print(len(column_name))
print()
print(column_name.strip())
print(len(column_name.strip()))

# se puede usar seguido
'''
use_input="   MaRaDoNa"

clean_input="user_input.strip().upper()
'''