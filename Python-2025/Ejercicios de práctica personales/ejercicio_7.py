'''Suma acumulada

Pide al usuario ingresar números uno a uno.

Finaliza cuando el usuario escribe "fin".

Muestra la suma total de los números ingresados.

Usa while, break y conversión de strings a int.'''

suma_numeros = 0

while True:
    numeros= input('Ingresa un número: ')
    if numeros == str('fin'):
        break
    else:
        suma_numeros += int(numeros)

print(f'La suma de los números da como resultado: {suma_numeros}')
    