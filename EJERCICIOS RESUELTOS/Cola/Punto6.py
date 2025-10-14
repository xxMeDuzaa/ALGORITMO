#6. Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar.
from queue import Queue

number_queue = Queue()

def cargarCola(num_queue):
    for i in range(5):
        numeros=int(input("Ingrese 5 elementos dentro de la cola: "))
        number_queue.arrive(numeros)

def ocurrenciasElemento(num_queue, bus, cont_ocurrencia):
  while num_queue.size()>0:
      if num_queue.attention()==bus:
          cont_ocurrencia+=1
  return cont_ocurrencia
        
contador_ocurrencia=0
cargarCola(number_queue)
buscado=int(input("Ingrese un determinado elemento para saber su numero de ocurrencias: "))
print()
print("Contenido de la pila: ")
number_queue.show()
contador_ocurrencia = ocurrenciasElemento(number_queue, buscado, contador_ocurrencia) #guardo el valor del return en una variable
print(f"El numero de ocurrencias de el elemento {buscado} es de: {contador_ocurrencia}")