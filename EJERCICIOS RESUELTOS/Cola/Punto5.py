#5. Utilizando operaciones de cola y pila, invertir el contenido de una pila.
from queue import Queue
from stack import Stack
from random import randint

number_stack= Stack()

def cargarPila(num_stack):
    for i in range(5):
        num_stack.push(randint(1,10))
        
def invertirPila(num_stack):
    aux_queue=Queue()
    while num_stack.size()>0:
        element=num_stack.pop()
        aux_queue.arrive(element)
        
    while aux_queue.size()>0:
        num_stack.push(aux_queue.attention())

cargarPila(number_stack)
print("La pila original: ")
number_stack.show()
invertirPila(number_stack)
print("La pila invertida: ")
number_stack.show()