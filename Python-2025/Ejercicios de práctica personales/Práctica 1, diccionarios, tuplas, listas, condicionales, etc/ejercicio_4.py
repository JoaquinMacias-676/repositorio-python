'''Solicita al usuario una edad y muestra un mensaje:

Si es menor de 18: “Menor de edad”

Si es 18 o más: “Mayor de edad”'''

edad = int(input('\nIngrese su edad para saber si es mayor de edad o no: '))

if edad > 1 and edad < 18:
    print(f'Usted tiene {edad} años, es menor de edad.\n')
elif edad == 1:
    print(f'Usted tiene {edad} año, es menor de edad.\n')
elif edad == 0:
    print(f'{edad} no es un número viable para una edad.')
elif edad >= 18 and edad <= 120:
    print(f'Usted tiene {edad} años, es mayor de edad.\n')
elif edad < 0:
    print(f'{edad} no es número válido para una edad.\n')
elif edad > 120:
    print(f'{edad} es un número demasiado alto.\n')