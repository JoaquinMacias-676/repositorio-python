# Ejemplo: Búsquedad de un número primo

for n in range(2, 11):
    for i in range(2, n):
        if n % i == 0:
            print(f'{n} es un número compuesto, divisible por {i}')
            break