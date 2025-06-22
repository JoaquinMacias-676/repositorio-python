# Ejercicio 6

# Contar las horas del dia, de 0 a 23
for hora in range(24):
    # Contar los minutos de cada hora del dia, de 0 a 59
    for minutos in range(60):
        # Contar los segundos de cada minuto del dia, de 0 a 59
        for segundos in range(60):
            # Mostrar la hora actual
            print(f"{hora:02d}:{minutos:02d}:{segundos:02d}")
