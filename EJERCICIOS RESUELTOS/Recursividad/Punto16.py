#16. Implementar un función recursiva que permita obtener el valor de an en una sucesión geomé-
#trica (o progresión geométrica) con un valor a1= 2 y una razón r = -3. Además desarrollar un
#algoritmo que permita visualizar todos los valores de dicha sucesión desde a1 hasta an.


def sucesionGeometrica(a1, r, n):
    # Caso base: cuando n es 1, el término es simplemente a1
    if n == 1:
        return a1
    else:
        return r * sucesionGeometrica(a1, r, n - 1)  # Llamada recursiva para obtener el valor del término anterior

# Algoritmo para visualizar todos los valores de la sucesión desde a1 hasta an
def visualizarSucesion(a1, r, n, i=1):
    # Caso base: cuando el índice supera n, terminamos
    if i > n:
        return
    else:
        # Imprimir el término de la sucesión para el índice actual
        print(f"a_{i} = {sucesionGeometrica(a1, r, i)}")
        # Llamada recursiva para el siguiente término
        visualizarSucesion(a1, r, n, i + 1)

visualizarSucesion(2, -3, 3)