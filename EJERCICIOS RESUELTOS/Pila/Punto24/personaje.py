class Personaje:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad de películas de la saga en la que participó: {self.cantidad}"