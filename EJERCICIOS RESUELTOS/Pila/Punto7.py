#7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.
from stack import Stack
palabras_stack = Stack()

def cargarPila(pala_stack):
    for i in range(4):
        palabraIngresada=str(input(f"Ingrese la palabra {i}: "))
        pala_stack.push(palabraIngresada)
    
def eliminarIesimo(pal_stack,pos):
    aux_stack=Stack()
    for i in range(pos): #necesito desapilar 1 elemento desde la cima y guardarlo
        aux_stack.push(pal_stack.pop())
        
    pal_stack.pop()
       
    while aux_stack.size()>0:
        pal_stack.push(aux_stack.pop())
        
        
cargarPila(palabras_stack)
print("Pila cargada de palabras: ")
palabras_stack.show()
print()
eliminarIesimo(palabras_stack,1)
print("Pila modificada, eliminando el i-esimo elemento, teniendo que cuenta que (0) es la cima: ")
palabras_stack.show()