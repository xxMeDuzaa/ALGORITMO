# 10. Desarrollar dos algoritmos, el primero que permita calcular el número de nodos de un nivel
# del árbol –a partir de un nivel ingresado–. La segunda que cuente los nodos que hay en dicho
# nivel –dado que podría no estar completo–, para responder las siguientes actividades:

# a. determinar si el nivel del árbol está completo;
# b. ¿cuántos nodos faltan para completar dicho nivel?

from Binarytree import BinaryTree

arbol_numeros = BinaryTree()

def cargar_arbol(arbol):
    arbol.insert(4)
    arbol.insert(1)
    arbol.insert(3)
    arbol.insert(6)
    arbol.insert(2)
    arbol.insert(5)
    arbol.insert(7)
    arbol.insert(15)
    arbol.insert(14)
    arbol.insert(19)
    
# Primer algoritmo: calcula máximo posible de nodos en un nivel
# Nivel 0 → raíz → máximo 1 nodo (2^0 = 1)

# Nivel 1 → hijos de la raíz → máximo 2 nodos (2^1 = 2)

# Nivel 2 → máximo 4 nodos (2^2 = 4
def nodos_nivel(level, m=2):
    return m ** level

# Segundo algoritmo: cuenta los nodos reales en un nivel dado
def contar_nodos_nivel(arbol, nivel_buscado):
    def __contar_nodos_nivel(nodo, nivel_actual):
        cantidad = 0
        if nodo is not None:
            if nivel_actual == nivel_buscado:
                cantidad += 1
            else:
                cantidad += __contar_nodos_nivel(nodo.left, nivel_actual + 1)
                cantidad += __contar_nodos_nivel(nodo.right, nivel_actual + 1)
        return cantidad

    if arbol.root is not None:
        return __contar_nodos_nivel(arbol.root, 0)
    return 0

# a) Determina si un nivel está completo
def nivel_completo(arbol, level, m=2):
    maximos = nodos_nivel(level, m) #maximos → el máximo posible de nodos en ese nivel (m^level).
    reales = contar_nodos_nivel(arbol, level) #reales → cuántos nodos hay efectivamente en el nivel.
    return reales == maximos #Devuelve True si el nivel está lleno (reales == maximos), o False si faltan nodos.

# b) Calcula cuántos nodos faltan para completar un nivel
def nodos_faltantes(arbol, level, m=2):
    maximos = nodos_nivel(level, m) #Usa la misma lógica que nivel_completo, pero devuelve la diferencia entre los nodos posibles y los reales.
    reales = contar_nodos_nivel(arbol, level) 
    return maximos - reales

cargar_arbol(arbol_numeros)
nivel = 2
print(f"Nivel {nivel} máximo posible: {nodos_nivel(nivel)}")
print(f"Nivel {nivel} real: {contar_nodos_nivel(arbol_numeros, nivel)}")
print(f"¿Nivel completo? {nivel_completo(arbol_numeros, nivel)}")
print(f"Nodos que faltan: {nodos_faltantes(arbol_numeros, nivel)}")