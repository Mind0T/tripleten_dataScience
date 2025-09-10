#En una lista se pueden mezclar tipos de datons enteros, float, hasta una lista


lista=['Jaime','Irvin','Dilan']

print(lista)

movie_info=['Fight Club',1999,['thriller','drama','crime'],139,8.644]
print(movie_info)

title='Fight club'
year=1999
genre=['thriller','drama','crime']
movie_info2=[title,year,genre,139,8.644]
print(movie_info2)

print(movie_info[0])
print(type(movie_info[0]))
print(type(movie_info[1]))

print(movie_info[1:4]) ## Recuerda que el segundo numero es excluyente
#Igual que hace en los string al hacer slice y poner un valor fuera de un posision no marcara problema alguno

