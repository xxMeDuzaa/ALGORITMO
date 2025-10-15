from list_ import List
from datetime import datetime

class EstacionMeteorologica:
    def __init__(self, pais, ubicacion, c_latitud,c_longitud,c_altitud):
        self.pais = pais
        self.ubicacion = ubicacion
        self.c_latitud = c_latitud
        self.c_longitud = c_longitud
        self.c_altitud = c_altitud
        self.registro = List()
        
    def __str__(self):
        return f"{self.pais}, {self.ubicacion}, {self.c_latitud}, {self.c_longitud}, {self.c_altitud}"

class Medicion:
    def __init__(self, temperatura, presion, humedad, estado, ubicacion, fecha_hora):
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
        self.estado = estado
        self.ubicacion = ubicacion
        self.fecha_hora = fecha_hora  # tipo datetime
    
    def __str__(self):
        return (f"{self.fecha_hora.strftime('%Y-%m-%d %H:%M')} | "
                f"Temp: {self.temperatura}°C, Presión: {self.presion} hPa, "
                f"Humedad: {self.humedad}%, Estado: {self.estado}, Ubicación: {self.ubicacion}")