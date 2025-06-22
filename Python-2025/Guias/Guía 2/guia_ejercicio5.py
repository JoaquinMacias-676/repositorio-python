# Ejercicio 5

columnas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
tablero = {}

# Fila 1 (Blancas)
piezas_blancas = ["TorreB", "CaballoB", "AlfilB", "ReinaB", "ReyB", "AlfilB", "CaballoB", "TorreB"]
for i in range(8):
    tablero[columnas[i] + '1'] = piezas_blancas[i]
    tablero[columnas[i] + '2'] = "PeonB"

# Fila 8 (Negras)
piezas_negras = ["TorreN", "CaballoN", "AlfilN", "ReinaN", "ReyN", "AlfilN", "CaballoN", "TorreN"]
for i in range(8):
    tablero[columnas[i] + '8'] = piezas_negras[i]
    tablero[columnas[i] + '7'] = "PeonN"

 #Mapa de simbolos ASCII

simbolos = {
     "TorreB": "R", "CaballoB": "N", "AlfilB": "B", "ReinaB": "Q", "ReyB": "K", "PeonB": "P",
     "TorreN": "r", "CaballoN": "n", "AlfilN": "b", "ReinaN": "q", "ReyN": "k", "PeonN": "p"
}

# Lista de piezas capturadas
capturadas = []

# Bucle de juego
while True:
    print(" a b c d e f g h")
    for fila in range(8, 0, -1):
        linea = str(fila) + " "
        for columna in columnas:
            casilla = columna + str(fila)
            if casilla in tablero:
                linea += simbolos[tablero[casilla]] + " "
            else:
                linea += ". "
        print(linea)
    print()

    # Piezas capturadas
    if capturadas:
        print("Piezas capturadas:", ' '.join(simbolos[p] for p in capturadas))
    else:
        print("Piezas capturadas: Ninguna")

    # Pedir movimientos
    origen = input("Ingrese casilla de origen (ejemplo: e2): ").lower()
    destino = input("Ingrese casilla de destino (ejemplo: e4): ").lower()

    if origen not in tablero:
        print("No hay ninguna pieza en esta casilla. Intente de nuevo. \n")
        continue

    pieza = tablero[origen]

    # Si hay pieza en destino (captura)
    if destino in tablero:
        pieza_destino = tablero[destino]
        if pieza[-1] != pieza_destino[-1]:  # Si son de distinto color
            capturadas.append(pieza_destino)
            print(f"Capturó a {pieza_destino} en {destino.upper()}\n")
        else:
            print("No puede capturar su propia pieza. Intente de nuevo.\n")
            continue

    # Mover la pieza
    tablero[destino] = pieza
    del tablero[origen]
