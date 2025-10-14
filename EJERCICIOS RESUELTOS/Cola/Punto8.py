#8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando solo una cola como estructura auxiliar.
from queue import Queue

number_queue= Queue()
numeros=[2,4,3,1,5]

def cargarCola(num_queue,numeros):
    for num in numeros:
        num_queue.arrive(num)

        
def ordenarPilaCreciente(num_queue):
    aux_queue = Queue()
    
    while num_queue.size() > 0:
        minimo = num_queue.on_front()
    
    # Recorremos la cola original para encontrar el mínimo
    for i in range(num_queue.size() - 1):
        elemento = num_queue.attention()
        # Si el elemento es menor que el mínimo, lo actualizamos
        if elemento < minimo:
            num_queue.arrive(minimo)
            minimo = elemento
        else:
            num_queue.arrive(elemento)

    # Colocamos el mínimo en la cola auxiliar
    aux_queue.arrive(minimo)

        
cargarCola(number_queue,numeros)
print("La cola original: ")
number_queue.show()
print("La cola ordenada: ")
ordenarPilaCreciente(number_queue)
number_queue.show()