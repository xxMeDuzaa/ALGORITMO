# 10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una
# pila con nombres de dioses griegos.

from stack import Stack
dioses_stack = Stack()

dioses = ["Zeus", "Hera", "Poseidón", "Hades", "Apolo"]
def cargarDioses(dios_stack,dioses):
    for dios in dioses:
        dios_stack.push(dios)

def insertarAtenea(dios_stack,pos):
    aux_stack=Stack()
    
    for i in range(pos): #necesito desapilar 1 elemento desde la cima y guardarlo
        aux_stack.push(dios_stack.pop())
    
    dios_stack.push("Atenea")
        
            
    while aux_stack.size()>0:
        dios_stack.push(aux_stack.pop())
        
print("Pila cargada de Dioses antes de Atenea: ")
cargarDioses(dioses_stack,dioses)
dioses_stack.show()
print()
insertarAtenea(dioses_stack, 1) #aca le mando valor 1 ya que es el que esta abajo de la cima
print("Pila modificada, teniendo a la diosa griega Atenea, (0 es la cima): ")
dioses_stack.show()