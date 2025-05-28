# CREANDO SETS 
colores = {'Azul', 'Rojo', 'Azul', 'Verde'} # NO TIENEN ORDEN
colorcitos = {'Azul', 'Naranjo'}
'''print(colores[0]) AL NO TENER ORDEN, NO SE PUEDE DETERMINAR LA POSICIÓN'''

#IMPRIMIENDO EL SET COLORES
print(colores)

# AGREGANDO UN NUEVO ELEMENTO AL SET
colores.add('Blanco')
print(colores)

# ELIMINANDO UN ELEMENTO DEL SET
colores.discard('Blanco')
print(colores)

# APLICANDO EL MÉTODO DIFFERENCE
diferencia = colores.difference(colorcitos)
print(diferencia)