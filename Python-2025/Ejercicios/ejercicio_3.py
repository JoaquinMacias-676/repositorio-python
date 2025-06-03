'''Crear un algoritmo que permita manipular cadenas de texto:
A. Ingresar una frase de máximo 30 caracteres.
B. Generar dos nuevas variables: una en mayúsculas y otra en minúsculas.
C. Utilizar un método propio para determinar cuántas veces aparece la letra «a» (tanto «a»
como «A») en la frase, y muestra el total.
D. Emplear otro método para imprimir la longitud de la frase original.'''

# INGRESO DE FRASE MEDIANTE CONSOLA
frase = str(input('Ingrese una frase, que tendrá como máximo 30 caracteres: '))[0:30]

# FRASE CON VARIABLES EN MAYÚSCULAS Y MINÚSCULAS
mayor = frase.upper()

menor = frase.lower()

# CONTADORES DE "a" Y "A"
cantidad_a = frase.count('a')

cantidad_A = frase.count('A')

# IMPRESIÓN DE FRASES

print(f'La frase con variables en mayúsculas es: {mayor}')

print(f'La frase con variables en minúsculas es: {menor}')

print(f'Hay un total de {cantidad_a} "a"')

print(f'Hay un total de {cantidad_A} "A"')

print(f'Longitud de la frase: {len(frase)}')