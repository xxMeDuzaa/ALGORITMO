# 15. Suponga que se escapa hacia el planeta tierra en un Caza TIE robado –huyendo de un Destruc-
# tor Estelar y necesita localizar la base rebelde más cercana– y se tiene una cola con informa-
# ción de las bases rebeldes en la tierra de las cuales conoce su nombre, número de flota aérea,
# coordenadas de latitud y longitud. Desarrolle un algoritmo que permita resolver las siguientes
# tareas una vez que aterrice:
# a. determinar cuál es la base rebelde más cercana desde su posición actual.
# b. para el cálculo de la distancia deberá utilizar la fórmula de Haversine:

# donde r es el radio medio de la tierra en metros (6371000), φ1 y φ2 las latitudes de los
# dos puntos –por ejemplo coordenadas actual–, λ1 y λ2 las longitudes de los dos puntos
# –coordenadas de la base– ambos expresadas en radianes; para convertir de grados a
# radianes utilice la función math.radians(ángulo coordenada).

# c. mostrar el nombre y la distancia a la que se encuentran las tres bases más cercanas y deter-
# minar cual tiene mayor flota aérea.

# d. determinar la distancia hasta la base rebelde con mayor flota aérea.

from basesRebeldes import BasesRebeldes
from queue import Queue
from math import radians, sin, cos, sqrt, atan2

basesRebeldes_queue=Queue()

base1 = BasesRebeldes("Base Echo", 50, 40.7128, -74.0060) 
base2 = BasesRebeldes("Base Delta", 80, 34.0522, -118.243)
base3 = BasesRebeldes("Base Nova", 60, 41.8781, -87.6298)       
base4 = BasesRebeldes("Base Aurora", 45, 29.7604, -95.3698)    
base5 = BasesRebeldes("Base Solaris", 70, 33.4484, -112.0740)   

bases=[base1, base2, base3, base4, base5]

def cargarCola(bases_queue,bases):
    for pj in bases:
        bases_queue.arrive(pj)
    
#b)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Radio de la Tierra en metros
    φ1 = radians(lat1)
    φ2 = radians(lat2)
    Δφ = radians(lat2 - lat1)
    Δλ = radians(lon2 - lon1)

    a = sin(Δφ / 2)**2 + cos(φ1) * cos(φ2) * sin(Δλ / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def baseMasCercana(bases_queue, lat_actual, lon_actual):
    aux_queue = Queue()
    min_distancia = 999999999 #un valor alto
    base_mas_cercana = None

    while bases_queue.size()>0:  
        base = bases_queue.attention()  
        aux_queue.arrive(base)    

        distancia = haversine(lat_actual, lon_actual, base.latitud, base.longitud)
        if distancia < min_distancia:
            min_distancia = distancia
            base_mas_cercana = base

    # Restaurar la cola original
    while aux_queue.size()>0:
        bases_queue.arrive(aux_queue.attention())

    return base_mas_cercana, min_distancia

def tresBasesMasCercanas(bases_queue, lat_actual, lon_actual):
    aux_queue = Queue()
    basesCerca_queue=Queue()

    while bases_queue.size()>0:
        base = bases_queue.attention()
        aux_queue.arrive(base)  # Guardamos en la cola auxiliar

        # Calcular la distancia usando Haversine
        distancia = haversine(lat_actual, lon_actual, base.latitud, base.longitud)
        basesCerca_queue.arrive((base, distancia))
        
    while basesCerca_queue.size()>0:
        print(basesCerca_queue.attention())

    # Restaurar la cola original
    while aux_queue.size()>0:
        bases_queue.arrive(aux_queue.attention())  # Restaurar a la cola original



        
#CUERPO PRINCIPAL
#La posicion actual podria ser:
latitud_actual = 36.0
longitud_actual = -100.0
cargarCola(basesRebeldes_queue,bases)
print("Cola cargada de bases Rebeldes en la tierra: ")
basesRebeldes_queue.show()
base_cercana, distancia = baseMasCercana(basesRebeldes_queue, latitud_actual, longitud_actual)
print()
print(f"La base más cercana es: {base_cercana.nombre}")
print(f"Se encuentra a una distancia de: {(distancia/1000)} km")
print()
print("Las 3 bases mas cercanas:")
tresBasesMasCercanas(basesRebeldes_queue,latitud_actual,longitud_actual)