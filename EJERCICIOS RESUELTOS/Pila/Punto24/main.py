# 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from personaje import Personaje
from stack import Stack

personajes_stack=Stack()

perso1 = Personaje("Iron Man", 3)
perso2 = Personaje("Captain America", 9)
perso3 = Personaje("Black Widow", 7)
perso4 = Personaje("Rocket Raccoon", 5)
perso5 = Personaje("Groot", 5)
perso6 = Personaje("Doctor Strange", 4)
perso7 = Personaje("Gamora", 6)
perso8 = Personaje("Hawkeye", 8)
perso9 = Personaje("Captain Marvel", 3)
perso10 = Personaje("Drax", 4)

personajes = [perso1, perso2, perso3, perso4, perso5, perso6, perso7, perso8, perso9, perso10]

def CargarPila(perso_stack,personajes):
    for pj in personajes:
        perso_stack.push(pj)
        
def determinarPosicion(perso_stack):
    aux_stack=Stack() #pila auxiliar para restaurar la pila original
    pos=0
    encontrados=False
    for i in range(perso_stack.size()):
        pos+=1
        pj=perso_stack.pop()
        aux_stack.push(pj)
        
        if pj.nombre=="Rocket Raccoon" or pj.nombre=="Groot":
            print(f"La posicion en donde se encuentra \033[95m{pj.nombre}\033[0m es: \033[91m{pos}\033[0m")
            encontrados=True
            
    if encontrados==False:
        print("Ninguna, ya que no se encontraron los personajes Rocket Raccoon y Groot.")
            
    while aux_stack.size()>0: #restauro la pila original
        perso_stack.push(aux_stack.pop())

def determinarParticipacion(perso_stack):
    aux_stack=Stack() #pila auxiliar para restaurar la pila original
    encontrado=False
    while perso_stack.size()>0:
        pj=perso_stack.pop()
        aux_stack.push(pj)
        
        if pj.cantidad>5:
            encontrado=True
            print(f"El personaje \033[95m{pj.nombre}\033[0m participo en \033[91m{pj.cantidad}\033[0m peliculas de la saga.")
        
    if encontrado==False:
        print("Ninguno, ya que no hay personajes que participaron en mas de 5 peliculas de la saga.")
        
    while aux_stack.size()>0: #restauro la pila original
        perso_stack.push(aux_stack.pop())

def determinarParticipacionBW(perso_stack):
    aux_stack=Stack() #pila auxiliar para restaurar la pila original
    encontrado=False
    while perso_stack.size()>0:
        pj=perso_stack.pop()
        aux_stack.push(pj)
        
        if pj.nombre=="Black Widow":
            encontrado=True
            print(f"El personaje \033[95m{pj.nombre}\033[0m participo en \033[91m{pj.cantidad}\033[0m peliculas")
            
    if encontrado==False:
        print("Ninguna, ya que no aparece el personaje Black Widow.")
        
    while aux_stack.size()>0: #restauro la pila original
        perso_stack.push(aux_stack.pop())
        
def determinarComienzo(perso_stack):
    aux_stack=Stack() #pila auxiliar para restaurar la pila original
    encontrado=False
    while perso_stack.size()>0:
        pj=perso_stack.pop()
        aux_stack.push(pj)
        
        if pj.nombre[0] in "CDG":
            encontrado=True
            print(f"\033[95m{pj.nombre}\033[0m")
            
    if encontrado==False:
        print("Ninguno, ya que no hay ningun personaje cuyo nombre empieze con C, D y G.")
        
    while aux_stack.size()>0: #restauro la pila original
        perso_stack.push(aux_stack.pop())
        
    
#CUERPO PRINCIPAL
CargarPila(personajes_stack,personajes)
# print("Pila cargada con todos los personajes: ")
# personajes_stack.show()
print()
print("\033[92m¿En qué posición se encuentran los personajes Rocket Raccoon y Groot?:\033[0m")
determinarPosicion(personajes_stack)
print()
print("\033[92mLos personajes que participaron en mas de 5 peliculas de la saga:\033[0m")
determinarParticipacion(personajes_stack)
print()
print("\033[92m¿En cuantas peliculas participo la la Viuda Negra (Black Widow)?:\033[0m")
determinarParticipacionBW(personajes_stack)
print()
print("\033[92mPersonajes cuyos nombre empiezan con C, D y G: \033[0m")
determinarComienzo(personajes_stack)
print()
print("\033[96mTrabajo realizado por: \033[34mAxel Sandillú\033[0m")