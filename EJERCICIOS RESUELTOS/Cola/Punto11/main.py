# 11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:

from queue import Queue
from starwars import StarWars
    
personajes_queue= Queue()

personajes=[
    StarWars("Luke Skywalker","Tatooine"),
    StarWars("Leia Organa","Alderaan"),
    StarWars("Han Solo", "Corellia"),
    StarWars("Yoda", "Dagobah"),
    StarWars("Jar Jar Binks","Tatooine"),
    StarWars("Darth Vader", "Endor"),
        
]

def cargarCola(perso_queue,personajes):
    for pj in personajes:
        perso_queue.arrive(pj)
        
        
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
def mostrarPJPlanetas(perso_queue):
    encontrado=False
    tamañoCola=perso_queue.size()
    
    for i in range(tamañoCola):
        pj=perso_queue.on_front()
        
        if pj.planeta in ("Alderaan","Endor","Tatooine"):
            encontrado=True
            print(f"{pj.nombre}")
            
        perso_queue.move_to_end()
            
    if not encontrado:
        print("No se han encontrado personajes del platena Alderaan, Endor y Tatooine.")
        
        
# b. indicar el plantea natal de Luke Skywalker y Han Solo
def planetaNatal(perso_queue):
    encontrado=False
    tamañoCola=perso_queue.size()
    
    for i in range(tamañoCola):
        pj=perso_queue.on_front()
        
        if pj.nombre in ("Luke Skywalker", "Han Solo"):
            encontrado=True
            print(f"El planeta natal de {pj.nombre} es: {pj.planeta}")
            
        perso_queue.move_to_end()
              
    if not encontrado:
        print("No se han encontrado personajes Luke Skywalker y Han Solo.")
        
        
def insertarPjEspecifico(perso_queue):
    aux_queue=Queue()
    encontrado=False

    while perso_queue.size()>0:
        pj=perso_queue.attention()
        if pj.nombre=="Yoda" and not encontrado:
            encontrado=True
            nuevoPJ=StarWars("Obi-Wan Kenobi", "Stewjon")
            aux_queue.arrive(nuevoPJ)  # insertar primero a Obi-Wan
        aux_queue.arrive(pj)

    if not encontrado:
        print("No se encontro el personaje Maestro Yoda.")

    while aux_queue.size()>0:
        perso_queue.arrive(aux_queue.attention())

        
def eliminarPjEspecifico(perso_queue):
    aux_queue=Queue()
    encontrado=False
    while perso_queue.size()>0:
        pj=perso_queue.attention()
        if pj.nombre=="Jar Jar Binks" and not encontrado:
            encontrado=True
            aux_queue.arrive(pj)  # guardar Jar Jar
            if perso_queue.size()>0:
                perso_queue.attention()  # eliminar el siguiente personaje
        else:
            aux_queue.arrive(pj)

    if not encontrado:
        print("No se encontro el personaje Jar Jar Binks.")

    while aux_queue.size()>0:
        perso_queue.arrive(aux_queue.attention())


#CP
cargarCola(personajes_queue,personajes)
print("Personajes del planeta Alderaan, Endor y Tatooine: ")
mostrarPJPlanetas(personajes_queue)
print()
print("Planeta natal de Luke Skywalker y Han Solo: ")
planetaNatal(personajes_queue)
print()
insertarPjEspecifico(personajes_queue)
print("Cola despues de insertar un nuevo personaje despues del Maestro yoda: ")
personajes_queue.show()
print()
eliminarPjEspecifico(personajes_queue)
print("Cola despues de eliminar un personaje ubicado despues de Jar Jar Binks: ")
personajes_queue.show()