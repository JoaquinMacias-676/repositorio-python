'''Menú interactivo con match-case

Crea un menú que permita al usuario:

Ver una lista de tareas.

Agregar una tarea.

Eliminar una tarea.

Salir del programa.

Usa match, listas y bucle while.'''

tareas = []

print('\n============ MENÚ DE TAREAS ============')

while True:
    print('\nSelecciona una opción:\n')
    print('1. Ver Tareas')
    print('2. Agregar Tarea')
    print('3. Eliminar Tarea')
    print('4. Salir\n')

    opcion = input('Opción: ')

    match opcion:
        case "1":
            if not tareas:
                print('\nNo hay tareas asignadas aún')
            else:
                print('\nTarea(s):')
                for i, tarea in enumerate(tareas, start=1):
                    print(f'{i}. {tarea}')
        
        case "2":
            tarea_agregar = input('Agregar Tarea: ')
            tareas.append(tarea_agregar)
            print(f'La tarea {tarea_agregar} ha sido agregada con exito.')

        case "3":
            if not tareas:
                print('\nNo hay tareas las cuales eliminar.')
            else:
                print('Tareas Actuales:')
                for i, tarea in enumerate(tareas, start=1):
                    print(f'{i}. {tarea}')
                try:
                    num_eliminar = int(input('Ingrese el número de la tarea a eliminar: '))
                    if num_eliminar >= 1 and num_eliminar <= len(tareas):
                        eliminada = tareas.pop(num_eliminar - 1)
                        print(f'La tarea {eliminada} fue eliminada correctamente.')
                    else:
                        print('Ingrese otro número')
                except ValueError:
                    print('Ingrese un número que sea válido')

        case "4":
            print('\n============ CERRANDO MENÚ ============\n')
            break

        case _:
            print('Valor erróneo. Inténtelo de nuevo.')
