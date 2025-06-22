# Ejercicio 7

# Lista en la que guardar los predecesores del número ingresado, junto con el mismo número
predecesores = []

# Solicitud de número al cual buscar su factorial
numero = int(input('\nIngrese un número para poder calcular su factorial: '))

# Predecesores del número y el número
for i in range(1, numero + 1):
    predecesores.append(i)

# Variable con valor de 1 para el segundo bucle
multi = 1

# Bucle del factorial del número
for n in predecesores:
    multi = multi * n

# Impresión del factorial del número ingresado
print(f'\nEl factorial del número {numero} es {multi}\n')
