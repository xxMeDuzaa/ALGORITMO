# Realizar un algoritmo que ingrese en una pila los dos valores iniciales de la sucesión de Fi-
# bonacci –o condiciones de fin de forma recursiva– y a partir de estos calcular los siguientes
# valores de dicha sucesión, hasta obtener el valor correspondiente a un número numero ingresado por
# el usuario.

from stack import Stack

sucesionFB_stack=Stack()


def ingresarNumero():
    num=int(input("Ingrese el numero hasta donde quiere que se calcule la sucesion de Fibonacci: "))
    return num

def cargarValoresIniciales(suceFB_stack):
    suceFB_stack.push(0)
    suceFB_stack.push(1)
    
def calcularFibonacci(suceFB_stack, numero):
    while suceFB_stack.size() < numero:
        ultimo = suceFB_stack.pop()
        penultimo = suceFB_stack.pop()
        
        nuevo_valor = ultimo + penultimo
        # Volvemos a cargar los valores anteriores en orden
        suceFB_stack.push(penultimo)
        suceFB_stack.push(ultimo)
        suceFB_stack.push(nuevo_valor)

# CUERPO PRINCIPAL
numero=ingresarNumero()
if numero >= 2:
    cargarValoresIniciales(sucesionFB_stack)
    calcularFibonacci(sucesionFB_stack, numero)
elif numero == 1:
    sucesionFB_stack.push(0)

print(f"Sucesión de Fibonacci hasta el término: {numero}")
sucesionFB_stack.show()