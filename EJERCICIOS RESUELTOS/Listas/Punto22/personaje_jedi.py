class PersonajesJedi:
    def __init__(self, nombre, maestros, coloresSableLuz, especie):
        self.nombre = nombre
        self.maestros = maestros
        self.coloresSableLuz = coloresSableLuz
        self.especie= especie

    def __str__(self):
        return f"Nombre: {self.nombre}, Maestros: {self.maestros}, Colores de sable usados: {self.coloresSableLuz}, Especie: {self.especie}"
    
def order_by_nombre(pj):
    return pj.nombre

def order_by_especie(pj):
    return pj.especie