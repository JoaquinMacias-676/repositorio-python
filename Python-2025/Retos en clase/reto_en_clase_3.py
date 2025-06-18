# Inicializando la suma en 0
sum = 0
numeros = []

# Inicializando a en 500
a = 500

print('\nLos números del 500 al 100, decreciendo de 3 en 3 son: \n')

# Sumatoria del 500 al 100, decreciendo en 3
while a >= 100:
    print(a)
    a -= 3 
    sum += a + a
    numeros.append(a)

# Cantidad de números
cantidad = len(numeros)

# El promedio entre todos los números
promedio = sum / cantidad

# Impresión de lo solicitado

print('\n================ RESULTADOS ================')
print(f'\nLa suma de todos los números da como resultado: {sum}')
print(f'La cantidad de numeros que se suman es: {cantidad}')
print(f'El promedio es: {promedio}\n')