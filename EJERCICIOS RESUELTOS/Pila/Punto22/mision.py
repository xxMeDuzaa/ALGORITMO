class Mision:
    def __init__(self, planeta, captura, costo):
        self.planeta = planeta
        self.captura = captura
        self.costo = costo

    def __str__(self):
        return f"Planeta visitado: {self.planeta}, A quien capturo: {self.captura}, Costo de recompensa: {self.costo}"