# 20. Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro),
# que resuelva las siguientes actividades:

# a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son
# los siguientes:

# I. automóviles (tarifa $47);
# II. camionetas (tarifa $59);
# III. camiones (tarifa $71);
# IV. colectivos (tarifa $64).

# b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
# c. determinar qué cabina recaudó mayor cantidad de pesos ($).
# d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.

from queue import Queue
from vehiculo import Vehiculo
from random import choice

cabina1_queue=Queue()
cabina2_queue=Queue()
cabina3_queue=Queue()

tipos=["Automovil", "Camioneta", "Camion", "Colectivo"]

def cargarCabinas(cabina_queue, tipos, cantidad):
    for cabina in range(cantidad):
        tipo_vehiculo = choice(tipos)
        cabina_queue.arrive(Vehiculo(tipo_vehiculo))

def mayorRecaudoCabina(cab1_queue,cab2_queue,cab3_queue):
    aux1_queue=Queue()
    aux2_queue=Queue()
    aux3_queue=Queue()
    recaudoCabina1=0
    recaudoCabina2=0
    recaudoCabina3=0
    
    while cab1_queue.size()>0:
        cabina1=cab1_queue.attention()
        aux1_queue.arrive(cabina1)
        recaudoCabina1=recaudoCabina1+cabina1.tarifa
    
    while cab2_queue.size()>0:
        cabina2=cab2_queue.attention()
        aux2_queue.arrive(cabina2)
        recaudoCabina2=recaudoCabina2+cabina2.tarifa
        
    while cab3_queue.size()>0:
        cabina3=cab3_queue.attention()
        aux3_queue.arrive(cabina3)
        recaudoCabina3=recaudoCabina3+cabina3.tarifa
        
    if (recaudoCabina1>recaudoCabina2) and (recaudoCabina1>recaudoCabina3):
        print(f"La cabina 1 es la que recaudó mayor cantidad de pesos, con una cantidad de ${recaudoCabina1} pesos.")
    elif (recaudoCabina2>recaudoCabina1) and (recaudoCabina2>recaudoCabina3):
        print(f"La cabina 2 es la que recaudó mayor cantidad de pesos, con una cantidad de ${recaudoCabina2} pesos.")
    else:
        print(f"La cabina 3 es la que recaudó mayor cantidad de pesos, con una cantidad de ${recaudoCabina3} pesos.")
    
    while aux1_queue.size()>0:
        cab1_queue.arrive(aux1_queue.attention())
        
    while aux2_queue.size()>0:
        cab2_queue.arrive(aux2_queue.attention())
        
    while aux3_queue.size()>0:
        cab3_queue.arrive(aux3_queue.attention())
    
def vehiculosAtentidos(cabina_queue):
    c_auto=0
    c_camioneta=0
    c_camion=0
    c_colectivo=0
    
    while cabina_queue.size()>0:
        element=cabina_queue.attention()
        
        if element.tipo=="Automovil":
            c_auto+=1
        elif element.tipo=="Camioneta":
            c_camioneta+=1
        elif element.tipo=="Camion":
            c_camion+=1
        else:
            c_colectivo+=1
        
    print(f"Automovil: {c_auto}")
    print(f"Camioneta: {c_camioneta}")
    print(f"Camion: {c_camion}")
    print(f"Colectivo: {c_colectivo}")
      
#CUERPO PRINCIPAL
cargarCabinas(cabina1_queue,tipos,3) #ACA TENDRIAN QUE SER 10 VEHICULOS DE CADA UNO
cargarCabinas(cabina2_queue,tipos,3)
cargarCabinas(cabina3_queue,tipos,3)
print()
print("Cabina 1 cargada: ")
cabina1_queue.show()
print()
print("Cabina 2 cargada: ")
cabina2_queue.show()
print()
print("Cabina 3 cargada: ")
cabina3_queue.show()
print()
mayorRecaudoCabina(cabina1_queue,cabina2_queue,cabina3_queue)
print()
print("Cantidad de vehículos de cada tipo que se atendieron en la cabina 1: ")
vehiculosAtentidos(cabina1_queue)
print("Cantidad de vehículos de cada tipo que se atendieron en la cabina 2: ")
vehiculosAtentidos(cabina2_queue)
print("Cantidad de vehículos de cada tipo que se atendieron en la cabina 3: ")
vehiculosAtentidos(cabina3_queue)