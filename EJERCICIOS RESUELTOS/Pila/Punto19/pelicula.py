class Pelicula:
    def __init__(self, titulo, estudio, año):
        self.titulo = titulo
        self.estudio = estudio
        self.año = año

    def __str__(self):
        return f"Titulo: {self.titulo}, Estudio Cinematografico: {self.estudio}, Año: {self.año}"