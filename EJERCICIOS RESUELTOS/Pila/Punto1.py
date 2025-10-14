#1. Determinar el número de ocurrencias de un determinado elemento en una pila.
from stack import Stack

number_stack = Stack()
def cargarPila(num_stack):
  for i in range(5):
    numeros=int(input("Ingrese 5 elementos dentro de la pila: "))
    num_stack.push(numeros)

def ocurrenciasElemento(num_stack, bus, cont_ocurrencia):
  for i in range(num_stack.size()):
      if num_stack.pop()==bus:
          cont_ocurrencia+=1
  return cont_ocurrencia
        
contador_ocurrencia=0
cargarPila(number_stack)
buscado=int(input("Ingrese un determinado elemento para saber su numero de ocurrencias: "))
print()
print("Contenido de la pila: ")
number_stack.show()
contador_ocurrencia = ocurrenciasElemento(number_stack, buscado, contador_ocurrencia) #guardo el valor del return en una variable
print(f"El numero de ocurrencias de el elemento {buscado} es de: {contador_ocurrencia}")