# 12. Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
# que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.
from stack import Stack
personajes_stack = Stack()

personaje = [
    "Luke Skywalker",
    "Leia Organa",
    "Han Solo",
    "Darth Vader",
    "Yoda",
    "Obi-Wan Kenobi",
    "Chewbacca",
    "R2-D2",
    "C-3PO",
    "Boba Fett",
    "Palpatine",
    "Rey",
    "Kylo Ren",
    "Padmé Amidala",
    "Anakin Skywalker"
]

def cargarPJ(pj_stack, personaje):
    for pj in personaje:
        pj_stack.push(pj)

def verificarPJ(pj_stack):
    boolean=False
    aux_stack=Stack()
    while pj_stack.size() > 0:
        pj = pj_stack.pop()
        aux_stack.push(pj)
        if (pj=="Leia Organa" or pj=="Boba Fett"):
            boolean=True
    
    while aux_stack.size() > 0:
        pj_stack.push(aux_stack.pop())
        
    return boolean #tengo que ponerlo al final del todo porque sino no me detecta el segundo while
        
cargarPJ(personajes_stack,personaje)
print("Pila cargada con todos los personajes: ")
personajes_stack.show()
print()
encontrado=verificarPJ(personajes_stack)
if (encontrado==True):
    print("Se encontraron los personajes Leia Organa o Boba Fett")
else:
    print("No se encontraron los personajes Leia Organa o Boba Fett") 
print()
print("Pila Restaurada: ")
personajes_stack.show()