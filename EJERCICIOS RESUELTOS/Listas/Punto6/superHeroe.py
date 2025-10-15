class Superheroe:
    def __init__(self, nombre, año, casaComic, biografia):
        self.nombre = nombre
        self.año = año
        self.casaComic = casaComic
        self.biografia= biografia

    def __str__(self):
        return f"Nombre: {self.nombre}, Año aparición: {self.año}, Casa a la que pertenece: {self.casaComic}, Biografia {self.biografia}"

#FUNCIONES PARA ORDENAR POR ATRIBUTO
def order_by_nombre(heroe):
    return heroe.nombre

def order_by_año(heroe):
    return heroe.año

def order_by_casaComic(heroe):
    return heroe.casaComic

def order_by_biografia(heroe):
    return heroe.biografia