# Ejercicio 2

# Inicializar la sumatoria en 0
s = 0

# Inicializar a y b desde el primer número que aparece en la sumatoria
a = 500
b = 456

# Bucle que hace la sumatoria hasta que a (que empieza en 500) sea igual o menor que 800, sin que se pase de 800
while a <= 800:
    s += a + b
    a += 10
    b -= 2

# Impresión del resultado
print(f'\nLa sumatoria es: {s}\n')