# INTEGRANTES: JOAQUÍN MACÍAS, DAYANA LEVICOY

# INGRESO DE PRECIOS Y CANTIDADES MEDIANTE CONSOLAS (MARTILLO)
precio_m = float(input('Ingrese el valor del Martillo: '))
cantidad_m = int(input('Ingrese la cantidad que hay del producto "Martillo": '))

# INGRESO DE PRECIOS Y CANTIDADES MEDIANTE CONSOLAS (CLAVOS)
precio_c = float(input('Ingrese el valor de los Clavos: '))
cantidad_c = int(input('Ingrese la cantidad que hay del producto "Clavos": '))

# INGRESO DE PRECIOS Y CANTIDADES MEDIANTE CONSOLAS (SERRUCHO)
precio_s = float(input('Ingrese el valor del Serrucho: '))
cantidad_s = int(input('Ingrese la cantidad que hay del producto "Serrucho": '))

# INGRESO DE PRECIOS Y CANTIDADES MEDIANTE CONSOLAS (TORNILLOS)
precio_t = float(input('Ingrese el valor de los Tornillos: '))
cantidad_t = int(input('Ingrese la cantidad que hay del producto "Tornillos": '))

# CÁLCULO DE SUBTOTAL MARTILLO
subtotal_m = precio_m * cantidad_m

# CÁLCULO DE SUBTOTAL CLAVOS
subtotal_c = precio_c * cantidad_c

# CÁLCULO DE SUBTOTAL SERRUCHO
subtotal_s = precio_s * cantidad_s

# CÁLCULO DE SUBTOTAL TORNILLOS
subtotal_t = precio_t * cantidad_t

# SUMA DE SUBTOTALES
sum_totales = subtotal_m + subtotal_c + subtotal_s + subtotal_t

# IVA APLICADO A LOS SUBTOTALES
iva_subtotales = sum_totales + (sum_totales * 19/100)

# PROMEDIO PRECIOS UNITARIOS
prom_unitario = (precio_m + precio_c + precio_s + precio_t)/4

# IMPRESIÓN SUBTOTALES
print(f'Subtotal Martillo: ${round(subtotal_m, 2)} CLP | Subtotal Clavos: ${round(subtotal_c, 2)} CLP | Subtotal Serrucho: ${round(subtotal_s, 2)} CLP | Subtotal Tornillos: ${round(subtotal_t, 2)} CLP')

# IMPRESIÓN DE VALOR TOTAL DE SUBTOTALES
print(f'Valor total de los Subtotales: ${sum_totales} CLP')

# IMPRESIÓN DE MÁXIMO Y MÍNIMO ENTRE LOS 4 SUBTOTALES
print(f'El máximo entre los 4 subtotales es de: ${max(subtotal_m, subtotal_c, subtotal_s, subtotal_t)} CLP')

print(f'El minimo entre los 4 subtotales es de: ${min(subtotal_m, subtotal_c, subtotal_s, subtotal_t)} CLP')

# IMPRESIÓN DE PROMEDIO SUBTOTALES
print(f'El promedio de los Subtotales: ${round(prom_unitario, 2)} CLP')

print(f'Valor total de los Subtotales con el IVA (19%) aplicado: ${iva_subtotales} CLP')