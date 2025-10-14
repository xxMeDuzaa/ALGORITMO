# 16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
# strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
# permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
# bos episodios.

from stack import Stack
personajes_stack1 = Stack()
personajes_stack2 = Stack()

personajesV = ["Luke Skywalker", "Darth Vader", "Han Solo", "Leia Organa"]
personajesVII = ["Rey", "Finn", "Han Solo", "Leia Organa"]

def cargarPila1(perso_stack1,personajesV):
    for personaje1 in personajesV:
        perso_stack1.push(personaje1)
        
def cargarPila2(perso_stack2,personajesVII):
    for personaje2 in personajesVII:
        perso_stack2.push(personaje2)
        
def interseccionPilas(perso_stack1,perso_stack2):
    aux_stackpj2=Stack()
    while perso_stack1.size()>0:
       pj1=perso_stack1.pop() #SACO EL PERSONAJE
       while perso_stack2.size()>0:
           pj2=perso_stack2.pop()
           aux_stackpj2.push(pj2)
           if (pj1==pj2): #COMPARO EL PERSONAJE SACADO ANTERIORMENTE CON CADA UNO DE LOS OTROS
               print(f"El personaje {pj1} aparece en ambos episodios")
               
       while aux_stackpj2.size() > 0:
         perso_stack2.push(aux_stackpj2.pop())
    
    
               

#CUERPO PRINCIPAL
cargarPila1(personajes_stack1,personajesV)
cargarPila2(personajes_stack2,personajesVII)
print("Pila de personajes episodio V: ")
personajes_stack1.show()
print()
print("Pila de personajes episodio VII: ")
personajes_stack2.show()
print()
interseccionPilas(personajes_stack1,personajes_stack2)