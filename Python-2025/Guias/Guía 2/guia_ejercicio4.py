# Ejercicio 4

# Pedir al usuario el valor de n
n = int(input("Ingrese el valor de n: "))

# Inicializamos el primer número impar
impar = 1

# Bucle para calcular los primeros n cubos
for i in range(1, n + 1):
    suma = 0
    sumas = []

    # Se suman los siguientes i impares
    for _ in range(i):
        suma += impar
        sumas.append(impar)
        impar += 2

# Resultado
suma_texto = ' + '.join(str(num) for num in sumas)
print(f"{n}^3 = {suma_texto} = {suma}")
