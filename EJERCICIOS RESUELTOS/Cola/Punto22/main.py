# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
# –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

from personaje import Personaje
from queue import Queue

personajes_queue=Queue()

perso1 = Personaje("Tony Stark", "Iron Man", "M")
perso2 = Personaje("Steve Rogers", "Capitán América", "M")
perso3 = Personaje("Natasha Romanoff", "Black Widow", "F")
perso4 = Personaje("Carol Danvers", "Capitana Marvel", "F")
perso5 = Personaje("Scott Lang", "Ant-Man", "M")

personajes=[perso1,perso2,perso3,perso4,perso5]

def cargarCola(perso_queue,personajes):
    for pj in personajes:
        perso_queue.arrive(pj)

def determinarNombrePJ(perso_queue):
    
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()
        
        if pj.nombreSH=="Capitana Marvel":
            print(f"\033[95m{pj.nombrePJ}\033[0m")
    
        perso_queue.move_to_end()
 
def nombresPjFemeninos(perso_queue): 
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()
        
        if pj.genero=="F":
            print(f"\033[95m{pj.nombreSH}\033[0m")
            
        perso_queue.move_to_end()
    
def nombresPjMasculinos(perso_queue):
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()

        if pj.genero=="M":
            print(f"\033[95m{pj.nombrePJ}\033[0m")
            
        perso_queue.move_to_end()
  
def determinarNombreSH(perso_queue):
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()
        
        if pj.nombrePJ=="Scott Lang":
            print(f"\033[95m{pj.nombreSH}\033[0m")
            
        perso_queue.move_to_end()
  
def nombreComienzaS(perso_queue):
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()
        
        if pj.nombrePJ[0]=="S":
            print(f"Nombre del personaje: \033[95m{pj.nombrePJ}\033[0m, Nombre del Superhéroe: \033[95m{pj.nombreSH}\033[0m, Género: \033[91m{pj.genero}\033[0m")
            
        perso_queue.move_to_end()  
        
def determinarPersonaje(perso_queue):
    encontrado=False
    for i in range(perso_queue.size()):
        pj=perso_queue.on_front()
        
        if pj.nombrePJ=="Carol Danvers":
            encontrado=True
            print(f"Si, su nombre de Superhéroe es: \033[95m{pj.nombreSH}\033[0m")
        
        perso_queue.move_to_end()
    
    if encontrado==False:
        print("No, no se encontro el personaje Carol Danvers.")
               
#CUERPO PRINCIPAL
cargarCola(personajes_queue,personajes)
# print("Cola cargada de personajes de Marvel Cinematic Universe: ")
# personajes_queue.show()
print()
print("\033[92mEl nombre de la personaje de la Superhéroe Capitana Marvel es:\033[0m")
determinarNombrePJ(personajes_queue)
print()
print("\033[92mNombres de personajes femeninos:\033[0m")
nombresPjFemeninos(personajes_queue)
print()
print("\033[92mNombres de personajes Masculinos:\033[0m")
nombresPjMasculinos(personajes_queue)
print()
print("\033[92mNombre del superhéroe del personaje Scott Lang:\033[0m")
determinarNombreSH(personajes_queue)
print()
print("\033[92mTodos los datos de personajes cuyo nombre comienza con S:\033[0m")
nombreComienzaS(personajes_queue)
print()
print("\033[92m¿El personaje Carol Danvers se encuentra en la cola?:\033[0m")
determinarPersonaje(personajes_queue)
print()
print("\033[96mTrabajo realizado por: \033[34mAxel Sandillú\033[0m")