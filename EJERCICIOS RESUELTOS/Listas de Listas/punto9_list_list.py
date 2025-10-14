#Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
#Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
#la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
#algoritmo que permita realizar la siguientes actividades:

class Alumno:
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo

    def __str__(self):
        return f""


#a. mostrar los alumnos ordenados alfabéticamente por apellido;
#b. indicar los alumnos que no desaprobaron ningún parcial;
#c. determinar los alumnos que tienen promedio mayor a 8,89;
#d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
#e. mostrar el promedio de cada uno de los alumnos;
#f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
#g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
#h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
#i. mostrar todos los alumnos que rindieron en el año 2020;
#j. debe modificar el TDA para implementar lista de lista.