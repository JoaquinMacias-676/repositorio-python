# JOAQUÍN MACÍAS Y DAYANA LEVICOY

# RESUMEN INGRESADO MEDIANTE CONSOLA
resumen = str(input('Ingrese un resumen: '))

# VERIFICACIÓN DE RESUMEN (SI CUMPLE CON EL LÍMITE DE 50)
boleano_resumen = len(resumen) <= 50

# CONTADOR DE VECES QUE APARECE "e"
num_e = resumen.count('e')

# IMPRESIÓN DE SI EL RESUMEN CUMPLE CON LOS LÍMITES
print(f'¿El resumen cumple con el límite?: {boleano_resumen}')

# IMPRESIÓN DE LONGITUD DEL RESUMEN
print(f'La longitud del resumen es de: {len(resumen)} caracteres')

# IMPRESIÓN DE RESUMEN EN MAYÚSCULAS
print(f'Resumen en mayúsculas: {resumen.upper()}')

# IMPRESIÓN DE RESUMEN EN MINÚSCULAS
print(f'Resumen en minúsculas: {resumen.lower()}')

# IMPRESIÓN DE VECES QUE APARECE LA VOCAL "e"
print(f'Número de veces que aparece la vocal e {num_e}')

# INTENTO DE IMPRESIÓN
print(f'Mostrar los primeros 15 caracteres {resumen[14]}')
#print(f'Mostrar los últimos 15 caracteres {}')
#print(f'Resumen con sus palabras unidas con coma {resumen.}')