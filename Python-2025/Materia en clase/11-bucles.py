from colorama import init, Fore
init()

# 01-WHILE
edad = 15
num = 0

# Bucle infinito
'''while edad < 18:
    print("Eres menor de edad, no puedes manejar")'''

# Bucle infinito
'''while True:
    print(num)
    num += 2'''

# ¿Qué hace este bucle
print(Fore.GREEN + "############## 01 - WHILE ##############")
print(Fore.YELLOW + '\n>>> Impresión de numeros de 0 al 100'
'(Incrementando de 2 en 2)')

num = 0
while num <= 100:
    print(num)
    num += 2
    #num = num + 2

# SIEMPRE BUSCAR UNA MANERA DE INTERRUMPIR EL BUCLE

print(Fore.RED + "Primer Bucle terminado!\n")

# Combinando

# Break

while True:
    parametro = input(">")
    if parametro == "salir":
        break
    else:
        print(parametro)

# Continue

n = 0

while n <= 50:
    n += 1
    if n == 40:
        continue
    print(n)

# For
print(Fore.YELLOW+'\n>>> FOR N°1')
for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(i)

print(Fore.YELLOW+'\n>>> FOR N°2')
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in new_list:
    print(i)

# Range
print(Fore.YELLOW+'\n>>> FOR N°3')
for i in range (1,11): # Optimizado, especificando el rango
    print(i)