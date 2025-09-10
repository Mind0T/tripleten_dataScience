#Ordenar lists listas coleccion mutable de elementos
'''
metodo sort()  Es un metodo de lista modifica la lista
                Si se intenta  asignar esta a una variable regresara none ya que esta no devuelve ningun valor

funcion sorted() Es un funcion genera una nueva lista ordenada
                Se de asignar a una variable nueve


'''

#Metodo sort ordena la lista
print('Metodo sort\n')
years=[1994,1972,1993,2003,1994,1966,1999,1962,1997]
print(years)

years.sort()  #por defecto los ordena de mayor a menor
print(years)

years.sort(reverse=True) # podemos modificar el orden de mayor a menor con reverse=True
print(years)

'''
Para cuanod va ordenar strings sique un ORDEJ LEXICOGRAFICO

-Signos de puntuacion
-Numeros
-A-Z
-a-z
'''
movies=['The Shawshank Redemption','The Godfather','The Dark Knight','Schindler\'s List']
print(movies)
movies.sort()
print(movies) #si modificaramos The Dark Knight por the Dark Knight se modificaria el orden


#Funcion sorted

year2=[1994,1972,1993,2003,1994,1966,1999,1962,1997]
years_sort=year2.sort()
print(years_sort) #dara None

year_sorted=sorted(year2,reverse=True)
print(year_sorted)