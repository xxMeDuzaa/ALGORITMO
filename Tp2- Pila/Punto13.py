"""
Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
las siguientes actividades:

a) determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
además mostrar el nombre de dichas películas
B) mostrar los modelos que quedaron dañados, sin perder información de la pila.
C) eliminar los modelos de los trajes destruidos mostrando su nombre.
D) un modelo de traje puede usarse en más de una película y en una película se pueden usar
más de un modelo de traje, estos deben cargarse por separado.
E) agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
repetidos en una misma película;
F) mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
“Capitan America: Civil War”.

"""
from stack import Stack

personajesMCU = Stack()

personajes = [
    ("Iron Man", 10),
    ("Captain America", 9),
    ("Groot", 5),
    ("Rocket Raccoon", 6),
    ("Black Widow", 8),
    ("Doctor Strange", 4),
    ("Gamora", 6),
    ("Drax", 5),
    ("Captain Marvel", 3),
    ("Star-Lord", 6)
]

for personaje in personajes:
    personajesMCU.push(personaje)

# A) Posición de Rocket Raccoon y Groot
def buscarPersonajes(pila):
    aux = Stack()
    pos = 1
    posRocket = None
    posGroot = None

    while not pila.is_empty():
        personaje = pila.pop()
        aux.push(personaje)
        if personaje[0] == "Rocket Raccoon":
            posRocket = pos
        if personaje[0] == "Groot":
            posGroot = pos
        pos += 1

    while not aux.is_empty():
        pila.push(aux.pop())

    print("\na) Posición desde la cima de la pila:")
    print(f"- Rocket Raccoon: {posRocket if posRocket else 'No encontrado'}")
    print(f"- Groot: {posGroot if posGroot else 'No encontrado'}")

# B) Personajes con más de 5 películas
def masDe5Peliculas(pila):
    aux = Stack()
    print("\nb) Personajes con más de 5 películas:")
    hay = False

    while not pila.is_empty():
        personaje = pila.pop()
        aux.push(personaje)
        if personaje[1] > 5:
            print(f"- {personaje[0]}: {personaje[1]} películas")
            hay = True

    if not hay:
        print("Ninguno.")

    while not aux.is_empty():
        pila.push(aux.pop())

# C) Películas de Black Widow
def cantidadBlackWidow(pila):
    aux = Stack()
    cantidad = 0

    while not pila.is_empty():
        personaje = pila.pop()
        aux.push(personaje)
        if personaje[0] == "Black Widow":
            cantidad = personaje[1]

    while not aux.is_empty():
        pila.push(aux.pop())

    print(f"\nc) Black Widow participó en {cantidad} película(s).")

# D) Personajes que empiezan con C, D y G
def nombresCDG(pila):
    aux = Stack()
    encontrados = []

    while not pila.is_empty():
        personaje = pila.pop()
        aux.push(personaje)
        if personaje[0][0].upper() in ['C', 'D', 'G']:
            encontrados.append(personaje[0])

    while not aux.is_empty():
        pila.push(aux.pop())

    print("\nd) Personajes cuyos nombres empiezan con C, D y G:")
    if encontrados:
        for nombre in encontrados:
            print(f"- {nombre}")
    else:
        print("Ninguno.")


def mostrarPersonajes(pila):
    aux = Stack()
    print("\nPERSONAJES EN LA PILA (de cima a base):")
    while not pila.is_empty():
        personaje = pila.pop()
        aux.push(personaje)
        print(f"- {personaje[0]} ({personaje[1]} películas)")
    while not aux.is_empty():
        pila.push(aux.pop())







# Menú
import os

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def mostrarMenu():
    print("-----> MENÚ PRINCIPAL DE LA PILA DE PERSONAJES MCU <-----")
    print("1. Ver personajes cargados")
    print("2. Ver posición de Rocket Raccoon y Groot")
    print("3. Ver personajes con más de 5 películas")
    print("4. Ver cantidad de películas de Black Widow")
    print("5. Ver personajes cuyos nombres empiezan con C, D o G")
    print("6. Salir")

opcion = 0
while opcion != 6:
    limpiar_consola()
    mostrarMenu()
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if opcion == 1:
        limpiar_consola()
        mostrarPersonajes(personajesMCU)
        input("\nPresione Enter para continuar...")
    elif opcion == 2:
        limpiar_consola()
        buscarPersonajes(personajesMCU)
        input("\nPresione Enter para continuar...")
    elif opcion == 3:
        limpiar_consola()
        masDe5Peliculas(personajesMCU)
        input("\nPresione Enter para continuar...")
    elif opcion == 4:
        limpiar_consola()
        cantidadBlackWidow(personajesMCU)
        input("\nPresione Enter para continuar...")
    elif opcion == 5:
        limpiar_consola()
        nombresCDG(personajesMCU)
        input("\nPresione Enter para continuar...")
    elif opcion == 6:
        print("\nSaliendo del programa...")
    else:
        print("Opción no válida.")
