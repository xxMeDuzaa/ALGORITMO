#4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.
from random import randint
from stack import Stack
number_stack = Stack()

def cargarPila(num_stack):
    for i in range(5):
        rand_number = randint(1, 100)
        #print(rand_number)
        num_stack.push(rand_number)
    
def invertirAuxiliar(num_stack):
    aux_stack= Stack()
    for i in range(num_stack.size()):
        aux_stack.push(num_stack.pop())
    return aux_stack

cargarPila(number_stack)
print("Pila antes de invertir: ")
number_stack.show()
print()
print("Pila despues de ser invertida: ")
number_stack=invertirAuxiliar(number_stack)
number_stack.show()