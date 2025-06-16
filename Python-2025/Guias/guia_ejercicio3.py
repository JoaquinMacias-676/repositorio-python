'''Tres vendedores de una tienda de ropa deportiva registran sus ventas diarias durante 5
días. Los vendedores obtienen un bono por cierta cantidad de ventas realizadas durante
la semana:
Venta semanal total superior a $1.500.000 (Bono de un 20 % del sueldo base)
Venta semanal total superior a $1.000.000 (Bono de un 10 % del sueldo base)
Venta semanal total superior a $500.000 (Bono de un 5 % del sueldo base)
Ademas considerar: Sueldo Base en Chile 2025 es de $529.000
Se solicita:
a) Crea un diccionario donde la clave sea el nombre del vendedor y el valor otra estructura que guarde las ventas diarias (Puede ser una lista o tupla)
b) Calcula el total de las ventas semanales de cada vendedor y su bono si le corresponde.
c) Obtener el promedio de ventas semanales de cada vendedor.
d) Imprime un reporte con el total del sueldo a pagar por cada vendedor.
Los nombres de los vendedores y los valores de las ventas deben estar instanciado en
codigo (Hardcodeado).'''

# Lista de ventas de los vendedores
lista_juan = [150000, 200000, 300000, 220000, 180000]
lista_sergio = [400000, 200000, 280000, 300000, 350000]
lista_roberto = [150000, 100000, 180000, 250000, 200000]

# Sueldo base en Chile 2025
sueldo_base = 529000

# Total en la lista
sum_listajuan = sum(lista_juan)
sum_listasergio = sum(lista_sergio)
sum_listaroberto = sum(lista_roberto)

# Diccionario de los vendedores
tienda = {
    'Juan': lista_juan,
    'Sergio': lista_sergio,
    'Roberto': lista_roberto
}

print('####### REPORTE: SUELDOS A PAGAR #######\n')

# Impresión del sueldo de Juan
if sum_listajuan < 500000:
    print(f'|Juan no cuenta con ningún bono, su sueldo a pagar es de: ${sueldo_base} CLP|')
elif sum_listajuan >= 500000 and sum_listajuan < 1000000:
    sueldo_j5 = sueldo_base + (sueldo_base * 5/100)
    print(f'|Juan cuenta con un bono del 5%, su sueldo a pagar es de ${sueldo_j5} CLP|')
elif sum_listajuan >= 1000000 and sum_listajuan < 1500000:
    sueldo_j10 = sueldo_base + (sueldo_base * 10/100)
    print(f'|Juan cuenta con un bono del 10%, su sueldo a pagar es de ${sueldo_j10} CLP|')
elif sum_listajuan >= 1500000:
    sueldo_j20 = sueldo_base + (sueldo_base * 20/100)
    print(f'|Juan cuenta con un bono del 20%, su sueldo a pagar es de ${sueldo_j20} CLP|')

# Impresión del sueldo de Sergio
if sum_listasergio< 500000:
    print(f'|Sergio no cuenta con ningún bono, su sueldo a pagar es de: ${sueldo_base} CLP|')
elif sum_listasergio >= 500000 and sum_listasergio < 1000000:
    sueldo_s5 = sueldo_base + (sueldo_base * 5/100)
    print(f'|Sergio cuenta con un bono del 5%, su sueldo a pagar es de ${sueldo_s5} CLP|')
elif sum_listasergio >= 1000000 and sum_listasergio < 1500000:
    sueldo_s10 = sueldo_base + (sueldo_base * 10/100)
    print(f'|Sergio cuenta con un bono del 10%, su sueldo a pagar es de ${sueldo_s10} CLP|')
elif sum_listasergio >= 1500000:
    sueldo_s20 = sueldo_base + (sueldo_base * 20/100)
    print(f'|Sergio cuenta con un bono del 20%, su sueldo a pagar es de ${sueldo_s20} CLP|')

# Impresión del sueldo de Roberto
if sum_listaroberto< 500000:
    print(f'|Roberto no cuenta con ningún bono, su sueldo a pagar es de: ${sueldo_base} CLP|')
elif sum_listaroberto >= 500000 and sum_listaroberto < 1000000:
    sueldo_r5 = sueldo_base + (sueldo_base * 5/100)
    print(f'|Roberto cuenta con un bono del 5%, su sueldo a pagar es de ${sueldo_r5} CLP|')
elif sum_listaroberto >= 1000000 and sum_listaroberto < 1500000:
    sueldo_r10 = sueldo_base + (sueldo_base * 10/100)
    print(f'|Roberto cuenta con un bono del 10%, su sueldo a pagar es de ${sueldo_r10} CLP|')
elif sum_listaroberto >= 1500000:
    sueldo_r20 = sueldo_base + (sueldo_base * 20/100)
    print(f'|Roberto cuenta con un bono del 20%, su sueldo a pagar es de ${sueldo_r20} CLP|')