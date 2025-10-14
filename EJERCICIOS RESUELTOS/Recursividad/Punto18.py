#18. Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.

def crearFila(columnas, valor=0):
    if columnas == 0:
        return []
    else:
        return [valor] + crearFila(columnas - 1, valor)

def crearMatriz(filas, columnas, valor=0):
    if filas == 0:
        return []
    else:
        return [crearFila(columnas, valor)] + crearMatriz(filas - 1, columnas, valor)

def mostrarFila(fila, col=0):
    if col == len(fila):
        print()
        return
    else:
        print(fila[col], end=" ")
        mostrarFila(fila, col + 1)

def mostrarMatriz(matriz, fila=0):
    if fila == len(matriz):
        return
    else:
        mostrarFila(matriz[fila])
        mostrarMatriz(matriz, fila + 1)

# Crear y mostrar matriz
matriz = crearMatriz(3, 4, 5)
mostrarMatriz(matriz)