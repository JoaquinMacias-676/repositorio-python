'''Contador de números pares

Pide al usuario un número entero positivo n.

Imprime todos los números pares del 0 al n.

Usa for y un condicional if.'''

try:
    numero = int(input('\nIngrese un número entero positivo: '))
    if numero > 0:
        print(f'\nNúmero ingresado: {numero}')
        print('\nNúmeros pares:')
        for i in range(1, numero + 1):
            if i % 2 == 0:
                print(i)
except ValueError:
    print('\nEl valor ingresado es incorrecto\n')
