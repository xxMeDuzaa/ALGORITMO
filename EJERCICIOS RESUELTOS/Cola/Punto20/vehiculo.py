class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo
        self.tarifa = self.obtener_tarifa()
        
    def obtener_tarifa(self):
        tarifas = {
            "Automovil": 47,
            "Camioneta": 59,
            "Camion": 71,
            "Colectivo": 64
        }
        return tarifas[self.tipo]
    
    def __str__(self):
        return f"{self.tipo} (${self.tarifa})"