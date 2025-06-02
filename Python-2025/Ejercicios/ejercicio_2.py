'''Desarrollar un algoritmo con operaciones mixtas con números complejos:
A. Ingresar tres valores numéricos diferentes (entero, flotante y complejo)
B. Calcular y mostrar:
● Potencia Compleja (Complejo y Entero)
● Suma Mixta (Complejo y Flotante)
● Producto Mixto (Complejo y Entero)
● Módulo de Potencia Compleja. El módulo se realiza utilizando la función abs()
(Variable Potencia Compleja, con 3 decimales)'''

# INGRESO DE VALORES NÚMEROS MEDIANTE CONSOLA
entero = int(input('Ingrese un número entero: '))
flotante = float(input('Ingrese un número en decimales: '))
complejo = complex(input('Ingrese un número complejo (ej: 1+7j): '))

# CÁLCULO DE OPERACIONES
potencia_com = complejo ** entero

suma_mix = complejo + flotante

producto_mixto = complejo * entero

mod_potencia_compleja = abs(potencia_com)

# ENTREGA DE RESULTADOS
print(f'El resultado de la potencia {complejo} ^ {entero} es {potencia_com:.3f}')

print(f'El resultado de la suma {complejo} + {flotante} es {suma_mix} ')

print(f'El resultado de la multiplicación {complejo} * {entero} es {producto_mixto}')

print(f'El modulo de la potencia {potencia_com:.3f} es {mod_potencia_compleja:.3f}')