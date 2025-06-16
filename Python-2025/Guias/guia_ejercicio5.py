'''Escribir un programa que simule el movimiento de piezas en un tablero de ajedrez, mostrando graficamente el estado del tablero (por consola) y registrando las piezas captu- ´
radas.
a) Inicializacion del tablero ´
Crea un diccionario para el tablero cuyas claves sean las coordenadas en notacion algebraica ( ´ “a1”.. .“h8”) y cuyos valores sean el nombre de la pieza con
sufijo “B” (blancas) o “N” (negras), por ejemplo:
• Fila 1: “TorreB”, “CaballoB”, “AlfilB”, “ReinaB”, “ReyB”, “AlfilB”, “CaballoB”,
“TorreB”.
• Fila 8: “TorreN”, “CaballoN”, “AlfilN”, “ReinaN”, “ReyN”, “AlfilN”, “CaballoN”,
“TorreN”.
Consejo: Usar bucles anidados puede ser una solucion. ´
b) Mapa de s´ımbolos ASCII
Prepara un diccionario con el nombre simbolos que asocie cada pieza a un
caracter: ´
• Blancas: TorreB → R, CaballoB → N, AlfilB → B, ReinaB → Q, ReyB → K,
PeonB ´ → P
• Negras: TorreN → r, CaballoN → n, AlfilN → b, ReinaN → q, ReyN → k,
PeonN ´ → p
c) Mostrar el tablero dibujado
Cada turno, imprime en consola el tablero con filas numeradas (8 a 1) y columnas encabezadas (a a h), usando:
• El símbolo correspondiente si la casilla esta ocupada.
• Un punto . si la casilla esta vacía.
d) Interaccion con el usuario ´
Declara una lista vac´ıa donde se almacenaran las piezas capturadas. ´
Debe existir una interaccion con el usuario, es decir, solicitar por consola un ´
input para que el jugador ingrese la casilla de origen (pieza a seleccionar) y
una casilla de destino (donde se va a mover la pieza seleccionada).
e) Logica de movimiento ´
Si en el tablero no existe la clave origen, muestra un mensaje de error y vuelve
a pedir movimiento.
Si existe:
• Extrae la pieza de origen.
• Si la pieza de origen se mueve a una casilla de destino donde existe una
pieza enemiga, anade la pieza rival a la ˜ lista capturadas y muestra un mensaje similar a lo siguiente: “Capturo a PeonN en B5”. ´
f) Reporte tras cada turno
Redibuja el tablero con los cambios.
Imprime la lista capturadas (convertida a s´ımbolos ASCII).'''