#11. Dada una pila de letras determinar cuántas vocales contiene.
from stack import Stack
letras_stack = Stack()

letras = ["a", "b", "c", "d", "e", "i", "o", "u", "a"]
def cargarLetras(letra_stack,letras):
    for letra in letras:
        letra_stack.push(letra)
        
        
def contarVocales(letra_stack,cont):
    cont=0
    while letra_stack.size() > 0:
        elemento=letra_stack.pop()
        if (elemento=="a" or elemento=="e" or elemento=="i" or elemento=="o" or elemento=="u"):
            cont+=1
    return cont
    
contador=0        
cargarLetras(letras_stack,letras)
print("Pila de Letras: ")
letras_stack.show()
print()
contador=contarVocales(letras_stack, contador)
print(f"La cantidad de vocales que contiene la Pila es de: {contador} ")