# 16. Se deben administrar las actividades de un proyecto de software, de estas se conoce su costo,
# tiempo de ejecución, fecha de inicio, fecha de fin estimada, fecha de fin efectiva y persona a
# cargo. Desarrollar un algoritmo que realice las siguientes actividades:


from list_ import List
from datetime import datetime
from actividad import Actividad

list_actividades=List()

actividades = [
    Actividad(1500, 40, 2024, 2025, 2026, "Ana"),
    Actividad(2000, 60, 2024, 2026, 2025, "Juan"),
    Actividad(800, 20, 2020, 2020, 2022, "Ana"),
    Actividad(3000, 80, 2019, 2022, None, "Pedro"),
    Actividad(1200, 30, 2018, 2023, 2021, "Juan"),
]


def cargarLista(list_act, actividades):
    for actividad in actividades:
        list_act.append(actividad)

# a. tiempo promedio de tareas;
def promedioTareas(list_act):
    promedio=0
    sumatoria=0
    for actividad in list_act:
        sumatoria=sumatoria+actividad.tiempoEjecucion
    promedio=sumatoria/len(list_act)
    return promedio

# b. costo total del proyecto;
def costoTotal(list_act):
    acumulador=0
    for actividad in list_act:
        acumulador=acumulador+actividad.costo
    return acumulador

# c. actividades realizadas por una determinada persona;
def actividadesPersona(list_act):
    encontrado=False
    persona=input("Ingrese a la persona por la que quiere saber sus actividades: ")
    for actividad in list_act:
        if actividad.Persona==persona:
            encontrado=True
            print(f"{actividad}")
            
    if not encontrado:
        print("No se encontro a la persona.")

# d. mostrar la información de las tareas a realizar entre dos fechas dadas;
def mostrarTareas(list_act):
    anio_desde = int(input("Ingrese el año desde donde: "))
    anio_hasta = int(input("Ingrese el año hasta donde: "))

    print(f"Tareas a realizar entre los años {anio_desde} y {anio_hasta}:")
    encontradas = False
    for actividad in list_act:
        if anio_desde <= actividad.FechaInicio <= anio_hasta:
            print(actividad)
            encontradas = True

    if not encontradas:
        print("No hay tareas en ese rango de años.")

# e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
def mostrarTareasFinalizadas(list_act):
    en_tiempo = False
    fuera_de_tiempo = False
    print("Tareas finalizadas en tiempo:")
    for actividad in list_act:
        if actividad.FechaFinEfectiva is not None:
            if actividad.FechaFinEfectiva <= actividad.FechaFinEstimada:
                print(f"{actividad}")
                en_tiempo = True

    if not en_tiempo:
        print("No hay tareas finalizadas en tiempo.")

    print("Tareas finalizadas fuera de tiempo:")
    for actividad in list_act:
        if actividad.FechaFinEfectiva is not None:
            if actividad.FechaFinEfectiva > actividad.FechaFinEstimada:
                print(f"{actividad}")
                fuera_de_tiempo = True

    if not fuera_de_tiempo:
        print(" No hay tareas finalizadas fuera de tiempo.")


# f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por
# el usuario.
def tareasPendientes(list_act):
    encontrado=False
    persona=input("Ingrese la persona por la cual quiere saber cuantas tareas pendientes tiene: ")
    contador=0
    for actividad in list_act:
        if (actividad.Persona == persona) and actividad.FechaFinEfectiva is None:
            encontrado=True
            contador += 1
    if encontrado:               
        print(f"{persona} tiene {contador} tarea(s) pendiente(s).")
    else:
        print("La persona no a sido encontrado/a o no tiene tareas pendientes.")
    


#CP
cargarLista(list_actividades,actividades)
# list_actividades.show()
promedioTotal=promedioTareas(list_actividades)
print(f"El promedio de las tareas es de: {promedioTotal}")
print()
costoProyecto=costoTotal(list_actividades)
print(f"El costo total del proyecto es de: {costoProyecto}$")
print()
actividadesPersona(list_actividades)
print()
mostrarTareas(list_actividades)
print()
mostrarTareasFinalizadas(list_actividades)
print()
tareasPendientes(list_actividades)