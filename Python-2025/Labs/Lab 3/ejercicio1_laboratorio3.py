# Creando el diccionario
cod_postal = {
        int(5700000) : {
        'Ciudad': str('Castro'),
        'Temperatura Promedio Anual': float(11.8),
        'Precipitación Total': int(2000)
    },
        int(5770000) : {
        'Ciudad': str('Chonchi'),
        'Temperatura Promedio Anual': float(8.3),
        'Precipitación Total': int(2800)
    },
        int(5790000) : {
        'Ciudad': str('Quellón'),
        'Temperatura Promedio Anual': float(10.2),
        'Precipitación Total': int(2950)
    },
}

# Imprimiendo la primera versión del diccionario
print(f'\nLa primera versión del diccionario es:\n\n{cod_postal}')

# Implementando la clave 'Clima' en el sub-diccionario de Castro, y asignandole su valor
try:
    if cod_postal[int(5700000)]['Temperatura Promedio Anual'] < 10:
        cod_postal[int(5700000)]['Clima'] = 'Frio'
    elif cod_postal[int(5700000)]['Temperatura Promedio Anual'] >= 10 and cod_postal[int(5700000)]['Temperatura Promedio Anual'] <= 15:
        cod_postal[int(5700000)]['Clima'] = 'Templado'
    else:
        cod_postal[int(5700000)]['Clima'] = 'Cálido'
except:
    ValueError('Desconocida')

# Implementando la clave 'Clima' en el sub-diccionario de Chonchi, y asignandole su valor
try:
    if cod_postal[int(5770000)]['Temperatura Promedio Anual'] < 10:
        cod_postal[int(5770000)]['Clima'] = 'Frio'
    elif cod_postal[int(5770000)]['Temperatura Promedio Anual'] >= 10 and cod_postal[int(5770000)]['Temperatura Promedio Anual'] <= 15:
        cod_postal[int(5770000)]['Clima'] = 'Templado'
    else:
        cod_postal[int(5770000)]['Clima'] = 'Cálido'
except:
    ValueError('Desconocida')

# Implementando la clave 'Clima' en el sub-diccionario de Quellón, y asignandole su valor
try:
    if cod_postal[int(5790000)]['Temperatura Promedio Anual'] < 10:
        cod_postal[int(5790000)]['Clima'] = 'Frio'
    elif cod_postal[int(5790000)]['Temperatura Promedio Anual'] >= 10 and cod_postal[int(5790000)]['Temperatura Promedio Anual'] <= 15:
        cod_postal[int(5790000)]['Clima'] = 'Templado'
    else:
        cod_postal[int(5790000)]['Clima'] = 'Cálido'
except:
    ValueError('Desconocida')

# Creando lista vacía
lista_castro = []

# Creando lista con los meses
lista_meses = ['Mayo', 'Junio', 'Julio']

# Implementando una una clave al sub-diccionario de Castro
cod_postal[int(5700000)]['Meses más lluviosos'] = lista_castro

# Agregando la lista de los meses a la lista vacía
lista_castro.append(lista_meses)

# Eliminando el mes de julio de la lista
lista_meses.pop(1)

# Actualizando el valor de Ciudad en el codigo postal "5770000" para que sea "Ciudad de los Tres Pisos"
cod_postal[int(5770000)]['Ciudad'] = 'Ciudad de los Tres Pisos'

# Creando lista de Lluvias
lluvias = [cod_postal[int(5700000)]['Precipitación Total'], cod_postal[int(5770000)]['Precipitación Total'], cod_postal[int(5790000)]['Precipitación Total']]

# Suma de precipitaciones
suma_lluvias = sum(lluvias)

# La mayor y menor precipitación entre todas
mayor_p = max(lluvias)
menor_p = min(lluvias)

# Posición de la precipitación más alta
posicion = lluvias.index(mayor_p)

# Imprimiendo lo solicitado
print('\n############### RESULTADOS ###############')
print(f'\n- La suma de las precipitaciones de las tres ciudades da como resultado: {suma_lluvias} (mm)')
print(f'- La mayor precipitación entre las tres ciudades es de: {mayor_p} (mm)')
print(f'- La menor precipitación entre las tres ciudades es de: {menor_p} (mm)')
print(f'- La posición de la precipitación más alta en la lista es la número: {posicion}')

# Imprimiendo la segunda versión del diccionario
print(f'\nLa segunda versión del diccionario es:\n\n{cod_postal}\n')

# Lista de tuplas
lista_tuplas = cod_postal.items()

# Imprimiendo lista de tuplas
print(f'La lista de tuplas con las claves y valores del diccionario es: \n\n{lista_tuplas}\n')