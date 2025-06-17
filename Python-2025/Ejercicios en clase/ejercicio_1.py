'''Una tienda de productos tecnológicos maneja la siguiente información:
● Productos: Smartphone, Laptop, Tablet, Smartwatch
● Precios (USD): 300, 800, 150, 200
● Stock disponible (unidades):
○ Smartphone: 25
○ Notebook: 12
○ Tablet: 8
○ Smartwatch: 4
Se solicita desarrollar un algoritmo que:
1. Imprima el nombre y precio del artículo más caro y del más barato, utilizando métodos
de Python visto en clases.
2. Para cada artículo, muestre su categoría de precio según las siguientes condiciones:
● Producto Económico: precio < 200
● Producto Estándar: 200 ≤ precio ≤ 500
● Producto Premium: precio > 500
3. Liste los artículos con stock bajo (menos de 10 unidades).
'''

# Productos

productos = ['Smartphone', 'Laptop', 'Tablet', 'Smartwatch']
valores = [300, 800, 150, 200]
stock = {
    'Smartphone': 25,
    'Laptop': 12,
    'Tablet': 8,
    'Smartwatch': 4
}

# Min-Max
max_precio = max(valores)
min_precio = min(valores)

# Nombre productos más caro y más barato
prod_max = productos[valores.index(max_precio)]
prod_min = productos[valores.index(min_precio)]

print(f'El artículo más caro es {prod_max}, con un valor de {max_precio}')
print(f'El artículo más caro es {prod_min}, con un valor de {min_precio}')

# Establecer el tipo de producto
for prod, precio in zip(productos, valores):
    if precio < 200:
        categoria = 'Producto Económico'
    elif precio >= 200 and precio <= 500:
        categoria = 'Producto Estándar'
    else:
        categoria = 'Producto Premium'
    print(f'{prod}: ${precio} -> {categoria}')

for prod, cantidad in stock.items():
    if cantidad < 10:
        print(f'{prod}: {cantidad} unidades')
