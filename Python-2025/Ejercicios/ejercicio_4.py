'''Desarrollar un programa de gestión de inventario:
A. Ingresar el nombre de un producto y su precio unitario.
B. Ingresar la cantidad en stock.
C. Calcular el valor total de los productos ingresados y mostrarlo con 2 decimales.
D. Crear una variable booleana llamada umbral, que entregue un True si el valor_total >
100000 y False en caso contrario..
E. Imprimir el nombre del producto, la cantidad, el valor total y el estado umbral en un solo
print() formateado.'''

# INGRESO DE VALORES POR CONSOLA
producto = input('Ingrese el nombre del producto: ')

precio = int(input('Ingrese el precio del producto: ' ))

stock = int(input('Ingrese la cantidad de stock de la cual se dispone: '))

# CÁLCULO Y UMBRAL
valor_total = precio * stock

umbral = int(valor_total) > 100000

# IMPRESIÓN
print(f'El nombre del producto es "{producto}", con una cantidad de {stock} y dando como valor total ${valor_total:.2f} CLP y con un estado umbral = {umbral}')