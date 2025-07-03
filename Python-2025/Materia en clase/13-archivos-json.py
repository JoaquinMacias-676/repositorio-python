import json # Manipulación de archivos json
import os # métodos para trabajar con el sistema operativo (SO)

ruta = os.path.join("JSON", "datos.json") # ruta relativa => JSON/datos.json

# LECTURA DE ARCHIVO JSON
print("\n====== LECTURA DEL JSON ======")

# r de read 
# utf-8 = los caracteres que usa nuestro idioma, a diferencia de otros que no usan la ñ por ejemplo
with open(ruta, "r", encoding='utf-8') as archivo:
    datos = json.load(archivo) # Convierte el archivo json en una estructura de Python

for usuario in datos:
    print(f"\nID: {usuario['id']}, Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")

# ESCRITURA DE ARCHIVO JSON
print("\n====== ESCRITURA DEL JSON ======")

# Agregar un nuevo usuario
nuevo_usuario = {
    "id": 5,
    "nombre": "Fernanda",
    "edad": 30
}

datos.append(nuevo_usuario)

# Guardar los cambios en el archivo JSON utilizando json.dump
# w = write
with open(ruta, "w", encoding='utf-8') as archivo:
    json.dump(
        datos,
        archivo,
    )