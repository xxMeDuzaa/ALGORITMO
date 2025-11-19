"""
Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce 
el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
–por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, 
Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
"""


class PersonajeMCU:
    def __init__(self, nombre_real, nombre_heroe, genero):
        self.nombre_real = nombre_real
        self.nombre_heroe = nombre_heroe
        self.genero = genero  # 'M' o 'F'

    def __str__(self):
        return f"{self.nombre_real} - {self.nombre_heroe} - {'Masculino' if self.genero == 'M' else 'Femenino'}"


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_todos(self):
        return self.items.copy()



def buscar_personaje_por_heroe(cola, nombre_heroe):
    cola_aux = Cola()
    personaje = None
    while not cola.esta_vacia():
        item = cola.desencolar()
        if item.nombre_heroe.lower() == nombre_heroe.lower():
            personaje = item.nombre_real
        cola_aux.encolar(item)
    # Restaurar la cola original
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())
    return personaje


def mostrar_heroes_femeninos(cola):
    cola_aux = Cola()
    print("\n Superhéroes femeninos:")
    for item in cola.ver_todos():
        if item.genero == 'F':
            print(f"- {item.nombre_heroe}")
        cola_aux.encolar(item)


def mostrar_personajes_masculinos(cola):
    cola_aux = Cola()
    print("\n Personajes masculinos:")
    for item in cola.ver_todos():
        if item.genero == 'M':
            print(f"- {item.nombre_real}")
        cola_aux.encolar(item)


def buscar_heroe_por_personaje(cola, nombre_personaje):
    cola_aux = Cola()
    heroe = None
    while not cola.esta_vacia():
        item = cola.desencolar()
        if item.nombre_real.lower() == nombre_personaje.lower():
            heroe = item.nombre_heroe
        cola_aux.encolar(item)
    # Restaurar
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())
    return heroe


def mostrar_datos_que_empiezan_con_s(cola):
    cola_aux = Cola()
    print("\n Personajes o superhéroes que comienzan con 'S':")
    for item in cola.ver_todos():
        if item.nombre_real.startswith("S") or item.nombre_heroe.startswith("S"):
            print(item)
        cola_aux.encolar(item)


def verificar_carol_danvers(cola):
    cola_aux = Cola()
    encontrado = False
    nombre_heroe = ""
    for item in cola.ver_todos():
        if item.nombre_real.lower() == "carol danvers":
            encontrado = True
            nombre_heroe = item.nombre_heroe
        cola_aux.encolar(item)
    if encontrado:
        print(f"\n Carol Danvers está en la cola. Su nombre de superhéroe es: {nombre_heroe}")
    else:
        print("\n Carol Danvers no se encuentra en la cola.")


def mostrar_todos(cola):
    print("\n Todos los personajes en la cola:")
    for item in cola.ver_todos():
        print(item)


# Programa principal 
def menu():
    personajes = Cola()
    personajes.encolar(PersonajeMCU("Tony Stark", "Iron Man", "M"))
    personajes.encolar(PersonajeMCU("Steve Rogers", "Capitán América", "M"))
    personajes.encolar(PersonajeMCU("Natasha Romanoff", "Black Widow", "F"))
    personajes.encolar(PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"))
    personajes.encolar(PersonajeMCU("Scott Lang", "Ant-Man", "M"))
    personajes.encolar(PersonajeMCU("Stephen Strange", "Doctor Strange", "M"))
    personajes.encolar(PersonajeMCU("Wanda Maximoff", "Scarlet Witch", "F"))
    personajes.encolar(PersonajeMCU("Shuri", "Black Panther", "F"))

    while True:
        print("\n=== MENÚ MCU ===")
        print("a. Obtener nombre del personaje de Capitana Marvel")
        print("b. Mostrar nombres de superhéroes femeninos")
        print("c. Mostrar nombres de personajes masculinos")
        print("d. Obtener nombre del superhéroe de Scott Lang")
        print("e. Mostrar datos que empiezan con 'S'")
        print("f. Verificar si Carol Danvers está en la cola")
        print("g. Ver todos los personajes")
        print("h. Salir")

        opcion = input("Elegí una opción: ").lower()

        if opcion == 'a':
            nombre = buscar_personaje_por_heroe(personajes, "Capitana Marvel")
            if nombre:
                print(f"\n El personaje detrás de Capitana Marvel es: {nombre}")
            else:
                print("\n No se encontró el personaje.")
        elif opcion == 'b':
            mostrar_heroes_femeninos(personajes)
        elif opcion == 'c':
            mostrar_personajes_masculinos(personajes)
        elif opcion == 'd':
            heroe = buscar_heroe_por_personaje(personajes, "Scott Lang")
            if heroe:
                print(f"\n El nombre de superhéroe de Scott Lang es: {heroe}")
            else:
                print("\n No se encontró a Scott Lang.")
        elif opcion == 'e':
            mostrar_datos_que_empiezan_con_s(personajes)
        elif opcion == 'f':
            verificar_carol_danvers(personajes)
        elif opcion == 'g':
            mostrar_todos(personajes)
        elif opcion == 'h':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")


# Ejecutar
menu()
