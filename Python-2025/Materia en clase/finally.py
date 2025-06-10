import os
print("Directorio de trabajo actual:", os.getcwd()) # Muestra la ubicación del directorio actual

try:
    archivo = open("Python-Ulagos-2025/Data/datos.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print("Lectura exitosa.")
finally: #Acción de Limpieza: cerrar el archivo si fue abierto
    try:
        archivo.close()
        print("Archivo cerrado.")
    except NameError:
        print("No fue necesario cerrar el archivo.")