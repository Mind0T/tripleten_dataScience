#Mientras un string es inmutable un a lista es un objeto mutable
print('Metodos para modificar un lista')
print(
'''
append()
extend()
insert()
pop()
'''
)



#Adicion de elementos a una lista

#Agregar un elemento al final de una lista
print('Adicion de elemento a una lista con append\nSolo se puede agregar un elemento a la vez')
shawshank_movie=['The Shawshank Redemption','USA',1994,'drama',142,9.111]
print(shawshank_movie)

shawshank_movie.append('Frank Darabont')# solo se puede agregar un elemento a la vez
print(shawshank_movie)

print()

#Agregar varios elementos al final de una lista

print('Agregar un elemento al final de una lista con extend\nSe puede agregar varios elementos a la vez')

godfather_movie=['The Godfather','USA',1972]
print(godfather_movie)
godfather_movie.extend(['Francis Ford Coppola','Nino Rota'])
print(godfather_movie)

print()
# Agregar un elemento en un indice determinado con insert
print('Agregar un elemento en un indice especifico con insert')
dark_knight_movie=['The Dark Knight','USA','fantasy, action, triller',152]
print(dark_knight_movie)
dark_knight_movie.insert(2,2008) # primer parametro el indice y en el segundo el valor que ira en ese indice lo inserta sin sustituir
print(dark_knight_movie)

print()

#Eliminar un elemento de una lista
print('Eliminar elementos de una lista con pop()')

movie=['Matrix','Matrix 2','Matrix 3']
print(movie)
movie.pop(1) #este se puede almacenar en una variable
print(movie)