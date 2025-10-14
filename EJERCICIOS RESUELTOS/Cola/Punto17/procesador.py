class Procesador:
    def __init__(self, idProceso, tiempo):
        self.idProceso = idProceso
        self.tiempo = tiempo

    def __str__(self):
        return f"Id del proceso: {self.idProceso}, Tiempo de ejecución: {self.tiempo}"