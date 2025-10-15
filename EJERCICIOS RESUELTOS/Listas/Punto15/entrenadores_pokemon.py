from list_ import List

class Entrenador:
    def __init__(self, nombre, TGanados, BPerdidas, BGanadas):
        self.nombre = nombre
        self.TGanados = TGanados
        self.BPerdidas = BPerdidas
        self.Bganadas = BGanadas
        self.pokemones= List()
        
    def __str__(self):
        return f"{self.nombre}, T.ganados: {self.TGanados}, B.perdidas: {self.BPerdidas}, B.ganadas: {self.Bganadas}"
        
class Pokemon:
    
    def __init__(self, nombre, nivel, tipo, subtipo, nombreEntrenador):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
        self.nombreEntrenador = nombreEntrenador 
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Nivel: {self.nivel}, Tipo: {self.tipo}, SubTipo: {self.subtipo}, Entrenador: {self.nombreEntrenador}"
    
def order_by_nombre(entrenador):
    return entrenador.nombre