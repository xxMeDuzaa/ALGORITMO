class BasesRebeldes:
    def __init__(self, nombre, numeroFlota, latitud, longitud):
        self.nombre = nombre
        self.numeroFlota = numeroFlota
        self.latitud = latitud
        self.longitud= longitud
    def __str__(self):
        return f"Nombre: {self.nombre}, Némero de flota aérea: {self.numeroFlota}, Coordenadas: latidud {self.latitud}, longitud: {self.longitud}"