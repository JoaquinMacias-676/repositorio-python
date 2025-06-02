'''Crear un algoritmo que permita manipular cadenas de texto:
A. Ingresar una frase de máximo 30 caracteres.
B. Generar dos nuevas variables: una en mayúsculas y otra en minúsculas.
C. Utilizar un método propio para determinar cuántas veces aparece la letra «a» (tanto «a»
como «A») en la frase, y muestra el total.
D. Emplear otro método para imprimir la longitud de la frase original.'''

frase = str(input('Ingrese una frase, que tendrá como máximo 30 caracteres: '))[0:30]

mayor = frase.upper(3)
menor = frase.lower(1)

cantidad_a = frase.count('a')
cantidad_A = frase.count('A')

print(frase)

print('a')

print('A')