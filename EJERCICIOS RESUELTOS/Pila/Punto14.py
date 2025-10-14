# 14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde-
# nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
# pueden utilizar métodos de ordenamiento–.
from stack import Stack

number_stack = Stack()
numeros=[2,4,3,1,5]

def cargarPila(num_stack,numeros):
    for num in numeros:
        num_stack.push(num)

def ordenarPilaCreciente(num_stack):
    aux_stack = Stack()
    
    while num_stack.size() > 0:
        elemento = num_stack.pop()
        
        
        while aux_stack.size()>0 and aux_stack.on_top()<elemento:
            num_stack.push(aux_stack.pop())
            
        aux_stack.push(elemento)
    return aux_stack
     
        
cargarPila(number_stack,numeros)
print("Pila original:")
number_stack.show()
print("Pila ordenada de forma creciente:")
pilaOrdenada=ordenarPilaCreciente(number_stack)
pilaOrdenada.show()