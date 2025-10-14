from typing import Any, Optional

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None: #AGREGA ELEMENTO A LA CIMA DE LA PILA
        self.__elements.append(value)

    def pop(self) -> Optional[Any]: #ELIMINA ELEMENTO QUE ESTA A LA CIMA DE LA PILA
        return (
            self.__elements.pop() 
            if self.__elements #VERIFICA SI TIENE ELEMENTOS O NO
            else None
        )

    def size(self) -> int: #TAMAÑO DE LA PILA
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1] #OBJETO QUE ESTA EN LA CIMA
            if self.__elements
            else None
        )

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())