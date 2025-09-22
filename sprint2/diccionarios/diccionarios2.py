clients = [
    [32456, "Jack Wilson", 31, 150000, "Healthcare"],
    [34591, "Nina Brown", 43, 250000, "Telecom"],
    [37512, "John Smith", 32, 210000, "IT"],
    [39591, "Brian Perez", 49, 340000, "Healthcare"],
    [45123, "Brian Lee", 48, 75000, "Telecom"],
    [47635, "David Chen", 56, 180000, "Telecom"],
    [49571, "Brian Chen", 52, 220000, "IT"],
    [50391, "David Rodriguez", 31, 120000, "IT"],
    [34556, "Lucas Hernandez", 37, 180000, "Healthcare"]
]

incomes_per_field = {} # aquí colocarás los ingresos para cada campo

for client in clients:
    campo=client[4]
    ingresos=client[3]
    if campo not in incomes_per_field.keys():
        incomes_per_field[campo]=[ingresos]
    else:
        incomes_per_field[campo]+=[ingresos]# si el campo extraído está en el diccionario incomes_per_field
		# añade el nuevo ingreso a la lista de ingresos para un campo en particular