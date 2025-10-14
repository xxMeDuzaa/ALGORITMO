# 18. Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejemplo
# monitor 1 kg, teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del

# objeto más liviano al más pesado–. Solo pueden utilizar pilas auxiliares como estructuras ex-
# tras, no se pueden utilizar métodos de ordenamiento.

from office import Office
from stack import Stack

objetos_stack=Stack()

objeto1 = Office("monitor", 1)
objeto2 = Office("teclado", 0.25)
objeto3 = Office("silla", 7)
objeto4 = Office("mouse", 0.125)

                       
                       
objetos=[objeto1,objeto2,objeto3,objeto4]

def cargarPila(obje_stack,objetos):
    for obj in objetos:
        obje_stack.push(obj)
        
def ordenarPila(obje_stack):
    aux_stack = Stack()
    
    while obje_stack.size() > 0:
        elemento = obje_stack.pop()
        
        
        while aux_stack.size()>0 and aux_stack.on_top().peso<elemento.peso:
            obje_stack.push(aux_stack.pop())
            
        aux_stack.push(elemento)
    return aux_stack
     
#CUERPO PRINCIPAL
cargarPila(objetos_stack,objetos)
print("Pila original: ")
objetos_stack.show()
pilaOrdenada=ordenarPila(objetos_stack)
print()
print("Pila ordenada con el peso de forma creciente: ")
pilaOrdenada.show()