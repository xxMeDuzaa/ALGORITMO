#6. Leer una palabra y visualizarla en forma inversa.
from stack import Stack
palabras_stack = Stack()

def cargarPila(pal_stack):
    palabraIngresada=str(input(f"Ingrese la palabra para visualizarla en forma inversa: "))
    pal_stack.push(palabraIngresada)
    
def InvertirPalabra(pal_stack):
    invertir_stack=Stack()
    for i in range(pal_stack.size()):
        palabra=pal_stack.pop()
        palabra_invertida=palabra[::-1]
        invertir_stack.push(palabra_invertida)
    return invertir_stack

cargarPila(palabras_stack)
print("Pila cargada de palabras: ")
palabras_stack.show()
print()
print("Pila visualizada con las palabras inversas: ")
palabras_stack=InvertirPalabra(palabras_stack)
palabras_stack.show()
    