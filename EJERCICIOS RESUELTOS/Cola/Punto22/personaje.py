class Personaje:
    def __init__(self, nombrePJ, nombreSH, genero):
        self.nombrePJ = nombrePJ
        self.nombreSH = nombreSH
        self.genero = genero

    def __str__(self):
        return f"Nombre del personaje: {self.nombrePJ}, Nombre del Superhéroe: {self.nombreSH}, Género: {self.genero}"