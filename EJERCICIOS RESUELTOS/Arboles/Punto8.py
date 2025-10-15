#8. Desarrollar un algoritmo que implemente dos funciones, una para obtener el mínimo nodo del
#árbol y la segunda para obtener el máximo.

from Binarytree import BinaryTree
import random 

arbol_numeros= BinaryTree()

def cargar_arbol(arbol): 
    for i in range(10):
        numero = random.randint(1, 20)  # rango arbitrario
        arbol.insert(numero)
        
def nodo_minimo(arbol):
    def __nodo_minimo(node):
        if node.left is not None:
            return __nodo_minimo(node.left) #vamos siempre por la izquierda porque ahi se supone que siempre va a estar el minimo
        else:
            return node.value 
            
    
    if arbol.root is not None:
        return __nodo_minimo(arbol.root)
    else:
        return None

def nodo_maximo(arbol):
    def __nodo_maximo(node):
        if node.right is not None:
            return __nodo_maximo(node.right) #vamos siempre por la derecha porque ahi se supone que siempre va a estar el maximo
        else:
            return node.value 
            
    
    if arbol.root is not None:
        return __nodo_maximo(arbol.root)
    else:
        return None

    
    
        
#MAIN
cargar_arbol(arbol_numeros)
arbol_numeros.pre_order()
print()
print(f"El nodo minimo del arbol es: {nodo_minimo(arbol_numeros)}")
print(f"El nodo maximo del arbol es: {nodo_maximo(arbol_numeros)}")