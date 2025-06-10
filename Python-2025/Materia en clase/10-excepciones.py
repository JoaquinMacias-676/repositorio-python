entrada = input('Ingrese un valor entero: ')

try:
    numero = int(entrada)
    print(f"Número ingresado: {numero}")
except ValueError:
    print("Error de valor: el valor ingresado no es entero") # Error por tipo de dato
except Exception as e:
    print("Erro inesperado: {e}") #Un error generico e inesperado, fallo de sistema, archivo corrupto, etc.
else:
    print("Conversión fue exitosa!")
finally:
    print("Finalizaciónd del bloque")