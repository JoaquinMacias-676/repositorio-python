'''1. Crear un algoritmo que sirva de Conversor de Temperatura:
A. Solicitar por consola una temperatura en grados Celsius (números flotantes)
B. Calcular su equivalente en grados Fahrenheit y Kelvin utilizando las fórmulas
correspondientes.
C. Mostrar los tres valores en pantalla, redondeados a 2 decimales.'''

temperatura_c = int(input("Ingrese una temperatura en grados Celsius: "))

temperatura_k = temperatura_c + 274.15

temperatura_f = (temperatura_c*9/5) + 32

print(f'La temperatura en grados Fahrenheit es {round(temperatura_f, 2)}° F')

print(f'La temperatura en grados Kelvin es {round(temperatura_k, 2)}° K')