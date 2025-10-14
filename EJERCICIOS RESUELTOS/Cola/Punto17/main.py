# 17. Desarrollar un algoritmo que permita cargar procesos a la cola de ejecución de un procesador,
# de los cuales se conoce id del proceso y tiempo de ejecución. Resuelva las siguientes situaciones:

# a. simular la atención de los procesos de la cola transcurriendo su tiempo –utilizando la fun-
# ción time.sleep (segundos) – hasta que se vacíe la cola.

# b. considerar que el quantum de tiempo asignado por el procesador a cada proceso es como
# máximo 4.5 segundos –si el proceso no terminó su ejecución deberá volver a la cola con el
# tiempo restante para terminar su ejecución–.

# c. cuando se realiza el cambio de proceso, porque finalizó su ejecución o porque se le agotó el
# quantum de tiempo, se pueden ingresar nuevos procesos a la cola por el usuario.

# d. no se aplican criterios de prioridad en los procesos.

from procesador import Procesador
from queue import Queue
import time

procesos_queue=Queue()

proceso1 = Procesador("76", 6)
proceso2 = Procesador("88", 2.5)
proceso3 = Procesador("3343", 4)
proceso4 = Procesador("342", 1.5)
proceso5 = Procesador("13", 7.5)

procesos=[proceso1,proceso2,proceso3,proceso4,proceso5]

def cargarCola(proce_queue,procesos):
    for pj in procesos:
        proce_queue.arrive(pj)

def atenderProcesos(proce_queue):
    while proce_queue.size() > 0:
        proceso = proce_queue.attention()
        
        if proceso.tiempo <= 4.5:
            print(f"Ejecutando proceso {proceso.idProceso} ({proceso.tiempo} segundos)...")
            time.sleep(proceso.tiempo)
            print(f"Proceso {proceso.idProceso} finalizado.")
            print()
        else:
            print(f"Ejecutando proceso {proceso.idProceso} (mayor a 4.5 segundos de quantum)...")
            time.sleep(4.5)
            tiempo_restante = (proceso.tiempo - 4.5)
            print(f"Proceso {proceso.idProceso} no finalizado (excedido de segundos). Tiempo restante: {tiempo_restante} segundos.")
            print("Este proceso sera retomado nuevamente mas adelante.")
            print()
            # Creo un nuevo objeto con el tiempo restante y lo vuelvo a agregar a la cola
            proceso_restante = Procesador(proceso.idProceso, tiempo_restante)
            proce_queue.arrive(proceso_restante)
    
    cargarNuevosProcesos(proce_queue)
        
def cargarNuevosProcesos(proce_queue):
    agregar = input("¿Desea agregar un nuevo proceso? (s/n): ").lower()
    if agregar == "s":
        id_nuevo = input("Ingrese el ID del nuevo proceso: ")
        tiempo_nuevo = float(input("Ingrese el tiempo de ejecución del nuevo proceso: "))
        nuevo_proceso = Procesador(id_nuevo, tiempo_nuevo)
        proce_queue.arrive(nuevo_proceso)    


#CUERPO PRINCIPAL
cargarCola(procesos_queue,procesos)
print("Cola cargada de procesos de un procesador: ")
procesos_queue.show()
print()
atenderProcesos(procesos_queue)
print()
print("Cola final: ")
procesos_queue.show()