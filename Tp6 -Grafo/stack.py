from typing import Any, Optional

class Stack:

    def __init__(self):
        self.__elements = []
        
    def is_empty(self): #sirve para ver si la pila esta vacia
        return len(self.items) == 0


    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop() 
            if self.__elements #VERIFICA SI TIENE ELEMENTOS O NO
            else None
        )

    def size(self) -> int:
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