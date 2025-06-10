print('===== MENÚ =====')
print('1. Hamburguesa')
print('2. Pizza')
print('3. Completo Italiano')

opcion = input('Por favor, elige una opción (1-3): ')

match opcion:
    case "1":
        print("Has elegido una Hamburguesa. Precio: $5000")
    case "2":
        print("Has elegido una Pizza. Precio: $7500")
    case "3":
        print("Has elegido un Completo Italiano. Precio: $2500")
    case _:
        print("Opción no válida. Por favor, elige entre 1 y 3")

# Ejemplo: determinar estación según mes
mes = 4 # abril
match mes:
    case 12 | 1 | 2: # | es igual a or
        print("Verano")
    case 3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Invierno")
    case 9 | 10 | 11:
        print("Primavera")
    case _:
        print("Mes inválido")

# Ejemplo: saludo según hora del día
hora = 18 # formato 24 horas
match hora:
    case h if 0 <= h < 6:
        print("Buenas madrugadas")
    case h if 6 <= h < 12:
        print("Buenos dias")
    case h if 12 <= h < 18:
        print("Buenas tardes")
    case h if 18 <= h < 24:
        print("Buenas noches")
    case _:
        print("Hora inválida")

# Patrones Compuestos
x = [1, 2, 3]
match x:
    case [a, b, c]: # desagrupando valores de la lista x
        print(f"Elementos de la Lista x: {a}, {b}, {c}")

datos = {
    'nombre': 'Victor',
    'edad': 31
}
match datos:
    case {'nombre': n, 'edad': e}:
        print(f'Nombre: {n}, Edad: {e}')

# Guards
valor = 6
match valor:
    case x if x % 2 == 0:
        print(f"{valor} es un número Par")
    case x if x % 2 != 0:
        print(f"{valor} es un número Impar")