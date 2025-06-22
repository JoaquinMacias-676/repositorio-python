# Dado el siguiente conjunto de notas:
# notas = [4.5, 5.0, 4.5, 6.0, 6.0, 7.0]
# Utiliza un set para eliminar los duplicados y calcula el promedio de las notas únicas.

notas = [4.5, 5.0, 4.5, 6.0, 6.0, 7.0]

notas_no_repetidas = set(notas)

promedio = sum(notas_no_repetidas) / len(notas_no_repetidas)

print(f'La lista de las notas son: {notas}')
print(f'La lista de las notas únicas son: {notas_no_repetidas}')
print(f'El promedio de las notas únicas es: {promedio:.2f}')