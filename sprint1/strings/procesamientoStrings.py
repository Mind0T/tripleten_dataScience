#Procesamiento Strings

#recordando que un string es inmutable que pasaria si quisiera modificar una letra o una palabra repetida o mal escrita
#para ello tenemos 

'''
split() convertir un string en una lista
join()  
'''
print('Metodo split')

phrase='Hola estas mi hermano'
print(f"Este es un string: {phrase}")
words=phrase.split(' ') #---> en el parentesis se puede especificar que usaremos como separador por ejemplo .split('-')
print(f"Este es mi String a lista: {words} con tipo {type(words)}")

words.insert(1,'como') # aqui aprovecho para inclur otro dato
print(words)

print('\nMetodo join')
new_string=' '.join(words) #se especifica que usara para separa los elementos de la lista
print(f"De nuevo a string {new_string}, --> {type(new_string)}")


#para convertir un string de una sola palabra a lista es convertirlo o recastearlo directamente

name = "Irving"
print(name)
letters = list(name)
print(letters)

letters[0]='i'
print(letters)
name=''.join(letters)
print(name)
