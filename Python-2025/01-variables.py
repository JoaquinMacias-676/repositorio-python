"""GUIA INICIAL DE PYTHON
DE VARIABLES - ULAGOS 2025""" #comentario multilinea

# 01 - DECLARANDO E INICIALIZANDO VARIABLES
nombre = "Joaquin"
apellido = "Macias"

# 02 - IIPRESIÓN DE VARIABLE

# 03 - UTILIZANDO MÁS DE UNA VARIABLE EN UN PRINT
print("Hola mi nombre es" , nombre, "y mi apeliido es", apellido) 

# 04 - IMPRIMIENDO CON OPERADOR DE CONCATENACION
print("Hola mi nombre es " + nombre + " y mi apellido es " + apellido)

# 05 - IMPRIMIENDO CON F-STRINGS (CADENAS LITERALES)
print(f"Hola mi nombre es {nombre} y mi apellido es {apellido}")

# 06 -INICIALIZANDO MULTI VARIABLES EN UNA SOLA LINEA (no recomendable, ya que es más dificil encontrar errores)
ciudad, region, pais = "Castro", "Los Lagos", "Chile"
print(f"Hola soy de {ciudad}, {region}, {pais}")

peso = 75
edad = 31

# 07 - USO DEL INPUT
print(nombre)
nombre = input("Ingrese su nombre:\n")
print(f"Hola mi nombre es : {nombre}")

print(nombre)
