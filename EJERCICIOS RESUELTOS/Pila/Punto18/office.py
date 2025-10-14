class Office:
    def __init__(self, nombre,peso):
        self.nombre = nombre
        self.peso = peso

    def __str__(self):
        return f"Nombre: {self.nombre}, Peso: {self.peso}Kg"