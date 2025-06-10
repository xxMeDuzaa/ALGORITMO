from super_heroe_class import *
from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue


def order_by_name(item): return item.name
def order_by_real_name(item): return str(item.real_name) if item.real_name is not None else ""
def order_by_first_appearance(item): return item.first_appearance


superheroesList = List()
superheroesList.add_criterion('name', order_by_name)
superheroesList.add_criterion('real_name', order_by_real_name)
superheroesList.add_criterion('first_appearance', order_by_first_appearance)



for i in range(len(superheroes)):
    data = superheroes[i]
    superheroesList.append(Superheroe(data['name'], data['alias'], data['real_name'], data['short_bio'], data['first_appearance'], data['is_villain']))

def list_villains(personajes: List):
    for personaje in personajes:
        if personaje.is_villain:
            print(personaje.name)

def list_by_initial(personajes: List, char: str):
    for personaje in personajes:
        if personaje.name.startswith(char):
            print(personaje.name)

def list_by_bio(personajes: List, bio: str):
    for personaje in personajes:
        if bio in personaje.short_bio:
            print(f"{personaje.name}:\nShort_bio: {personaje.short_bio}\n")

def queue_villain(personajes: List):
    queue = Queue()
    for personaje in personajes:
        if personaje.is_villain:
            queue.arrive(personaje)
    return queue

def list_by_year(personajes: Queue, year: int):
    for _ in range(personajes.size()):
        personaje = personajes.attention()
        if personaje.first_appearance < year:
            print(personaje.name)




print("------Personajes ordenados por nombre:")
superheroesList.sort_by_criterion('name')
for superheroe in superheroesList:
    print(superheroe.name)
input()

print("-------Posición de personajes:")
print(f"The Thing está en la posición:  {superheroesList.search('The Thing', 'name')}")
print(f"Rocket Raccoon está en la posición:  {superheroesList.search('Rocket Raccoon', 'name')}")
input()

print("-------Villanos:")
list_villains(superheroesList)
input()

print("------ Villanos que aparecieron antes de 1980:")
villainQueue = queue_villain(superheroesList)
list_by_year(villainQueue, 1980)
input()

print("------Superhéroes que comienzan con Bl, G, My, W:")
for prefix in ["Bl", "G", "My", "W"]:
    print(f"\nPersonajes que inician con {prefix}:")
    list_by_initial(superheroesList, prefix)
input()

print("------Personajes ordenados por nombre real:")
superheroesList.sort_by_criterion('real_name')
for superheroe in superheroesList:
    print(f"{superheroe.name}, {superheroe.real_name}")
input()

print("-------Personajes ordenados por fecha de aparición:")
superheroesList.sort_by_criterion('first_appearance')
for superheroe in superheroesList:
    print(f"{superheroe.name}, {superheroe.first_appearance}")
input()

print("-------Modificación del nombre real de Ant Man:")
index = superheroesList.search('Ant Man', 'name')
if index is not None:
    superheroesList[index].real_name = 'Scott Lang'
    print(f"{superheroesList[index].name}, {superheroesList[index].real_name}")
input()

print("------Personajes con 'time-traveling' o 'suit' en la bio: ----------------")
print("Con 'time-traveling':")
list_by_bio(superheroesList, 'time-traveling')
input()
print("Con 'suit':")
list_by_bio(superheroesList, 'suit')
input()

print("------Eliminación de Electro y Baron Zemo:")
electro = superheroesList.delete_value('Electro', 'name')
baron_zemo = superheroesList.delete_value('Baron Zemo', 'name')
print("------Eliminados: ")
if electro:
    print("Eliminado:", electro.name)
else:
    print("Electro no encontrado.")
if baron_zemo:
    print("Eliminado:", baron_zemo.name)
else:
    print("Baron Zemo no encontrado.")


