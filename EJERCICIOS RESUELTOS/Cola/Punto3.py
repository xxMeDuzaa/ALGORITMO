#3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo.
from queue import Queue
from stack import Stack

cadena_queue = Queue()

cadena="neuquen"
def cargarPalabra(cade_queue,cadena):
   for caracter in cadena:
      cade_queue.arrive(caracter)
   
   
def verificarPalindromo(cad_queue,cadena):
    cadena_invertida=""
    aux_stack=Stack()
    verificar=False
    while cad_queue.size()>0:
        element=cad_queue.attention()
        aux_stack.push(element)
    
    while aux_stack.size()>0:
        cadena_invertida+=aux_stack.pop()
        if cadena == cadena_invertida:
            verificar=True
    return verificar
      

cargarPalabra(cadena_queue,cadena)
print("Cadena ingresada: ")
cadena_queue.show()
print()
verificarP=verificarPalindromo(cadena_queue,cadena)
print(f"La cadena de caracteres es palindromo?: {verificarP}")