"""
Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra ‘Python’, si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son.
"""

class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora  # Formato HH:MM
        self.app = app
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.hora}] {self.app}: {self.mensaje}"


class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def tamaño(self):
        return len(self.items)

    def ver_todos(self):
        return self.items.copy()


class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def tamaño(self):
        return len(self.items)


"a. escribir una función que elimine de la cola todas las notificaciones de Facebook;"
def eliminar_facebook(cola):
    cola_aux = Cola()
    while not cola.esta_vacia():
        noti = cola.desencolar()
        if noti.app.lower() != "facebook":
            cola_aux.encolar(noti)
    return cola_aux

"b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;"
def mostrar_twitter_python(cola):
    cola_aux = Cola()
    print("\n Notificaciones de Twitter que contienen 'Python':")
    hay_resultados = False
    while not cola.esta_vacia():
        noti = cola.desencolar()
        if noti.app.lower() == "twitter" and "python" in noti.mensaje.lower():
            print(noti)
            hay_resultados = True
        cola_aux.encolar(noti)
    # Restaurar
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())
    if not hay_resultados:
        print("No se encontraron notificaciones de Twitter con 'Python'.")


def esta_entre(hora, h1, h2):
    return h1 <= hora <= h2

"c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son."
def guardar_en_pila_por_hora(cola, hora_inicio="11:43", hora_fin="15:57"):
    pila = Pila()
    cola_aux = Cola()
    while not cola.esta_vacia():
        noti = cola.desencolar()
        if esta_entre(noti.hora, hora_inicio, hora_fin):
            pila.apilar(noti)
        cola_aux.encolar(noti)
    # Restaurar
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())
    return pila.tamaño()


def mostrar_todas(cola):
    print("\n Contenido actual de la cola:")
    for noti in cola.ver_todos():
        print(noti)


# Programa principal 
def menu():
    
    notis = Cola()
    notis.encolar(Notificacion("10:30", "Facebook", "Mirá este video"))
    notis.encolar(Notificacion("11:50", "Twitter", "Python es genial"))
    notis.encolar(Notificacion("12:15", "Instagram", "Nueva historia"))
    notis.encolar(Notificacion("14:00", "Facebook", "Actualización disponible"))
    notis.encolar(Notificacion("15:45", "Twitter", "Curso de Python gratuito"))
    notis.encolar(Notificacion("16:30", "WhatsApp", "Nuevo mensaje"))

    while True:
        print("\n=== MENÚ DE NOTIFICACIONES ===")
        print("1. Eliminar notificaciones de Facebook")
        print("2. Mostrar notificaciones de Twitter con 'Python'")
        print("3. Contar notificaciones entre 11:43 y 15:57")
        print("4. Ver todas las notificaciones")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            notis = eliminar_facebook(notis)
            print(" Notificaciones de Facebook eliminadas.")
        elif opcion == "2":
            mostrar_twitter_python(notis)
        elif opcion == "3":
            cantidad = guardar_en_pila_por_hora(notis)
            print(f" Cantidad de notificaciones entre 11:43 y 15:57: {cantidad}")
        elif opcion == "4":
            mostrar_todas(notis)
        elif opcion == "5":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción inválida. Intente nuevamente.")


# Ejecutar 
menu()
