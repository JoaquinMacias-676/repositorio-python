a = 100
print(f'El valor de a es {a}')

b = a
print(f'El valor de b es {b}')

a = 200
print(f'El valor de a es {a} y el valor de b es {b}') # aunque "a" cambié, "b" no va a cambiar

bencina = True
encendido = True
edad = 19

# Utilizando el operador AND
if bencina and encendido:
    print('El vehículo puede avanzar')
else:
    print('El vehículo no puede arrancar')

#Utilizando el operador OR
if bencina or encendido:
    print('El vehículo no puede avanzar')
else:
    print('El vehículo no puede arrancar')

#Declarando variables de tipo entero
a = 10
b = 5
c = 4
d = 10

# Operaciones Comunes
print('########')
print(a == b) #igual a
print(a != b) #a no es igual a b