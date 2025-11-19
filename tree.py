from typing import Any, Optional
from queue_ import Queue

class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            """
            Nodo de un árbol binario.
            :param value: Valor del nodo.
            :param other_values: Otros valores asociados al nodo.
            """
            self.value = value
            self.other_values = other_values
            self.left = None   # Hijo izquierdo
            self.right = None  # Hijo derecho
            self.hight = 0  # Altura del nodo

    def __init__(self):
        """
        Inicializa un árbol binario vacío.
        """
        self.root = None

    def insert(self, value: Any, other_values: Optional[Any] = None):
        """
            Inserta un nuevo nodo en el árbol binario.
            :param root: Nodo raíz del árbol o subárbol.
            :param value: Valor del nuevo nodo.
            :param other_values: Otros valores asociados al nuevo nodo.
            :return: Nodo raíz actualizado del árbol o subárbol.
            """
        def __insert(root, value, other_values):  #funcion recursiva
             # Caso base: si el nodo actual es nulo, hemos encontrado la posición para insertar.
            if root is None:  
                return BinaryTree.__nodeTree(value, other_values) 
            # Si el valor es menor, vamos por la rama izquierda.
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
                # Si el valor es mayor o igual, vamos por la rama derecha.
            else:
                root.right = __insert(root.right, value, other_values)

            # Después de insertar, balancea el árbol desde el nodo actual hacia arriba.
            root = self.auto_balance(root)
            # Actualiza la altura del nodo.
            self.update_hight(root)

            return root
        # Inicia el proceso de inserción desde la raíz del árbol.
        self.root = __insert(self.root, value, other_values)

    def pre_order(self):
        """
        Recorrido en preorden del árbol binario, como estan insertados (raiz-izquierda-derecha).
        """
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.hight)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    def in_order(self):
        """
        Recorrido en inorden del árbol binario(izquierda-raiz-derecha).
        """
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    def post_order(self):
        """
        Recorrido en postorden del árbol binario(derecha-raiz-izquierda) desndiente.
        """
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

    def search(self, value: Any) -> __nodeTree:
        """
        Busca un nodo con el valor especificado en el árbol binario.
        :param value: Valor a buscar.
        :return: Nodo encontrado o None si no se encuentra.
        """
        def __search(root, value):
            if root is not None:   
                if root.value == value:  #si lo encontramos, lo retornamos
                    return root
                elif root.value > value:  #si es menor, buscamos en el subarbol izquierdo
                    return __search(root.left, value)
                else:   #si es mayor, buscamos en el subarbol derecho
                    return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def proximity_search(self, value: Any) -> __nodeTree:
        """
        Busca y muestra todos los nodos cuyo valor comienza con un prefijo dado.
        Recorre todo el árbol para encontrar todas las coincidencias.
        """
        def __search(root, value):
            if root is not None:
                # Si el valor del nodo comienza con el prefijo, lo imprime.
                if root.value.startswith(value):
                    print(root.value)
                    # Continúa la búsqueda en ambos subárboles.
                # elif root.value > value:
                __search(root.left, value)
                # else:
                __search(root.right, value)

        aux = None
        # Inicia la búsqueda desde la raíz.
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def delete(self, value: Any):
        """
        Elimina un nodo con el valor especificado del árbol binario.
        :param value: Valor del nodo a eliminar.
        :return: Valor eliminado y otros valores asociados.
        """
        def __replace(root):
            """Función auxiliar para encontrar el nodo que reemplazará al eliminado (el mayor del subárbol izquierdo)."""
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    # Búsqueda del nodo a eliminar.
                    root.left, delete_value, deleter_other_values = __delete(root.left, value)
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(root.right, value)
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    # Caso 1: El nodo a eliminar no tiene hijo izquierdo.
                    if root.left is None:
                        root = root.right
                    # Caso 2: El nodo a eliminar no tiene hijo derecho.
                    elif root.right is None:
                        root.right = root.left
                    # Caso 3: El nodo tiene dos hijos.
                    else:
                        # Se busca el nodo reemplazante (el mayor del subárbol izquierdo).
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

                # Se rebalancea y actualiza la altura después de la eliminación.
                root = self.auto_balance(root)
                self.update_hight(root)
            return root, delete_value, deleter_other_values

        delete_value =  None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)
        
        return delete_value, deleter_other_values
    
    def by_level(self):     # recorrido por niveles
        """
        Muestra el árbol nivel por nivel, como si lo leyeras de arriba hacia abajo
        y de izquierda a derecha. Utiliza una cola para lograrlo.
        """
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(node.value)
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    def hight(self, root):   # hace un barrido por niveles (de arriba hacia abajo y de izquierda a derecha)
        if root is None:
            return -1   # altura de un nodo nulo
        else:
            return root.hight

    def update_hight(self, root):  # actualiza la altura basandose en la altura de sus hijos
        if root is not None:
            alt_left = self.hight(root.left)
            alt_right = self.hight(root.right)
            root.hight = max(alt_left, alt_right) + 1

    def simple_rotation(self, root, control):  
        """
        Realiza una rotación simple (derecha o izquierda).
        Imagina que "subes" un nodo hijo para que ocupe el lugar de su padre,
        y el padre "baja" para convertirse en hijo, reacomodando el árbol.
        """
        if control: # Rotación Simple a la Derecha (el hijo izquierdo sube)
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # Rotación Simple a la Izquierda (el hijo derecho sube)
            aux = root.right
            root.right = aux.left
            aux.left = root

        # Después de mover los nodos, recalculamos sus alturas.
        self.update_hight(root)
        self.update_hight(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        """
        Realiza una rotación doble. Es un movimiento de dos pasos para
        corregir desbalances más complejos que una rotación simple no puede arreglar.
        """
        if control: # Rotación Doble a la Derecha
            # 1. Primero, hacemos una rotación simple a la IZQUIERDA en el hijo izquierdo.
            #    Esto "alinea" el desbalance para poder corregirlo.
            root.left = self.simple_rotation(root.left, False)
            # 2. Luego, hacemos la rotación simple a la DERECHA en el nodo original.
            root = self.simple_rotation(root, True)
        else:
            # 1. Primero, hacemos una rotación simple a la DERECHA en el hijo derecho.
            root.right = self.simple_rotation(root.right, True)
            # 2. Luego, hacemos la rotación simple a la IZQUIERDA en el nodo original.
            root = self.simple_rotation(root, False)
        
        return root

    def auto_balance(self, root):
        """
        Verifica el factor de balanceo de un nodo y aplica las rotaciones
        necesarias para mantener el árbol balanceado (AVL).
        """
        if root is not None:
            # Si el subárbol izquierdo es más alto (desbalance hacia la izquierda).
            if self.hight(root.left) - self.hight(root.right) == 2:
                # Si el desbalance es causado por el hijo izquierdo (Rotación Simple).
                if self.hight(root.left.left) >= self.hight(root.left.right):
                    root = self.simple_rotation(root, True)
                    # Si el desbalance es causado por el hijo derecho del hijo izquierdo (Rotación Doble).
                else:
                    root = self.double_rotation(root, True)
                     # Si el subárbol derecho es más alto (desbalance hacia la derecha).
            if self.hight(root.right) - self.hight(root.left) == 2:
                # Si el desbalance es causado por el hijo derecho (Rotación Simple).
                if self.hight(root.right.right) >= self.hight(root.right.left):
                    # print("RS LEFT")
                    root = self.simple_rotation(root, False)
                    # Si el desbalance es causado por el hijo izquierdo del hijo derecho (Rotación Doble).
                else:
                    # print("RD LEFT")
                    root = self.double_rotation(root, False)
        return root
    



    def villain_in_order(self):
        def __villain_in_order(root):
            if root is not None:
                __villain_in_order(root.left)
                if root.other_values["is_villain"] is True:
                    print(root.value)
                __villain_in_order(root.right)

        if self.root is not None:
            __villain_in_order(self.root)

    def show_by_initial(self, letter):
        def __show_by_initial(root):
            if root is not None:
                __show_by_initial(root.left)
                if root.value.lower().startswith(letter.lower()) is True:
                    print(root.value)
                __show_by_initial(root.right)

        if self.root is not None:
            __show_by_initial(self.root)

    def count_heroes(self):
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.other_values["is_villain"] is False:
                    count += 1
                count += __count_heroes(root.left)
                count += __count_heroes(root.right)

            return count

        total = 0
        if self.root is not None:
            total = __count_heroes(self.root)
        return total
    
    def divide_tree(self, arbol_h, arbol_v):
        def __divide_tree(root, arbol_h, arbol_v):
            if root is not None:
                if root.other_values["is_villain"] is False:
                    arbol_h.insert(root.value, root.other_values)
                else:
                    arbol_v.insert(root.value, root.other_values)
                __divide_tree(root.left, arbol_h, arbol_v)
                __divide_tree(root.right, arbol_h, arbol_v)

        __divide_tree(self.root, arbol_h, arbol_v)
    
    def count_nodes(self):
        def __count_nodes(root):
            count = 0
            if root is not None:
                count += 1
                count += __count_nodes(root.left)
                count += __count_nodes(root.right)
            return count

        total = 0
        if self.root is not None:
            total = __count_nodes(self.root)
        return total