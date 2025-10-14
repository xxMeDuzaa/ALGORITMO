#2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.
from random import randint
from stack import Stack
number_stack = Stack()

def cargarPila(num_stack):
    for i in range(5):
        rand_number = randint(1, 100)
        #print(rand_number)
        num_stack.push(rand_number)

def eliminarImpares(num_stack):
    number_par=Stack()
    while num_stack.size() > 0:
        number = num_stack.pop()
        if number % 2 == 0:
            number_par.push(number)
    return number_par

cargarPila(number_stack)
print("Pila completa antes de modificar: ")
number_stack.show()
print()
numberPares=eliminarImpares(number_stack) 
print("Pila de elementos pares: ")
numberPares.show()