# Ejercicio 1

try:
    # Solicitar el parrafo
    parrafo = input('Ingrese un párrafo, por favor: ')

    if parrafo == "":
        raise ValueError()

    # Separar las palabras y ponerlas en una lista
    lista_palabras = parrafo.split()

    # Solicitar una palabra a buscar
    palabra_buscar = input('Ingrese una palabra que quiera buscar: ')

    # Contar cuantas veces aparace la palabra buscada (En mayúsculas y minúsculas)
    num_palabras = lista_palabras.count(palabra_buscar)

    print(f'La palabra "{palabra_buscar}" aparece {num_palabras} veces')

except ValueError:
    print("Error: El texto no puede estar vacío. Intentelo nuevamente.")

