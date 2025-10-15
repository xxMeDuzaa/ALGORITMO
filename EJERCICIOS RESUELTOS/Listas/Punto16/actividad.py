class Actividad:
    def __init__(self, costo, tiempoEjecucion, FechaInicio, FechaFinEstimada, FechaFinEfectiva, Persona):
        self.costo = costo
        self.tiempoEjecucion = tiempoEjecucion
        self.FechaInicio = FechaInicio
        self.FechaFinEstimada = FechaFinEstimada
        self.FechaFinEfectiva = FechaFinEfectiva
        self.Persona = Persona
        
    def __str__(self):
        return f"Costo: {self.costo}, T.ejecucion (SEG): {self.tiempoEjecucion}, F.inicio: {self.FechaInicio}, F.fin Estimada: {self.FechaFinEstimada}, F.fin Efectiva {self.FechaFinEfectiva}, Persona a cargo: {self.Persona} "