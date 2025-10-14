from vuelo import Vuelo
from queue import Queue

despegue_queue = Queue()
aterrizaje_queue = Queue()

despegues = [
    Vuelo("Aerolíneas Argentinas", 8.30, None, "Cordoba", "Buenos Aires", "pasajeros"),
    Vuelo("LATAM", 9.00, None, "Buenos Aires", "Misiones", "negocios"),
    Vuelo("JetsPrivados", 10.30, None, "Montevideo", "Entre Rios", "negocios"),
    Vuelo("CargaSur", 10.00, None, "Buenos Aires", "Tierra del Fuego", "carga"),
    
]

aterrizajes = [
    Vuelo("Aerolíneas Argentinas", None, 10.0, "Cordoba", "Buenos Aires", "pasajeros"),
    Vuelo("LATAM", None, 13.00,"Buenos Aires", "Misiones", "pasajeros"),
    Vuelo("JetsPrivados", None, 15.00, "Montevideo", "Entre Rios", "negocios"),
    Vuelo("CargaSur", None, 13.30, "Buenos Aires", "Tierra del Fuego", "carga"),
]

def cargarDespegues(desp_queue, despegues):
    despegues.sort(key=lambda vuelo: vuelo.get_hora_salida())  # Ordenar por hora de salida
    for vuelo in despegues:
        desp_queue.arrive(vuelo)  # Cargar el vuelo completo en la cola de despegue

def cargarAterrizajes(ate_queue, aterrizajes):
    aterrizajes.sort(key=lambda vuelo: vuelo.get_hora_llegada())  # Ordenar por hora de llegada
    for vuelo in aterrizajes:
        ate_queue.arrive(vuelo)  # Cargar el vuelo completo en la cola de aterrizaje

#CUERPO PRINCIPAL:
cargarDespegues(despegue_queue, despegues)
cargarAterrizajes(aterrizaje_queue, aterrizajes)
print("Vuelos de Despegue:")
despegue_queue.show()
print()
print("Vuelos de Aterrizaje:")
aterrizaje_queue.show()