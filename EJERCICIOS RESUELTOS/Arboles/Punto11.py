# 11. Escribir un algoritmo que permita resolver las siguientes actividades:


from Binarytree import BinaryTree
import random 

arbol_numeros= BinaryTree()

def cargar_arbol(arbol): 
    for i in range(5):
        numero = random.randint(1, 15)  # rango arbitrario
        arbol.insert(numero)

#a. contar el número de nodos del árbol;
def contarNodosArbol(arbol):
    def __contarNodosArbol(nodo):
        cantidad = 0
        if nodo is not None:
            cantidad += 1
            cantidad += __contarNodosArbol(nodo.left)
            cantidad += __contarNodosArbol(nodo.right)

        return cantidad

    total = 0
    if arbol.root is not None:
        total = __contarNodosArbol(arbol.root)
    
    return total

# b. determinar el número de hojas del árbol;
def contarHojas(arbol): #Una hoja es un nodo que no tiene hijos (left y right son None).
    def __contarHojas(nodo):
        if nodo is None:
            return 0
        # Si no tiene hijos → es hoja
        if nodo.left is None and nodo.right is None: 
            return 1
        else:
            # Si tiene hijos → contar recursivamente
            return __contarHojas(nodo.left) + __contarHojas(nodo.right)

    if arbol.root is not None:
        return __contarHojas(arbol.root)
    return 0

# c. mostrar la información de los nodos hojas;
def mostrar_info_hojas(arbol):
    def __mostrar_info_hojas(nodo):
        if nodo is None:
            return
        
        # Si no tiene hijos, es una hoja.
        if nodo.left is None and nodo.right is None: 
            print(nodo.value)
        else:
            __mostrar_info_hojas(nodo.left)
            __mostrar_info_hojas(nodo.right)

    if arbol.root is not None:
        __mostrar_info_hojas(arbol.root)
        
        
# d. determinar el padre de un nodo;
def determinar_padre(arbol, valor_nodo_a_buscar):
    if arbol.root is None or arbol.root.value == valor_nodo_a_buscar:
        return None  # La raíz no tiene padre, o el árbol está vacío.

    def __determinar_padre(nodo, valor_a_buscar, node=None):
        if nodo is None:
            return None # El nodo no se encuentra en este subárbol

        if nodo.value == valor_a_buscar:
            return node.value # Encontré el nodo, retorno su padre.

        if valor_a_buscar < nodo.value:
            return __determinar_padre(nodo.left, valor_a_buscar, nodo)
        else:
            return __determinar_padre(nodo.right, valor_a_buscar, nodo)
    
    if arbol.root is not None:
        return __determinar_padre(arbol.root, valor_nodo_a_buscar)

    
#MAIN
cargar_arbol(arbol_numeros)
print("Arbol cargado de numeros: ")
arbol_numeros.pre_order()
print(f"Numero de nodos del arbol: {contarNodosArbol(arbol_numeros)} ")
print(f"Numero de hojas del arbol: {contarHojas(arbol_numeros)} ")
print("Información de los nodos hojas: ")
mostrar_info_hojas(arbol_numeros)
print(f"Determino el padre del nodo con valor 2: {determinar_padre(arbol_numeros,2)}")
# e. determinar la altura de un árbol.
print(f"Altura del arbol: {arbol_numeros.hight(arbol_numeros.root)}")