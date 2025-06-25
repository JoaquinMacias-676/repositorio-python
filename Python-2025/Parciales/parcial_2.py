# Creando diccionario de la clínica
clinica = {
    int(101): {
        'Nombre': 'Luna',
        'Peso': float(1.2),
        'Edad': int(3),
        'Tamaño': int(30)
    },
    int(102): {
        'Nombre': 'Michi',
        'Peso': float(0.8),
        'Edad': int(2),
        'Tamaño': int(25)
    },
    int(103): {
        'Nombre': 'Pepito',
        'Peso': float(2.5),
        'Edad': int(5),
        'Tamaño': int(35)
    }
}

# Impresión del diccionario
print(f'\n==== DICCIONARIO DE LA CLÍNICA ====\n')
print(clinica)

# Bucle para añadir nueva clave 'Clasificación-Peso', junto a su valor
for i in clinica:
    peso = clinica[i]['Peso']
    try:
        if peso < 1:
            clinica[i]['Clasificación-Peso'] = 'Peso Bajo'
        elif peso >=1 and peso <= 4:
            clinica[i]['Clasificación-Peso'] = 'Normal'
        else:
            clinica[i]['Clasificación-Peso'] = 'Sobre Peso'
    except:
        print('Desconocida')

# Bucle para añadir nueva clave 'Categoría-Etaria', junto a su valor
for i in clinica:
    edad = clinica[i]['Edad']
    try:
        if edad < 4:
            clinica[i]['Categoría-Etaria'] = 'Cachorro'
        elif edad >=4 and edad <= 12:
            clinica[i]['Categoría-Etaria'] = 'Joven'
        else:
            clinica[i]['Categoría-Etaria'] = 'Adulto'
    except:
        print('Desconocida')


# Creando lista de tuplas
lista_tuplas = []

for a in clinica:
    peso2 = clinica[a]['Peso']
    tupla = (a, peso)
    lista_tuplas.append(tupla)
    
print(f'Lista de tuplas: {lista_tuplas}')

# Bucle para ingresar un nuevo gatito
while True:
    print('Ingrese datos para agregar otro gatito\n')
    n_ingreso = int(input('Ingrese el número de ingreso de su gatito: '))
    nombre = str(input('Ingrese el nombre del gatito: '))
    peso_gato = float(input('Ingrese le peso del gatito: '))
    edad_gato = int(input('Ingrese la edad del gatito: '))
    tamaño = int(input('Ingrese el tamaño del gatito: '))
    clinica[n_ingreso] = {
        'Nombre': nombre,
        'Peso': peso_gato,
        'Edad': edad_gato,
        'Tamaño': tamaño     
    }
    otro_gato = str(input('¿Desea agregar otro gatito? (si/no): '))
    if otro_gato == str('no'):
        break

# Lista de pesos
lista_pesos = []

# Bucle para agregar el ingreso y sus pesos
for e in clinica:
    pesos = clinica[i]['Peso']
    lista_pesos.append(pesos)

# Calculos para la lista
suma_lista = sum(lista_pesos)
promedio_lista = suma_lista / len(lista_pesos)
max_peso = max(lista_pesos)
min_peso = min(lista_pesos)

# Impresión de resultados
print(f'\nPromedio de pesos: {promedio_lista}Kg')
print(f'La suma de todos los pesos es igual a: {suma_lista}Kg')
print(f'El peso máximo es de: {max_peso}Kg')
print(f'El peso mínimo es de: {min_peso}Kg\n')

# Impresión de diccionario final
print('==== DICCIONARIO FINAL DE LA CLÍNICA ====\n')
print(clinica)