"""
Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
ción uno la cima de la pila;
b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
car la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
"""

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None

    def tamanio(self):
        return len(self.elementos)

    def copiar(self):
        nueva_pila = Pila()
        nueva_pila.elementos = self.elementos.copy()
        return nueva_pila


pila_mcu = Pila()
personajes = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Groot", "peliculas": 5},
    {"nombre": "Rocket Raccoon", "peliculas": 6},
    {"nombre": "Black Widow", "peliculas": 8},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Gamora", "peliculas": 6},
    {"nombre": "Drax", "peliculas": 5},
    {"nombre": "Captain Marvel", "peliculas": 3},
    {"nombre": "Star-Lord", "peliculas": 6}
]

for personaje in personajes:
    pila_mcu.apilar(personaje)


def procesar_pila(pila):
    pila_aux = pila.copiar()

    posicion_rocket = None
    posicion_groot = None
    personajes_mas_de_5 = []
    peliculas_black_widow = 0
    personajes_cdg = []

    posicion = 1  

    while not pila_aux.esta_vacia():
        personaje = pila_aux.desapilar()
        nombre = personaje["nombre"]
        peliculas = personaje["peliculas"]

        # a. Posiciones de Rocket Raccoon y Groot
        if nombre == "Rocket Raccoon":
            posicion_rocket = posicion
        if nombre == "Groot":
            posicion_groot = posicion

        # b. Más de 5 películas
        if peliculas > 5:
            personajes_mas_de_5.append((nombre, peliculas))

        # c. Películas de Black Widow
        if nombre == "Black Widow":
            peliculas_black_widow = peliculas

        # d. Nombres que empiezan con C, D o G
        if nombre[0].upper() in ['C', 'D', 'G']:
            personajes_cdg.append(nombre)

        posicion += 1

   
    print(f"a. Posición de Rocket Raccoon desde la cima: {posicion_rocket}")
    print(f"a. Posición de Groot desde la cima: {posicion_groot}")

    print("\nb. Personajes con más de 5 películas:")
    for nombre, cantidad in personajes_mas_de_5:
        print(f"- {nombre}: {cantidad} películas")

    print(f"\nc. La Viuda Negra (Black Widow) participó en {peliculas_black_widow} películas.")

    print("\nd. Personajes cuyos nombres empiezan con C, D y G:")
    for nombre in personajes_cdg:
        print(f"- {nombre}")


procesar_pila(pila_mcu)
