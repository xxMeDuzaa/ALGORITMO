# 9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
# Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
# la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
# algoritmo que permita realizar la siguientes actividades:
# a. mostrar los alumnos ordenados alfabéticamente por apellido;
# b. indicar los alumnos que no desaprobaron ningún parcial;
# c. determinar los alumnos que tienen promedio mayor a 8,89;
# d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
# e. mostrar el promedio de cada uno de los alumnos;
# f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
# g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
# h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
# i. mostrar todos los alumnos que rindieron en el año 2020;
# j. debe modificar el TDA para implementar lista de lista.

from list_ import List
from alumno_parcial import Alumno, Parcial, order_by_apellido

list_Alumnos = List()

alumnos = [
    Alumno("Lucia", "Gomez", 100),
    Alumno("Carlos", "Perez", 101),
    Alumno("Laura", "Lopez", 102),
    Alumno("Luis", "Lara", 103),
    Alumno("Ana", "Luna", 104),
    Alumno("Pedro", "Garcia", 105),
]

parciales = [
    Parcial("Algoritmos y estructuras de datos", 9, 2020, 100),
    Parcial("Ingeniería de software", 10, 2021, 100),
    Parcial("Base de datos", 8, 2022, 101),
    Parcial("Algoritmos y estructuras de datos", 10, 2020, 102),
    Parcial("Base de datos", 4, 2021, 102),
    Parcial("Ingeniería de software", 5, 2022, 103),
    Parcial("Base de datos", 7, 2020, 103),
    Parcial("Algoritmos y estructuras de datos", 5, 2021, 104),
    Parcial("Ingeniería de software", 9, 2022, 104),
    Parcial("Base de datos", 7, 2020, 105),
    Parcial("Algoritmos y estructuras de datos", 10, 2021, 105),
]


def ordenarCriterios(list_Alum):
    list_Alum.add_criterion("apellido", order_by_apellido)

#A
def ordenarApellidos(list_Alum):
    list_Alum.sort_by_criterion("apellido")
    
def cargarAlumnos(list_Alum, alumnos):
    for alumno in alumnos:
        list_Alum.append(alumno)
    
def cargarParciales(list_Alum, parciales):
    for parcial in parciales:
        for alumno in list_Alum:
            if alumno.legajo == parcial.legajo:
                alumno.parciales.append(parcial)

#B             
def alumnosNoDesaprobados(list_Alum): 
    print("Alumnos que no desaprobaron ningún parcial: ")
    for alumno in list_Alum:
        desaprobo = False
        for parcial in alumno.parciales:
            if parcial.nota < 6:
                desaprobo = True
                
        if desaprobo==False:
            print(f"{alumno.nombre}, {alumno.apellido}")
            
#C
def alumnosPromedioMayor(list_Alum):
    encontrado=False
    promedioTotal=0  
    for alumno in list_Alum:
        suma=0
        for parcial in alumno.parciales:
            suma = suma + parcial.nota
        promedioTotal=suma/len(alumno.parciales)
        if promedioTotal>=8.99:
            encontrado=True
            print(f"{alumno.nombre} {alumno.apellido}, tiene un promedio mayor a 8.99.")
    
    if encontrado==False:
        print("No se encontro ningun alumno con un promedio mayor a 8.99.")

#D
def mostrarInformacion(list_Alum):
    for alumno in list_Alum:
        if alumno.apellido[0]=="L":
            print(f"{alumno.nombre} {alumno.apellido}, {alumno.legajo}")
            print("Parciales: ")
            for parcial in alumno.parciales:
                print(f"{parcial}")
            print()

#E
def mostrarPromedio(list_Alum):
    promedio=0
    for alumno in list_Alum:
        suma=0
        for parcial in alumno.parciales:
            suma = suma + parcial.nota
        promedio=suma/len(alumno.parciales)
        print(f"{alumno.nombre} {alumno.apellido} con un promedio de: {promedio}")
        
#F
def mostrarAlumnosCatedra(list_Alum):
    for alumno in list_Alum:
        for parcial in alumno.parciales:
            if parcial.materia=="Algoritmos y estructuras de datos":
                print(f"{alumno.nombre} {alumno.apellido}")

#G
def porcentajeEspecífico(list_Alum):
    aprobado = 0
    encontrado = False
    alumnosEspecifico = input("Ingrese el nombre del alumno para ver su porcentaje de parciales aprobados: ")
    for alumno in list_Alum:
        if alumnosEspecifico == alumno.nombre:
            for parcial in alumno.parciales:
                if parcial.nota>=6:
                    aprobado+=1
            porcentaje = (aprobado / len(alumno.parciales)) * 100
            print(f"Porcentaje de parciales aprobados de {alumno.nombre} {alumno.apellido}: {porcentaje}%")
            encontrado = True

    if encontrado==False:
        print("Alumno no encontrado.")
        
#H
def catedraBDD(list_Alum):
    c_aprobados=0
    c_desaprobados=0
    for alumno in list_Alum: 
        for parcial in alumno.parciales:
            if parcial.materia=="Base de datos":
                if parcial.nota>=6:
                    c_aprobados+=1
                else:
                    c_desaprobados+=1

    return c_aprobados,c_desaprobados
            
#I
def alumnosParciales2020(list_Alum):
    for alumno in list_Alum: 
        for parcial in alumno.parciales:
            if parcial.fecha == 2020:
                print(f"{alumno.nombre} {alumno.apellido}")
                        

#CP
cargarAlumnos(list_Alumnos, alumnos)
cargarParciales(list_Alumnos, parciales)
ordenarCriterios(list_Alumnos)
ordenarApellidos(list_Alumnos)
print("Lista de alumnos ordenada por apellidos: ")
list_Alumnos.show_list_of_list()
print()
alumnosNoDesaprobados(list_Alumnos)
print()
print("Alumnos con un promedio mayor a 8.99: ")
alumnosPromedioMayor(list_Alumnos)
print()
print("Alumnos cuyos apellidos comienzan con L: ")
mostrarInformacion(list_Alumnos)
print()
print("Promedios de cada uno de los alumnos: ")
mostrarPromedio(list_Alumnos)
print()
print("Alumnos que rindieron la catedra Algoritmos y estructuras de datos: ")
mostrarAlumnosCatedra(list_Alumnos)
print()
porcentajeEspecífico(list_Alumnos)
print()
cant_aprobados,cant_desaprobados=catedraBDD(list_Alumnos)
print("Cantidad de alumnos aprobados y desaprobados: ")
print(f"Aprobados: {cant_aprobados}")
print(f"Desaprobados: {cant_desaprobados}")
print()
print("Alumnos que rindieron parciales en el 2020: ")
alumnosParciales2020(list_Alumnos)