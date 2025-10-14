#2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.

from queue import Queue
from stack import Stack
from random import randint

number_queue= Queue()

def cargarCola(num_queue):
    for i in range(5):
        num_queue.arrive(randint(1,10))
        
def invertirCola(num_queue):
    aux_stack=Stack()
    while num_queue.size()>0:
        element=num_queue.attention()
        aux_stack.push(element)
        
    while aux_stack.size()>0:
        num_queue.arrive(aux_stack.pop())

cargarCola(number_queue)
print("La cola original: ")
number_queue.show()
invertirCola(number_queue)
print("La cola invertida: ")
number_queue.show()