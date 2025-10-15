# 4. Implementar un algoritmo que contemple dos funciones, la primera que devuelva el hijo dere-
# cho de un nodo y la segunda que devuelva el hijo izquierdo.

from Binarytree import BinaryTree
import random 

arbol_numeros= BinaryTree()

def cargar_arbol(arbol): 
    for i in range(10): #aca tuviera que ser 1000
        numero = random.randint(1, 20)  # rango arbitrario
        arbol.insert(numero)

def hijo_derecho(arbol, valor):
    nodo = arbol.search(valor)
    if nodo and nodo.right: #Si el nodo existe y además tiene hijo derecho, entrá al if
        return nodo.right.value
    return None

def hijo_izquierdo(arbol, valor):
    nodo = arbol.search(valor)
    if nodo and nodo.left: #Si el nodo existe y además tiene hijo izquierdo, entrá al if
        return nodo.left.value
    return None

        
#MAIN
cargar_arbol(arbol_numeros)
arbol_numeros.pre_order()
print()
numero=int(input("Ingrese el numero del arbol, donde quiere ver su hijo derecho e izquierdo: "))
print(f"Hijo derecho de {numero}:", hijo_derecho(arbol_numeros, numero)) 
print(f"Hijo izquierdo de {numero}:", hijo_izquierdo(arbol_numeros, numero))