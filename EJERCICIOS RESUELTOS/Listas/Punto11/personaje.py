class Personaje:
    def __init__(self, nombre, altura, edad, genero, especie, planetaNatal, episodios):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero= genero
        self.especie = especie
        self.planetaNatal = planetaNatal
        self.episodios = episodios

    def __str__(self):
        return f"Nombre: {self.nombre}, Altura (CM): {self.altura}, Edad: {self.edad}, Genero: {self.genero}, Especie: {self.especie}, Planeta Natal: {self.planetaNatal}, Episodios {self.episodios}"

#FUNCIONES PARA ORDENAR POR ATRIBUTO
def order_by_nombre(pj):
    return pj.nombre

def order_by_altura(pj):
    return pj.altura

def order_by_edad(pj):
    return pj.edad

def order_by_genero(pj):
    return pj.genero