''' Crea un diccionario que almacene datos de un producto:
        producto = {
        "nombre": "Teclado",
        "precio": 18000,
        "stock": 35
        }
Aumenta el stock en 5 unidades y cambia el precio a $17.000. Luego imprime todos los valores usando values().'''

producto = {
    "nombre": "Teclado",
    "precio": 18000,
    "stock": 35
    }

producto["precio"] = 17000
producto["stock"] += 5

print(f'\nEl nuevo diccionario es {producto.values()}\n')

