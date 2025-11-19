from typing import Any
class HeapMax:

    def __init__(self):
        """Inicializa el montículo con una lista vacía para almacenar los elementos."""
        self.elements = []
    
    def size(self) -> int:
        """Devuelve la cantidad actual de elementos en el montículo."""
        return len(self.elements)

    def add(self, value: Any) -> None:
        """
        Agrega un nuevo elemento al montículo.
        1. Lo añade al final de la lista.
        2. Llama a 'float' para reordenarlo hacia arriba.
        """
        self.elements.append(value)
        self.float(self.size()-1)
    
    def remove(self) -> Any:
        """
        Elimina y devuelve el elemento más grande (la raíz).
        1. Intercambia la raíz con el último elemento.
        2. Elimina el elemento (que ahora es la raíz original) con pop().
        3. Llama a 'sink' para reordenar el nuevo elemento raíz hacia abajo.
        """
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        """
        Mueve el elemento en 'index' hacia arriba (hacia la raíz) si es mayor que su padre.
        Esto mantiene la propiedad de Max Heap después de una inserción.
        """
        father = (index - 1) // 2
        # La condición es: mientras no sea la raíz (index > 0) Y sea MAYOR que su padre.
        while index > 0 and self.elements[index] > self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        """
        Mueve el elemento en 'index' hacia abajo si es menor que el MAYOR de sus hijos.
        Esto mantiene la propiedad de Max Heap después de una eliminación de la raíz.
        """
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            # Busca al mayor de los dos hijos (o solo al izquierdo si no hay derecho)
            mayor = left_son
            if right_son < self.size():
                # Compara al hijo derecho con el hijo izquierdo
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son # 'mayor' es ahora el hijo derecho

            # Si el elemento actual es menor que el MAYOR de sus hijos, hunde el elemento
            if self.elements[index] < self.elements[mayor]:
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False # La propiedad de Max Heap se ha restaurado

    def interchange(self, index_1: int, index_2: int) -> None:
        """Función auxiliar para intercambiar los elementos en dos posiciones dadas."""
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        """
        Utiliza el montículo para ordenar los elementos. 
        Extrae repetidamente el máximo, resultando en una lista ORDENADA DESCENDENTEMENTE.
        """
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        """
        Método para usar el Max Heap como una Cola de Prioridad. 
        Agrega un elemento donde la 'priority' será el factor de ordenación.
        El valor con MAYOR prioridad numérica es el que se extrae primero.
        """
        self.add([priority, value])
    
    def attention(self) -> Any:
        """Extrae el elemento con la MÁXIMA prioridad (la raíz)."""
        value = self.remove()
        return value

class HeapMin:

    def __init__(self):
        """Inicializa el montículo con una lista vacía."""
        self.elements = []
    
    def size(self) -> int:
        """Devuelve la cantidad actual de elementos."""
        return len(self.elements)

    def add(self, value: Any) -> None:
        """
        Agrega un nuevo elemento y llama a 'float' para reordenarlo.
        """
        self.elements.append(value)
        self.float(self.size()-1)
    
    def remove(self) -> Any:
        """
        Elimina y devuelve el elemento más pequeño (la raíz).
        Proceso idéntico a HeapMax, pero 'sink' ahora mantiene la propiedad de Min Heap.
        """
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        """
        Mueve el elemento en 'index' hacia arriba si es MENOR que su padre.
        Esto mantiene la propiedad de Min Heap después de una inserción.
        """
        father = (index - 1) // 2
        # La condición es: mientras no sea la raíz (index > 0) Y sea MENOR que su padre.
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        """
        Mueve el elemento en 'index' hacia abajo si es MAYOR que el MENOR de sus hijos.
        Esto mantiene la propiedad de Min Heap después de una eliminación de la raíz.
        """
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            # Busca al menor de los dos hijos (o solo al izquierdo si no hay derecho)
            minor = left_son
            if right_son < self.size():
                # Compara al hijo derecho con el hijo izquierdo
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son # 'minor' es ahora el hijo derecho

            # Si el elemento actual es mayor que el MENOR de sus hijos, hunde el elemento
            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False # La propiedad de Min Heap se ha restaurado

    def interchange(self, index_1: int, index_2: int) -> None:
        """Función auxiliar para intercambiar los elementos en dos posiciones dadas."""
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        """
        Utiliza el montículo para ordenar los elementos.
        Extrae repetidamente el mínimo, resultando en una lista ORDENADA ASCENDENTEMENTE.
        """
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        """
        Método para usar el Min Heap como una Cola de Prioridad. 
        Agrega un elemento donde la 'priority' será el factor de ordenación.
        El valor con MENOR prioridad numérica es el que se extrae primero.
        """
        self.add([priority, value])
    
    def attention(self) -> Any:
        """Extrae el elemento con la MÍNIMA prioridad (la raíz)."""
        value = self.remove()
        return value

# priority_queue = HeapMin()

# priority_queue.arrive('x', 1)
# priority_queue.arrive('b', 2)
# priority_queue.arrive('a', 2)
# priority_queue.arrive('f', 1)
# priority_queue.arrive('y', 1)
# priority_queue.arrive('j', 2)
# priority_queue.arrive('z', 3)
# print(priority_queue.elements)

# while priority_queue.size() > 0:
#     print(priority_queue.attention())

# h = HeapMin()
# h.add(19)
# h.add(5)
# h.add(1)
# h.add(3)
# h.add(9)


# list_sort = h.heapsort()

# print(list_sort)
# print(h.elements)

