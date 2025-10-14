#9. Resolver el problema del factorial de un número utilizando una pila.
from stack import Stack

number_stack = Stack()

def cargarPila(num_stack,num):
    for i in range(1,num+1):
        num_stack.push(i)
   
def calcularFactorial(num_stack,result):
    result=1
    while num_stack.size() > 0:
        number=num_stack.pop()
        result=result * number
    return result



resultado=1
numero=int(input("Ingrese el numero que desea calcular el facorial: "))
cargarPila(number_stack,numero)  
print()
print("Pila cargada del factorial: ")
number_stack.show()
print()
resultado=calcularFactorial(number_stack, resultado)
print(f"El resultado del factorial de {numero} es: {resultado}")