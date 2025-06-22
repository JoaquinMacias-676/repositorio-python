# JOAQUÍN MACÍAS Y DAYANA LEVICOY

# RESUMEN INGRESADO MEDIANTE CONSOLA
resumen = str(input('\nIngrese un resumen: '))

# VERIFICACIÓN DE RESUMEN (SI CUMPLE CON EL LÍMITE DE 50)
boleano_resumen = len(resumen) <= 50

# CONTADOR DE VECES QUE APARECE "e"
num_e = resumen.count('e')

# RESUMEN CON COMAS
comas = resumen.split()

# IMPRESIÓN DE SI EL RESUMEN CUMPLE CON LOS LÍMITES
print(f'\n¿El resumen cumple con el límite?: {boleano_resumen}')

# IMPRESIÓN DE LONGITUD DEL RESUMEN
print(f'\nLa longitud del resumen es de: {len(resumen)} caracteres')

# IMPRESIÓN DE RESUMEN EN MAYÚSCULAS
print(f'\nResumen en mayúsculas:\n{resumen.upper()}\n')

# IMPRESIÓN DE RESUMEN EN MINÚSCULAS
print(f'Resumen en minúsculas:\n{resumen.lower()}\n')

# IMPRESIÓN DE VECES QUE APARECE LA VOCAL "e"
print(f'Número de veces que aparece la vocal e: {num_e}')

# INTENTO DE IMPRESIÓN
print(f'\nMostrar los primeros 15 caracteres: {resumen[:15]}')
print(f'\nMostrar los últimos 15 caracteres: {resumen[-15:]}')
print(f'\nResumen con sus palabras unidas con coma: {comas}\n')