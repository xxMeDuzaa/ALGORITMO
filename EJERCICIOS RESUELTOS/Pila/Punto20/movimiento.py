class Movimiento:
    def __init__(self, pasos, direccion):
        self.pasos = pasos
        self.direccion = direccion

    def __str__(self):
        return f"{self.pasos} pasos hacia {self.direccion}"