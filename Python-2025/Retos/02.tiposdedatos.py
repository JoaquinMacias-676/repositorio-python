# 15 DE MAYO 2025

# 01 - DECLARANDO E INICIALIZANDO VARIABLES NÚMERICAS

edad = 31
estatura = 1.71
peso = 75.4
complejo = 2 + 9j # INICIALIZANDO UN NÚMERO COMPLEJO
complejo2 = complex(1, 4) # OTRA FORMA DE INICIALIZAR UN NÚMERO COMPLEJO

print(complejo)
print(complejo2)

# 02 - OPERACIÓN ARITMÉTICA
imc = peso / estatura ** 2
print(f"Su IMC es: {imc}")

# 03 - FORMATO DE SALIDA DEL RESULTADO
print(f"Su IMC es: {imc:.2f}") # el número que va antes del segundo "f" es el que indica con cuantos decimales saldrá

# FORMATO DE SALIDA DE RESULTADOS (UTILIZANDO EL MÉTODO FORMAT)
print("Su IMC es: {:.2f}".format(imc))

# APLICANDO MÉTODO ROUND
print(round(imc, 2)) #salida redondeada a 2

# TRANSFORMANDO UN NÚMERO ENTERO EN UN NÚMERO FLOTANTE
print(float(edad)) # transformar un número a decimal (agrega decimales, aunque no tenga)

# 04 - DATOS DE TIPO STRING (CADENAS DE TEXTO)
carrera = 'Ingeniería Civil en Informática'
asignatura = "Programación"
descripcion = '''Esta es una asignatura de primer semestre'''

print(carrera[0]) #Imprime el cáracter de la cadena (en este caso la primera letra de la palabra "Ingeniería") (también puede imprimir un espacio vacío)
print(carrera[-1]) #Imprime el último carácter de la cadena
print(carrera[-2]) #Imprime el penúltimo carácter

print("Hola" * 4) #Repetir la cadena una cantidad de veces  (repetir el print 4 las veces que se indique)
#print("Hola"/2) <- Esto nose puede hacer

# UTILIZANDO EL INTERVALO DE UNA CADENA 
print(asignatura[0:5]) #Va a imprimir 5 caracteres, empezando desde el primer carácter hasta el quinto
print(asignatura[1:6]) #Va a imprimir 5 caracteres, empezando desde el segundo carácter hasta el sexto

# APLICANDO EL MÉTODO SPLIT (GENERA UN ARREGLO DE CADENASs)
print(descripcion.split())

#ARREGLO NUMÉRICO
v = [1, 2, 3, 4, 5] # Inicializando un arreglo numéricp
print(v) # El valor de cero marca la posición del primer elemento (Índice)

#FUNCIÓN LEN
len(carrera)

print(carrera.strip())

print(f'La palabra {carrera} tiene: ',len(carrera)), print("caracteres")

#VALORES BOOLEANOS
interruptor = True
ampolleta = False

#FUNCIÓN TYPE PERMITE SABER EL TIPO DE DATO QUE SE UTILIZA
print(type(interruptor))

#COMPARATIVA DE VALORES LÓGICOS
"""print(1<10)
print(100<=20)
print(100==100)
print(100=='100')"""

print(bool("")) #NO TIENE VALOR (ES FALSO)
print(bool(1)) #SI TIENE VALOR (ES VERDADERO)
print(bool(0)) #NO TIENE VALOR (ES FALSO)
print(bool("hola")) #SI TIENE VALOR (ES VERDADERO)