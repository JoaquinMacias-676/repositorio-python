'''Clasificador de edades

Pide al usuario ingresar varias edades (una por línea) hasta que escriba "stop".

Clasifica las edades en: niño (0-12), adolescente (13-17), adulto (18-64) y adulto mayor (65+).

Usa while, if/elif/else y contadores por categoría.'''

niños = 0
adolescentes = 0
adultos = 0
adultos_mayores = 0

print('')

while True:
    edad = input('Ingrese una edad, cuando quiera deternerse escriba la palabra "stop": ')
    if edad.lower() == str('stop'):
        break
    try:
        if int(edad) >= 0 and int(edad) <= 12:
            niños +=1 
        elif int(edad) > 12 and int(edad) <= 17:
            adolescentes += 1
        elif int(edad) > 17 and int(edad) <= 64:
            adultos += 1
        elif int(edad) < 0:
            print('Ingrese un número mayor o igual a 0, o escriba "stop')
        else:
            adultos_mayores += 1
    except ValueError:
        print('Valor Ingresado incorrecto, ingrese una edad o escriba "stop"')

print(f'\nNiños totales: {niños}')
print(f'Adolescentes totales: {adolescentes}')
print(f'Adultos totales: {adultos}')
print(f'Adultos Mayores totales: {adultos_mayores}\n')
