class Vuelo:
    def __init__(self, empresa, numeroVuelo, cantAsientos, fechaSalida, destino, KmVuelo, cantAsientosTotal, ocupadosPrimera, ocupadosTurista):
        self.empresa = empresa
        self.numeroVuelo = numeroVuelo
        self.cantAsientos = cantAsientos
        self.fechaSalida= fechaSalida
        self.destino = destino
        self.KmVuelo = KmVuelo
        self.cantAsientosTotal = cantAsientosTotal
        self.ocupadosPrimera = ocupadosPrimera
        self.ocupadosTurista = ocupadosTurista

    def __str__(self):
        return f"Empresa: {self.empresa}, N.Vuelo: {self.numeroVuelo}, C.Asientos: {self.cantAsientos}, F.salida: {self.fechaSalida}, destino: {self.destino}, Km del vuelo: {self.KmVuelo}, C. asientos Total: {self.cantAsientosTotal}, O.Primera: {self.ocupadosPrimera}, O.Turista: {self.ocupadosTurista}"

def order_by_numero(num):
    return num.numeroVuelo

vuelos = [
    Vuelo("Aegean Airlines", "AE123", 180, 2025, "Atenas", 320, 180, 20, 140),
    Vuelo("Sky Express", "SE456", 160, 2025, "Miconos", 270, 100, 15, 130),
    Vuelo("Olympic Air", "OA789", 150, 2025, "Rodas", 410, 150, 10, 120),
    Vuelo("Thai Airways", "TG999", 300, 2025, "Tailandia", 8000, 300, 40, 200),
    Vuelo("Crete Air", "CA111", 100, 2024, "Atenas", 320, 100, 10, 90),
    Vuelo("Island Hoppers", "IH333", 130, 2024, "Santorini", 200, 130, 5, 124),
    Vuelo("Thai Smile", "TS222", 220, 2023, "Tailandia", 8200, 220, 50, 150)
]