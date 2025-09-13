'''
Ejercicio
Tienes una lista anidada de pedidos en la que cada sublista contiene el precio, la cantidad y el descuento de un pedido.
Tienes que calcular los ingresos totales después de los descuentos y averiguar el valor más alto de un solo pedido.

Utiliza operadores de asignación aumentada para actualizar el valor de total_revenue y la función integrada de python
max() para obtener highest_order_total.

La salida esperada es esta:

Ingresos totales después de descuentos y tasas: 2332.4005
Valor máximo de un pedido: 849.966
'''

# Lista anidada de pedidos: [precio, cantidad, descuento]
orders = [
    [199.99, 2, 0.10],  # 10% de descuento
    [349.99, 1, 0.05],  # 5% de descuento
    [129.99, 3, 0.00],  # Sin descuento
    [499.99, 1, 0.20],  # 20% de descuento
    [249.99, 4, 0.15],  # 15% de descuento
]
# Inicializa las variables
total_revenue=0
highest_order_total=0


# Recorre los pedidos
for total in orders:
    print(total)


'''print(f"Ingresos totales despues de descuentos y tasas: {total_revenue}")
print(f"Valor maximo de un pedido es: {max(highest_order_total)}")'''



### AQUÍ VA TU CÓDIGO ###

    
# Salida: Ingresos totales después de descuentos y tasas: 2332.4005

# Salida: Valor de pedido único más alto: 849.966
