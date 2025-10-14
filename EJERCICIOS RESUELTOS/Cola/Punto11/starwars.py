class StarWars:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta 

    def __str__(self):
        return f"Nombre: {self.nombre}, Planeta: {self.planeta}"