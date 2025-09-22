'''
Programa una función, llamada filter_clients, que permita filtrar una lista de clientes según el área de trabajo del cliente. Por ejemplo, “IT”. 

Para ello, tu función deberá:

Recibir dos parámetros: la lista de clientes con la que deberá trabajar y el work_field que estoy buscando filtrar.
Definir dentro de la función una variable llamada field, la cual almacenará el área de trabajo por el que se busca
filtrar a los clientes. Utiliza el valor "Finance".
Recorrer cada cliente de la lista. Si se encuentra uno que coincida con el campo a filtrar, la información de este
cliente se debe añadir a una nueva lista.
Esta nueva lista se devolverá como resultado de ejecutar la función cuando se termine de recorrer la lista completa de clientes.
El resultado esperado es este:

[[47635, 'David Kim', 36, 180000, 'Finance'], [104556, 'William Brown', 38, 289000, 'Finance']]
'''


clients_list = [
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]]

#!Nota lee con atencion ya que yo andaba segmentando la lista desde el inicio cuado claramente
#!Las instrucciones mencionan pasar como parametro la lista completa y la palabra filtro 

def filter_clients(clients,work_field):
    filtro_clientes=[]
    for x in clients:
        if x[4]==work_field:
            filtro_clientes.append(x)
    return filtro_clientes

print(f"Lista filtrada por los que trabajan en Finance\n{filter_clients(clients_list,'Finance')}\n") #Ojito con los parentesis

print(f"Lista filtrada por los que trabajan en Architecture\n{filter_clients(clients_list,'Architecture')}")
