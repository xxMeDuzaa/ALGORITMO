#9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.
from queue import Queue

number_queue= Queue()
numeros=[-10,-1,7,2,5]

def cargarCola(num_queue,numeros):
    for num in numeros:
        num_queue.arrive(num)
     
def sacarMinMaximo(num_queue):
    aux_queue=Queue()
    element=num_queue.on_front()
    min=element
    max=element

    while num_queue.size() > 0:
        element = num_queue.attention()
        aux_queue.arrive(element)
        if element < min:
            min = element
            
        if element > max:
            max = element

    while aux_queue.size()>0:
        num_queue.arrive(aux_queue.attention())
     
    return min, max

def contarNegativos(num_queue):
    c_negativos=0
    while num_queue.size()>0:
        element=num_queue.attention()
        if element<0:
            c_negativos+=1
    return c_negativos

cargarCola(number_queue,numeros)
print("La cola original: ")
number_queue.show()
minimo,maximo=sacarMinMaximo(number_queue)
print(f"El rango entre el numero maximo {maximo} y el numero minimo {minimo} es de: {maximo-minimo}")
contador_negativos=contarNegativos(number_queue)
print(f"La cantidad de numeros negativos es de: {contador_negativos}")