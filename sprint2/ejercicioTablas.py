'''
Ejercicio 1
Es el Día de la Juventud, y el equipo de marketing quiere enviar un correo especial dirigido a nuestros clientes jóvenes.

Tu tarea es aplicar nuevos filtros combinados de ingresos y edad para clasificar a los clientes en dos nuevas categorías:

elite_young: Clientes con un ingreso anual entre $200.000 (exclusive) y $300.000 (inclusive) y edad menor a 35 años.
executive_young: Clientes con un ingreso anual superior a $300.000 (exclusive) y edad menor a 35 años.
Deberás actualizar el filtrado de los clientes utilizando estas reglas y asignarlos a la lista correspondiente.

Al final, imprime únicamente la lista executive_young.

El resultado esperado es este: 

[[39591, 'Brian Perez', 29, 340000, 'Transportation']]

'''

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"]
]

elite_young=[]
executive_young=[]
for cliente in clients:
    if cliente[2]<35 and (cliente[3]>=200000 or cliente[3]<300000): # interesante como lo resolvio dilan con intervalor 200000 <client[3]<=300000
        elite_young.append(cliente)
    if cliente[2]<35 and cliente[3]>=300000:
        executive_young.append(cliente)
print(f"Cliente ejecutivos")

print(executive_young)