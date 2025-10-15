class Pelicula:
    def __init__(self, nombre, valoracionPublico, añoEstreno, recaudacion):
        self.nombre = nombre
        self.valoracionPublico = valoracionPublico
        self.añoEstreno = añoEstreno
        self.recaudacion = recaudacion
        
    def __str__(self):
        return f"{self.nombre}, {self.valoracionPublico}, {self.añoEstreno}, {self.recaudacion}"

#FUNCIONES PARA ORDENAR POR ATRIBUTO
def order_by_nombre(peli):
    return peli.nombre

def order_by_valoracion_publico(peli):
    return peli.valoracionPublico

def order_by_año_estreno(peli):
    return peli.añoEstreno

def order_by_recaudacion(peli):
    return peli.recaudacion