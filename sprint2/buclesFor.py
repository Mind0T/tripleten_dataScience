
'''
film_genres=['Dilan','Jaime','Irvin','Brenda']

for x in enumerate(film_genres):
    print(x)
    
'''

'''
Todas las películas tienen una duración en minutos. Para convertirla en horas, itera sobre la lista movies_info,
extrae la duración y guárdala en la variable runtime. Luego, utiliza la asignación aumentada para convertir la
variable runtime de minutos a horas. Una vez actualizada, muestra la duración en horas.

La salida esperada es esta:

2.3666666666666667
2.9166666666666665
2.533333333333333
3.25
3.35
2.566666666666667
2.966666666666667
2.316666666666667
2.216666666666667
2.1

'''
movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

#Escribir solucion aqui