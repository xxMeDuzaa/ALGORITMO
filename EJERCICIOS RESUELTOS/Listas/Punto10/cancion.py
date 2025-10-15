class Cancion:
    def __init__(self, nombre, banda_artista, duracion, cantReproducciones):
        self.nombre = nombre
        self.banda_artista = banda_artista
        self.duracion = duracion
        self.cantReproducciones= cantReproducciones

    def __str__(self):
        return f"Nombre: {self.nombre}, Banda o Artista: {self.banda_artista}, Duracion (en segundos): {self.duracion}, Cantidad de reproducciones: {self.cantReproducciones}"

#FUNCIONES PARA ORDENAR POR ATRIBUTO
def order_by_nombre(song):
    return song.nombre

def order_by_banda_artista(song):
    return song.banda_artista

def order_by_duracion(song):
    return song.duracion

def order_by_cantReproducciones(song):
    return song.cantReproducciones