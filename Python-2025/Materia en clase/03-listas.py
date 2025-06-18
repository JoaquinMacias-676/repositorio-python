# LISTA COMPUESTA DE DATOS
lista1 = ['Victor', 31, True]
# print(lista1.index('Samir')) NO SE PUEDE

print(lista1)

# LISTA VACIA
frutas = ()

# LISTA DE SOLO NÚMEROS
n = [1, 2, 3, 4, 5] # DECLARANDO CON CORCHETES

# LISTA DE SOLO STRINGS - UTILIZANDO LA FUNCIÓN LIST
ramos = list(['Programación', 'Química', 'POO', 'Programación']) # DECLARANDO CON LA FUNCIÓN LIST

# IMPRIME LA POSICIÓN DEL PRIMER ELEMENTO DE LA LISTA (NO EL CARÁCTER)
print(ramos[0])

# MÉTODO COUNT ( CUENTA LA CANTIDAD DE CONCURRENCIAS DE UN ELEMENTO)
print(ramos.count('Programación'))

# MÉTODO APPEND
ramos.append('Introducción a la Matemática')
print(ramos)

# MODIFICAR ELEMENTOS A LA LISTA DE OTRA FORMA
ramos[0] = 'Comunicación' # estoy pasando la posición del elemento a modificar
print(ramos)

# OTRA FORMA DE INSERTAR UN ELEMENTO A LA LISTA (INSERT)
ramos.insert(0, 'Algebra') # A INSERT hay que entregarle dos elementos (parametros)
print(ramos)

#ELIMINAR EL ÚLTIMO ELEMENTO DE LA LISTA
ramos.pop() # No se puede especificar que eliminar, solo elimna el último
print(ramos)

# ORDENANDO ELEMENTOS DE UNA LISTA DE FORMA DESCENDENTE A ASCENDENTE
'''print(ramos.sort) No funciona '''
ramos.sort()
print(ramos)

# ORDENANDO ELEMENNTOS DE UNA LISTA SEGÚN LA CANTIDAD DE CARÁCTERES
ramos.sort(key=len)
print(ramos)

# OCUPANDO EL MÉTODO EXTEND (EXTENDIENDO UNA LISTA A PARTIR DE OTRA)
ramitos = ['Cálculo', 'Autómatas'] # Nueva lista creada
ramos.extend(ramitos) # Extiende la lista anterior (ramos), agregando los elementos de la lista (ramitos)
print(ramos)