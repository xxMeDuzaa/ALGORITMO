from typing import Any, Optional

class Queue:

    def __init__(self):
        """
        Inicializa las posiciones de la cola
        """
        self.__elements = []

    def arrive(self, value: Any) -> None:
        """
        Agrega un elemento al final de la cola
        """
        self.__elements.append(value)

    def attention(self) -> Optional[Any]:
        """
        Elimina y retorna el elemento al frente de la cola
        """
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        """
        Retorna el tnuemro de elementos de la cola
        """
        return len(self.__elements)
    
    def on_front(self) -> Optional[Any]:
        """
        Retorna el elemento que está al frente de la cola sin eliminarlo
        """
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:
        """
        Mueve el elemento al frente de la cola al final de la misma
        """
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value
    
    def show(self):
        """
        Muestra todos los elementos de la cola, desde el frente hasta el final,
        sin alterar el contenido original de la misma.
        """
        for i in range(len(self.__elements)):
            print(self.move_to_end())

