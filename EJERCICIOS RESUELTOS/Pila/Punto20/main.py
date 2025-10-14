# 20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
# cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
# norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
# que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
# partida, retornando por el mismo camino que fue.
from stack import Stack
from movimiento import Movimiento

# Diccionario con las direcciones opuestas
opuestas = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

movimientos_stack= Stack()

movi1=Movimiento(5,"norte")
movi2=Movimiento(2,"este")
movi3=Movimiento(3,"noroeste")

movimientos=[movi1,movi2,movi3]

def CargarPila(movi_stack,movimientos):
    for movi in movimientos:
        movi_stack.push(movi)
        
def volverPartida(movi_stack):
    aux_stack=Stack()
    while movi_stack.size()>0:
        mov=movi_stack.pop()
        direccion_opuesta=opuestas[mov.direccion]
        aux_stack.push(Movimiento(mov.pasos,direccion_opuesta))
    
    while aux_stack.size()>0:
        movi_stack.push(aux_stack.pop())
        
        
#CUERPO PRINCIPAL
CargarPila(movimientos_stack,movimientos)
print("Pila con movimientos: ")
movimientos_stack.show()
volverPartida(movimientos_stack)
print("Pila volviendo a su lugar de partida: ")
movimientos_stack.show()