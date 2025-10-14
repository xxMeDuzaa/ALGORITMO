# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:

# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;

# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

from stack import Stack
from queue import Queue
from notification import Notification

notificacion_queue = Queue()

# Crear objetos
notificacion1 = Notification(07.15, "WhatsApp", "Te enviaron una foto nueva")
notificacion2 = Notification(08.00, "Facebook", "Nueva historia publicada")
notificacion3 = Notification(11.43, "Twitter", "Tienes 3 nuevas notificaciones")
notificacion4 = Notification(12.57, "Facebook", "Alguien reaccionó a tu publicación")
notificacion5 = Notification(15.57, "Twitter", "Nuevo video sugerido para ti de Python")

notificaciones=[notificacion1,notificacion2,notificacion3,notificacion4,notificacion5]

def cargarCola(noti_queue,notificaciones):
    for noti in notificaciones:
        noti_queue.arrive(noti)
        
def eliminarNotiFacebook(noti_queue):
    encontrado=False
    aux_queue=Queue() #cola auxiliar para guardar las notis que no sean de facebook
    aux_restablecer=Queue() #cola para despues restablecer la cola original
    while noti_queue.size()>0:
        noti=noti_queue.attention()
        aux_restablecer.arrive(noti)
        if noti.aplicacion=="Facebook":
            encontrado=True
        else:
            aux_queue.arrive(noti) #guardo aquellas notificaciones que no sean de Facebook
            
    if encontrado==False:
        print("No se encontraron notificaciones de Facebook.")
    
    while aux_restablecer.size()>0: #restablezco la cola original
        noti_queue.arrive(aux_restablecer.attention())
        
    return aux_queue #returnamos aquellas notis que no sean de facebook

def mostrarNotiTwitter(noti_queue):
    encontrado=False
    aux_queue=Queue() #cola auxiliar para guardar las notis de Twitter (teniendo en cuenta que incluya el mensaje python)
    aux_restablecer=Queue() #cola para despues restablecer la cola original
    while noti_queue.size()>0:
        noti=noti_queue.attention()
        aux_restablecer.arrive(noti)
        if noti.aplicacion=="Twitter":
            if "Python" in noti.mensaje:
                encontrado=True
                aux_queue.arrive(noti)
                
    if encontrado==False:
        print("No se encontraron notificaciones de Twitter cuyo mensaje incluya la palabra Python.")
    
    while aux_restablecer.size()>0: #restablezco la cola original
        noti_queue.arrive(aux_restablecer.attention())
        
    return aux_queue #returnamos la cola auxiliar que guarda las notis de twitter que incluya la palabra python
      
def notiHorario(noti_queue):
    encontrado=False
    c_horario=0
    aux_stack=Stack()
    while noti_queue.size()>0:
        noti=noti_queue.attention()
        if noti.hora>=11.43 and noti.hora<=15.57:
            encontrado=True
            aux_stack.push(noti)
            c_horario+=1
     
    if encontrado==False:
        print("No se encontro ninguna notificacion producidas entre las 11:43 y las 15:57. ")     
    
    return aux_stack,c_horario
            

cargarCola(notificacion_queue,notificaciones)
# print("Cola Original: ")
# notificacion_queue.show()
print()
eliminarFacebook=eliminarNotiFacebook(notificacion_queue)
print("\033[92mCola sin notificaciones de Facebook:\033[0m")
eliminarFacebook.show()
print()
mensajeTwitter=mostrarNotiTwitter(notificacion_queue)
if mensajeTwitter.size() > 0:
    print("\033[92mCola con notificaciones de Twitter en donde el mensaje incluya la palabra Python:\033[0m")
    mensajeTwitter.show()
print()
horarioProducido,contador_horarios=notiHorario(notificacion_queue)
if contador_horarios>0:
    print(f"\033[92mPila con las notificaciones producidas entre las 11:43 y las 15:57 con una cantidad de\033[0m \033[91m{contador_horarios}\033[0m\033[92m:\033[0m ")
    horarioProducido.show()
print()
print("\033[96mTrabajo realizado por: \033[34mAxel Sandillú\033[0m")