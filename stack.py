from typing import Any, Optional


class Stack:

    def init(self):   
        """
        inicilizar las posiciones de la pila
        """
        self.elements = []   #array vacio


    def push(self, value: Any) -> None:    
        """
        agregar un elemento a la pila (top de la pila)
        """
        self.elements.append(value)        

    def pop(self) -> Optional[Any]:      
        """
        elimina y retorna un elemento de la pila (top de la pila) 
        """
        return (
            self.elements.pop()         
            if self.elements
            else None
        )

    def size(self) -> int:      
        """
        retorna el tamaño de la pila
        """
        return len(self.elements)

    def on_top(self) -> Optional[Any]:    
        """
        retorna el elemento que está en el top de la pila sin eliminarlo
        """
        return (
            self.elements[-1]
            if self.__elements
            else None
        )

    def show(self): 
        """
        Muestra todos los elementos de la pila, desde la cima hasta la base,
        sin alterar el contenido original de la misma.
        """        
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)

        while aux_stack.size() > 0: 
            self.push(aux_stack.pop())
