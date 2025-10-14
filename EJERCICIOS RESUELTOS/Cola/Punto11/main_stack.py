# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:

# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine

# b. indicar el plantea natal de Luke Skywalker y Han Solo

# c. insertar un nuevo personaje antes del maestro Yoda

# d. eliminar el personaje ubicado después de Jar Jar Binks

from starwars import StarWars
from queue import Queue

personajes_queue= Queue()

nuevo_personaje=StarWars("Obi-Wan Kenobi", "Stewjon")

perso1=StarWars("Luke Skywalker","Tatooine")
perso2=StarWars("Leia Organa","Alderaan")
perso3=StarWars("Han Solo", "Corellia")
perso4=StarWars("Yoda", "Dagobah")
perso5=StarWars("Jar Jar Binks","Tatooine")
perso6=StarWars("Darth Vader", "Endor")


personajes=[perso1,perso2,perso3,perso4,perso5,perso6]

def cargarCola(perso_queue,personajes):
    for pj in personajes:
        perso_queue.arrive(pj)
        
def mostrarPJ(perso_queue):
    encontrado=False
    aux_queue=Queue()
    aux_restablecer= Queue() #auxiliar para restablecer a la cola original
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_restablecer.arrive(pj)
        if pj.planeta in ("Alderaan", "Endor", "Tatooine"): #verifico si esta el planeta
            encontrado=True
            aux_queue.arrive(pj)
    
    if encontrado==False:
        print("No se encontraron personajes del planeta Alderaan, Endor y Tatooine")
    
    while aux_restablecer.size()>0: #reestablezco la cola original
        perso_queue.arrive(aux_restablecer.attention())
        
    return aux_queue #returnamos aquellos personajes que aparecen en el planeta requerido
      
def indicarPlaneta(perso_queue):
    encontrado=False
    aux_queue=Queue()
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_queue.arrive(pj)
        if pj.nombre in ("Luke Skywalker","Han Solo"): #verifico si estan los nombres
            encontrado=True
            print(f"Se encontro que {pj.nombre} es del planeta natal: {pj.planeta}")
    
    if encontrado==False:
        print("No se encontraron los personajes Luke Skywalker y Han Solo")    
        
    while aux_queue.size()>0: #restauramos la cola original
        perso_queue.arrive(aux_queue.attention())
        
def insertarAntesYoda(perso_queue,nuevo_pj):
    aux_queue=Queue()
    encontrado=False
    insertado=False
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        if pj.nombre=="Yoda" and insertado==False:
            insertado=True
            encontrado=True
            aux_queue.arrive(nuevo_pj)
        aux_queue.arrive(pj) #tengo que ir guardando despues asi queda antes del Maestro Yoda
        
    if encontrado==False:
        print("No se encontro el personaje Maestro Yoda")
        
    while aux_queue.size()>0:
        perso_queue.arrive(aux_queue.attention())
    
def eliminarPersonaje(perso_queue):
    aux_queue=Queue()
    encontrado=False
    eliminado=False
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        aux_queue.arrive(pj)
        if pj.nombre=="Jar Jar Binks" and eliminado==False:
            encontrado=True
            eliminado=True
            perso_queue.attention() #eliminamos el siguiente sacandolo antes y asi evitamos que se meta al while
    
    if encontrado==False:
        print("No se encontro el personaje Jar Jar Binks.")
    
    while aux_queue.size()>0: #reestablezco la cola original
        perso_queue.arrive(aux_queue.attention())
            
#CUERPO PRINCIPAL
cargarCola(personajes_queue,personajes)
print("Cola original: ")
personajes_queue.show()
print()
planetaRequerido=mostrarPJ(personajes_queue)
if planetaRequerido.size()>0: #verifico si hay personajes
    print("Cola de personajes que aparecen en los planetas Alderaan, Endor y Tatooine: ")
    planetaRequerido.show()
print()
indicarPlaneta(personajes_queue)
print()
print("Cola original insertando un nuevo personaje antes del Maestro Yoda (si es que el mismo esta): ")
insertarAntesYoda(personajes_queue,nuevo_personaje)
personajes_queue.show()
print()
print("Cola original eliminando el personaje ubicado después de Jar Jar Binks (si es que este existe): ")
eliminarPersonaje(personajes_queue)
personajes_queue.show()