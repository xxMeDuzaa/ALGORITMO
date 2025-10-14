#4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
from queue import Queue
from random import randint

number_queue = Queue()

def cargarCola(num_queue):
    for i in range(5):
        num_queue.arrive(randint(1, 10))
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def eliminarNoPrimos(num_queue):
    aux_cola = Queue()
    
    while num_queue.size() > 0:
        element = num_queue.attention()
        if es_primo(element): # Si es primo, lo agregamos a la cola auxiliar
            aux_cola.arrive(element)
    
    
    while aux_cola.size() > 0: 
        num_queue.arrive(aux_cola.attention())


cargarCola(number_queue)
print("La cola original: ")
number_queue.show()
eliminarNoPrimos(number_queue)
print("La cola después de eliminar los elementos que no son primos:")
number_queue.show()