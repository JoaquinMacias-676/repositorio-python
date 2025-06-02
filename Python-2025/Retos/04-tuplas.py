# CREANDO UNA TUPLA
estudiantes = ('Samir', 'Matias', 'Hector', 'Pia', 'Carlos')

# CREANDO OTRA TUPLA (CON DATOS ESTRUTURADOS)
tuplita = ([1,2,3,4,5],('Santiago', 'Viña'), {'Manzana', 'Piña'})

# IMPRIMIENDO LAS TUPLAS
print(estudiantes)
print(tuplita)
# ELIMINANDO EL ÚLTIMO ELEMENTO DE LA TUPLA (NO SE PUEDE -> INMUTABLE)
'''estudiantes.pop()
print(estudiantes)'''

'''estudiantes = ('Constanza')
print(estudiantes)'''

# MÉTODO INDEX EN TUPLAS (INDICA LA POSICIÓN DEL ELEMENTO)
print(estudiantes.index('Carlos'))

# MÉTODO SORTED EN TUPLAS (ORDENA LOS ELEMENTOS DE UNA TUPLA, VOLVIENDOLO UNA LISTA)
print(sorted(estudiantes))