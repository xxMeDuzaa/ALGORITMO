from typing import Any

class Tree:

    class __nodeTree:

        def __init__(self, value: Any):
            self.value = value
            self.left = None #inicializo enlaces a hijos
            self.right = None 

    def __init__(self): #inicializo arbol queda en vacio (creo la raiz)
        self.root = None

    def insert(self, value: Any):
        print(f'insertar value {value}')
        def __insert(root, value): #funcion recursiva
            if root is None: #caso base
                print('lugar libre insertar raiz')
                return Tree.__nodeTree(value)
            elif value < root.value:
                print(f'vamos a la izquierda ->padre {root.value}')
                root.left = __insert(root.left, value)
            else:
                print(f'vamos a la derecha ->padre {root.value}')
                root.right = __insert(root.right, value)
                
            #el nodo actual (root) se devuelve para que se pueda conectar al nodo padre de la llamada anterior.
            return root 

        #garantiza que, después de insertar un nuevo valor, la variable self.root siempre apunte a la raíz actualizada del árbol.
        self.root = __insert(self.root, value) #esto es fundamental porque en la primera inserción crea la raíz, y en las siguientes mantiene enlazado todo el árbol correctamente.


arbol = Tree()

arbol.insert(19)
arbol.insert(7)
arbol.insert(31)
arbol.insert(11)
print(arbol.root.value, arbol.root.left.value, arbol.root.right.value)