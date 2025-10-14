#7. Eliminar el i-ésimo elemento después del frente de la cola.
from queue import Queue
from random import randint

number_queue = Queue()

def cargarCola(num_queue):
    for i in range(4):
        num_queue.arrive(randint(1, 10))

def eliminarIesimo(num_queue, pos):
    aux_queue = Queue()
    
    # Mover los elementos hasta el i-ésimo y colocarlos en la cola auxiliar
    for i in range(pos):  # Desencolar y pasar a la cola auxiliar hasta llegar al índice pos
        aux_queue.arrive(num_queue.attention())
    
    num_queue.attention()  # Aquí se elimina el i-ésimo elemento
    
    # Devolver los elementos de la cola auxiliar a la cola original
    while aux_queue.size() > 0:
        num_queue.arrive(aux_queue.attention())

cargarCola(number_queue)
print("Cola original: ")
number_queue.show()
eliminarIesimo(number_queue, 1)
print("Cola después de eliminar el elemento i-esimo: ")
number_queue.show()