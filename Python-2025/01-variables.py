"""GUIA INICIAL DE PYTHON
DE VARIABLES - ULAGOS 2025""" #comentario multilinea

nombre = "Joaquin"
apellido = "Macias"

# UTILIZANDO VARIABLES EN UN PRINT CON COMAS
print("Hola mi nombre es" , nombre, "y mi apeliido es", apellido) 

# IMPRIMIENDO CON OPERADOR DE CONCATENACION
print("Hola mi nombre es " + nombre + " y mi apellido es " + apellido)

# IMPRIMIENDO CON F-STRINGS (CADENAS LITERALES)
print(f"Hola mi nombre es {nombre} y mi apellido es {apellido}")

# INICIALIZANDO MULTI VARIABLES EN UNA SOLA LINEA (no recomendable, ya que es más dificil encontrar errores)
ciudad, region, pais = "Castro", "Los Lagos", "Chile"
print(f"Hola soy de {ciudad}, {region}, {pais}")

peso = 75
edad = 31