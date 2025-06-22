# Ejercicio 3

# Sueldo base en Chile 2025
sueldo_base = 529000

# Diccionario de los vendedores
tienda = {
    'Juan': [150000, 200000, 300000, 220000, 180000],
    'Sergio': [400000, 200000, 280000, 300000, 350000],
    'Roberto': [150000, 100000, 180000, 250000, 200000]
}

print('\n===============================| REPORTE: SUELDOS A PAGAR |===============================\n')

# Bucle para conseguir las ventas y sus promedios
for vendedor, ventas in tienda.items():
    suma = sum(ventas)
    promedio = suma / len(ventas)

# Calculo del bono correspondiente
    if suma > 500000:
        bono = 0
    if suma > 1000000:
        bono = 0.05
    if suma > 1500000:
        bono = 0.1
    else:
        bono = 0.20

# Calculo del sueldo más el bono (si es que hay)
    sueldo = sueldo_base + sueldo_base * bono

# Impresión de resultados
    if bono == 0:
        print(f'|El vendedor {vendedor} no tiene ningún bono, por lo cual su sueldo es de ${int(sueldo)} CLP|')
    else:
        print(f'|El vendedor {vendedor} cuenta con un bono del {int(bono*100)}%, por lo que su sueldo es de: ${int(sueldo)} CLP|')

# Print decorativo
print('\n==========================================================================================\n')
