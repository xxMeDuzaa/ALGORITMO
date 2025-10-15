# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:

from Binarytree import BinaryTree
import random 

arbol_numeros= BinaryTree()

def cargar_arbol(arbol): 
    for i in range(10): #aca tuviera que ser 1000
        numero = random.randint(1, 8)  # rango arbitrario
        arbol.insert(numero)
        
        
# b. determinar si un número está cargado en el árbol o no;
def determinar_numero(arbol, numero):
    nodo = arbol.search(numero)
    if nodo:
        print(f"Se encontró el número {numero}.")
    else:
        print(f"No se encontró el número {numero}.")
        
# c. eliminar tres valores del árbol;
def eliminar_valores(arbol, numero1, numero2, numero3):
    numeros= [numero1, numero2, numero3]
    for num in numeros:
        eliminado, _ = arbol.delete(num) #con el _, ignoramos el other values
        if eliminado is not None:
            print(f"Se eliminó el número {eliminado}.")
        else:
            print(f"El número {num} no se encontró en el árbol.")
    
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
def determinar_ocurrencia(arbol, numero):
    def __determinar_ocurrencia(nodo, numero_a_buscar):
        # Caso base: si el nodo es nulo, no hay ocurrencias
        cantidad = 0
        if nodo is not None:
            # Si el valor del nodo actual coincide, suma 1 al cantidad
            if nodo.value == numero_a_buscar:
                cantidad += 1 
            # Llama recursivamente a la función para los subárboles izquierdo y derecho
            cantidad += __determinar_ocurrencia(nodo.left, numero_a_buscar)
            cantidad += __determinar_ocurrencia(nodo.right, numero_a_buscar)
    
        return cantidad
    
    total = 0
    if arbol.root is not None:
        total= __determinar_ocurrencia(arbol.root, numero)   # Llama a la función auxiliar con la raíz del árbol
    
    return total

# f. contar cuántos números pares e impares hay en el árbol.
def contar_pares_impares(arbol):
    def __contar_pares_impares(nodo):
        if nodo is not None:
            c_pares = 0
            c_impares = 0

            # Chequeo del nodo actual
            if nodo.value % 2 == 0:
                c_pares += 1
            else:
                c_impares += 1

            # Recorro recursivamente los subárboles izquierdo y derecho
            izq_pares, izq_impares = __contar_pares_impares(nodo.left)
            der_pares, der_impares = __contar_pares_impares(nodo.right)

            # Devuelvo la suma total
            return (c_pares + izq_pares + der_pares, c_impares + izq_impares + der_impares)
        else:
            # Caso base: nodo vacío
            return (0, 0)

    # Llamada inicial desde la raíz
    if arbol.root is not None:
        return __contar_pares_impares(arbol.root)
    else:
        return (0, 0)


        
#MAIN:
cargar_arbol(arbol_numeros)
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
print("Barrido preorden: ")
arbol_numeros.pre_order()
print("Barrido inorden: ")
arbol_numeros.in_order()
print("Barrido postorden: ")
arbol_numeros.post_order()
print("Barrido por nivel: ")
arbol_numeros.by_level()
print()
determinar_numero(arbol_numeros, 3) #le pongo 3 nomas
print()
eliminar_valores(arbol_numeros, 3, 4, 9)
print()
# d. determinar la altura del subárbol izquierdo y del subárbol derecho; 
print("Determinar la altura del subárbol izquierdo y del subárbol derecho. PD: -1 solo significa que no hay nodo.")  
subarbol_izquierdo = arbol_numeros.root.left
subarbol_derecho = arbol_numeros.root.right
print(f"Altura del subárbol izquierdo: {arbol_numeros.hight(subarbol_izquierdo)}")
print(f"Altura del subárbol derecho: {arbol_numeros.hight(subarbol_derecho)}")
print()
cantidad_ocurrencias = determinar_ocurrencia(arbol_numeros, 8)
print(f"El número 8 aparece {cantidad_ocurrencias} vez/veces en el árbol.")
print()
pares, impares = contar_pares_impares(arbol_numeros)
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")