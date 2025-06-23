'''Generador de matriz y suma por fila

Crea una matriz de n filas y m columnas, donde cada valor es ingresado por el usuario.

Imprime la matriz y luego la suma de cada fila.

Usa bucles anidados y listas de listas.'''

filas = int(input('Ingrese el número de filas que tendrá la matriz: '))
columnas = int(input('Ingrese el número de columnas que tendrá la matriz: '))

matriz = []

for i in range(filas):
    fila = []
    print(f'\nFila {i + 1}:')
    for j in range(columnas):
        valor = int(input(f'Ingrese el valor para posición [{i+1},{j+1}]: '))
        fila.append(valor)
    matriz.append(fila)

print('\nMatriz:\n')
for fila in matriz:
    print(fila)