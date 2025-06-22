'''Tabla de multiplicar

Solicita un número del 1 al 10.

Muestra la tabla de multiplicar de ese número hasta el 10.

Usa un for y f-string para el formato.'''

try:
    numero = int(input('\nIngrese un número del 1 al 10 para generar su tabla de multiplicar: '))
    if numero < 1 or numero > 10:
        print('\nNúmero ingresado fuera del rango solicitado\n')
    else:
        print(f'\nLa tabla de multiplicar del número {numero} es:')
        for i in range(11):
            multi = numero * i
            print(f'{numero}*{i} = {multi}')
except ValueError:
    print('\nValor ingresado erroneo\n')
    