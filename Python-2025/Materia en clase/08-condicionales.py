edad = 19

if edad >= 18:
    print('Eres mayor de edad')
print('Este print esta fuera del if')

if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Este print esta fuera del if')

edad = 66

if edad >= 18 and edad < 65: # elif es para cuando queremos evaluar varias opciones
    print('Eres mayor de edad')
elif edad >= 65:
    print('Eres un adulto mayor')
else:
    print('Eres menor de edad')

from colorama import init, Fore # Importando al biblioteca colorma, las funciones int, y la función fore
init()

#CONDICIONAL IF
print(Fore.MAGENTA + '############ 01 - UTILIZANDO IF Y ELSE ############')

licencia = False
edad = 19
automovil = False

#¿Estará correcto este código?
#Incorrecto
print(Fore.YELLOW +'\n>>> Testeando el primer condicional IF')
if licencia:
    print(Fore.WHITE + 'Puedo conducir porque tengo licencia\n')
else:
    print(Fore.WHITE + 'No tengo licencia para conducir')

print(Fore.GREEN + '############ 02 - UTILIZANDO IF, ELIF, y ELSE ############')
if licencia and edad >= 18:
    print(Fore.WHITE + 'jhb')