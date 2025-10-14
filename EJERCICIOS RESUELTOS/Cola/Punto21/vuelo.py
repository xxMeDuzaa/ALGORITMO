class Vuelo:
    def __init__(self, empresa, salida, llegada, origen_aeropuerto, destino_aeropuerto, tipo):
        self.empresa = empresa
        self.salida = salida      
        self.llegada = llegada 
        self.origen = origen_aeropuerto
        self.destino = destino_aeropuerto
        self.tipo = tipo

    def tiempo_pista(self, maniobra):
        """
        Retorna el tiempo (en segundos) que usa la pista según tipo y maniobra.
        maniobra puede ser "aterrizaje" o "despegue"
        """
        tiempos = {
            "pasajeros": {"aterrizaje": 10, "despegue": 5},
            "negocios": {"aterrizaje": 5, "despegue": 3},
            "carga": {"aterrizaje": 12, "despegue": 9}
        }
        return tiempos[self.tipo][maniobra]

    def get_hora_salida(self):
        """
        Retorna la hora de salida del vuelo, formateada para facilitar su comparación.
        """
        return self.salida

    def get_hora_llegada(self):
        """
        Retorna la hora de llegada del vuelo, formateada para facilitar su comparación.
        """
        return self.llegada

    def __str__(self):
        return (f"Empresa: {self.empresa}, Salida: {self.salida}, Llegada: {self.llegada}, "
                f"Origen: {self.origen}, Destino: {self.destino}, Tipo: {self.tipo}")