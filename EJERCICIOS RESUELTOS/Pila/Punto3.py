#3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.
from stack import Stack
number_stack=Stack()

def cargarPila(num_stack):
    for i in range(6):
        numeros=int(input("Ingrese 5 elementos dentro de la pila: "))
        num_stack.push(numeros)
        
def rempOcurrencias(num_stack,element_replace,new_element):
    aux_stack = Stack()
    while num_stack.size() > 0:
        elemento=num_stack.pop() 
        if elemento==element_replace:
            aux_stack.push(new_element)
        else:
            aux_stack.push(elemento)

    while aux_stack.size() > 0:
        num_stack.push(aux_stack.pop())

cargarPila(number_stack)
print("Pila Original: ")
number_stack.show()
rempOcurrencias(number_stack, 8, 3)
print("Pila con reemplazos: ")
number_stack.show()
