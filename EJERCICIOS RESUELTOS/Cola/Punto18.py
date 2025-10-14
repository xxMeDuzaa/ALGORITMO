# 18. Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
# letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
# que resuelva las siguientes situaciones:

# a. cargar 1000 turnos de manera aleatoria a la cola.
# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
# y F, y la cola_2 con el resto de los turnos (B, D y E).
# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
# tiene mayor cantidad.
# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
# mayor que 506.

from queue import Queue
from random import choice, randint


turnos_queue = Queue()
cola1_queue = Queue()
cola2_queue = Queue()

listaRandint = ['A', 'B', 'C', 'D', 'E', 'F']


def cargarCola(tur_queue, listaRandint):
    for i in range(5):
        letra = str(choice(listaRandint))
        numero = str(randint(0, 999))
        turno = letra + f"{numero:03}"
        tur_queue.arrive(turno)


def separarColas(turn_queue, col1_queue, col2_queue):
    while turn_queue.size() > 0:
        element = turn_queue.attention()
        if element[0] in ("ACF"):
            col1_queue.arrive(element)
        else:
            col2_queue.arrive(element)


def determinarTurnos(col1_queue, col2_queue):
    contador_letras = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    letraFrecuente = ""
    cantidadLetra = 0

    # Cola mayor y menor
    if col1_queue.size() > col2_queue.size():
        cola_mayor = col1_queue
        cola_menor = col2_queue
        print("La cola 1 es la que tiene mayor cantidad de turnos")
    else:
        cola_mayor = col2_queue
        cola_menor = col1_queue
        print("La cola 2 es la que tiene mayor cantidad de turnos")

    # Contar las letras en la cola mayor
    while cola_mayor.size() > 0:
        turno = cola_mayor.attention()
        letra = turno[0]
        contador_letras[letra] += 1

    # Determinar la letra más frecuente
    for letra in contador_letras:
        if contador_letras[letra] > cantidadLetra:
            letraFrecuente = letra
            cantidadLetra = contador_letras[letra]

    print(f"La letra que más se repite en la cola mayor es '{letraFrecuente}' con {cantidadLetra} apariciones.")

    return cola_menor


def mostrarColaMenor506(colaMenorCantidad):
    while colaMenorCantidad.size() > 0:
        element = colaMenorCantidad.attention()
        numero = int(element[1:])  # Convertir a número el valor después de la letra
        if numero > 506:
            print(element)


# Cuerpo principal
cargarCola(turnos_queue, listaRandint)
print("Cola cargada de turnos aleatorios: ")
turnos_queue.show()
print()

separarColas(turnos_queue, cola1_queue, cola2_queue)
print("Cola 1 que comienza con (A, C, F):")
cola1_queue.show()
print("Cola 2 que comienza con (B, D, E):")
cola2_queue.show()
print()

# Obtener la cola menor de acuerdo con la lógica de la función determinarTurnos
colaMenorCantidad = determinarTurnos(cola1_queue, cola2_queue)
print()
print("Los turnos mayores a 506 de la cola menor: ")
mostrarColaMenor506(colaMenorCantidad)