from list_ import List

class Alumno:
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.parciales = List()
        
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.legajo}"
        
class Parcial:
    
    def __init__(self, materia, nota, fecha, legajo):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha
        self.legajo = legajo #atributo compartido para saber que parcial le corresponde a cada alumno
    
    def __str__(self):
        return f"Materia: {self.materia}, Nota: {self.nota}, Fecha: {self.fecha}"
    

#FUNCIONES PARA ORDENAR POR ATRIBUTO
def order_by_apellido(alumno):
    return alumno.apellido.lower()