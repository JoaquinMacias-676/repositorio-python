# CREANDO DICCIONARIO 
paciente = {
    'nombre': 'Carlos',
    'apellido': 'Santana',
    'edad': 50,
    'ciudad': 'Puerto Montt',
    'comuna': {'Alerce'},
    'consultas': [14, 20, 40],
    'diagnostico': ('resfrio'),
    'info_extra': {
        'tipo_de_sangre': 'A+',
        'hemorragia': 'Sin Datos'
    }
}

print(type(paciente))

# OTRA FORMA DE DECLARAR DICCIONARIO
medico = dict(
    nombre = 'Samir',
    apellido = 'Arana',
    edad = 20,
    especialidad = 'Neurologo'
)

#IMMPRESIÓN DE DICCIONARIOS
print(paciente)
print(medico)

# CONSULTANDO UN ELEMENTO A TRAVÉS DE LA CLAVE DEL DICCIONARIO
print(medico['nombre'])

# ELIMINANDO UNA CLAVE DEL DICCIONARIO
del(paciente['nombre'])
print(paciente)