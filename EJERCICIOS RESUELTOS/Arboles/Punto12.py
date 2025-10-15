# 12. Generar un árbol binario que tenga nueve niveles, luego diseñar los algoritmos necesarios para
# resolver las siguientes actividades:

# b. contar cuántos nodos tiene cada árbol del bosque;
# c. realizar un barrido preorden de cada árbol del bosque;
# d. determinar cuál es el árbol con mayor cantidad de nodos;
# e. indicar que árboles del bosque están completos.

from binarytree2 import BinaryTree #importo el binarytree2 porque es el que no auto balancea

arbol_numeros= BinaryTree()

def cargar_arbol(arbol): #lo puedo cargar de manera secuencial para asegurarme de los 9 niveles
    for i in range(1,10):
        arbol.insert(i)
    
# a. generar un bosque cortando los tres primeros niveles del árbol;  
def generar_bosque(arbol, niveles_corte):
    bosque = []

    def __recorrer(nodo, nivel):
        if nodo is None:
            return
        
        if nivel == niveles_corte:
            # Cortar y crear nuevos árboles a partir de los hijos
            if nodo.left is not None:
                nuevo_izq = BinaryTree()
                nuevo_izq.root = nodo.left
                bosque.insert(nuevo_izq)
                nodo.left = None  # ¡IMPORTANTE! Cortar el enlace
            
            if nodo.right is not None:
                nuevo_der = BinaryTree()
                nuevo_der.root = nodo.right
                bosque.insert(nuevo_der)
                nodo.right = None  # ¡IMPORTANTE! Cortar el enlace
        else:
            __recorrer(nodo.left, nivel + 1)
            __recorrer(nodo.right, nivel + 1)

    __recorrer(arbol.root, 1)
    
    # También agregar el árbol principal si aún tiene nodos
    if arbol.root is not None:
        bosque.insert(0, arbol)  # El árbol principal va primero
    
    return bosque

    

#MAIN
cargar_arbol(arbol_numeros)
print("Arbol cargado:")
arbol_numeros.pre_order()
bosque = generar_bosque(arbol_numeros, 3)
print(f"Bosque generado: {len(bosque)} árboles")
     