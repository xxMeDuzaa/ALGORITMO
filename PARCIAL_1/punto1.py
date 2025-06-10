from super_heroes_data import superheroes
from random import randint

superheroe_List = []

for _ in range(15):
    superheroe_List.append(superheroes[randint(1, 100)]['name'])


def recursiveSearch(array: list, personaje: str, posicion = 0):
    if array[0] == personaje:
        return posicion
    elif len(array) == 1:
        return -1
    else:
        return recursiveSearch(array[1:], personaje, posicion + 1)

def recursiveShow(array: list):
    if len(array) == 0:
        return None
    else:
        print(array[0])
        return recursiveShow(array[1:])

searchIndex = recursiveSearch(superheroe_List, 'Captain America')

print("-------Lista de superheroes: ------")
recursiveShow(superheroe_List)

input()

if searchIndex == -1:
    print('Capitan America no esta en la lista')
else:
    print(f'Capitan America esta en la posicion {searchIndex+1}')
print()
