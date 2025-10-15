# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:

from list_ import List
from personaje_jedi import PersonajesJedi, order_by_nombre, order_by_especie

list_personajes = List()

jedis = [
    PersonajesJedi("Ahsoka Tano", ["Anakin Skywalker"], ["verde", "azul", "blanco"], "togruta"),
    PersonajesJedi("Kit Fisto", ["Yoda"], ["verde"], "nautolano"),
    PersonajesJedi("Anakin Skywalker", ["Obi-Wan Kenobi", "Qui-Gon Jin"], ["azul", "rojo"], "humano"),
    PersonajesJedi("Luke Skywalker", ["Obi-Wan Kenobi", "Yoda"], ["verde", "azul"], "humano"),
    PersonajesJedi("Yoda", ["N'Kata Del Gormo"], ["amarillo"], "desconocida"),
    PersonajesJedi("Mace Windu", ["Yoda"], ["violeta"], "humano"),
    PersonajesJedi("Obi-Wan Kenobi", ["Qui-Gon Jin"], ["azul"], "humano"),
    PersonajesJedi("Qui-Gon Jin", ["Conde Dooku"], ["verde"], "humano"),
    PersonajesJedi("Aayla Secura", ["Quinlan Vos"], ["azul"], "twi'lek"),
]

def cargarSuperheroes(list_perso, jedis):
    for jedi in jedis:
        list_perso.append(jedi)


def ordenarCriterios(list_peli):
    list_peli.add_criterion("nombre", order_by_nombre)
    list_peli.add_criterion("especie", order_by_especie)     
        
# a. listado ordenado por nombre y por especie;
def ordenarNombre(list_peli):
    list_peli.sort_by_criterion("nombre")
    
def ordenarEspecie(list_peli):
    list_peli.sort_by_criterion("especie")

def ordenarCriteriorSolicitados(list_peli):
    print("I. Ordenado por Especie: ")
    ordenarEspecie(list_peli)
    list_peli.show()
    print()
    
    print("II. Ordenado por nombre: ")
    ordenarNombre(list_peli)
    list_peli.show()
    print()


# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
def mostrarInfoPJ(list_peli):
    indice1 = list_peli.search("Ahsoka Tano", "nombre")
    indice2 = list_peli.search("Kit Fisto", "nombre")
    
    if indice1 is not None:
        print(list_peli[indice1])
    else:
        print("No se encontró a Ahsoka Tano.")
    
    if indice2 is not None:
        print(list_peli[indice2])
    else:
        print("No se encontró a Kit Fisto.")

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices; y # h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
def mostrarPadawan(list_peli,nombre1,nombre2):
    encontrado=False
    for pj in list_peli:
        if pj.nombre==nombre1 or pj.nombre==nombre2:
            encontrado=True
            print(f"{pj.nombre}-{pj.maestros}")
            
    if not encontrado:
        print("No se ha encontrado los Jedis, que de estos, quieres saber los padawan.")

# d. mostrar los Jedi de especie humana y twi'lek;
def mostrarJediEspecieHumana(list_perso):
    for pj in list_perso:
        if pj.especie=="humano" or pj.especie=="twi'lek":
            print(f"{pj.nombre}| {pj.especie}")
  
# e. listar todos los Jedi que comienzan con A;
def mostrarJedisA(list_perso):
    for pj in list_perso:
        if pj.nombre.startswith(("A")):
            print(f"{pj.nombre}")          
            
# f. mostrar los Jedi que usaron sable de luz de más de un color;
def mostrarJedisColor(list_perso):
    for pj in list_perso:
        if len(pj.coloresSableLuz)>1:
            print(f"{pj.nombre}: {pj.coloresSableLuz}")
            
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
def jedisSableLuzColores(list_perso):
    colores = ["amarillo", "violeta"]
    encontrado = False
    for pj in list_perso:
        for color in colores:
            if color in pj.coloresSableLuz:
                encontrado = True
                print(f"{pj.nombre}: {pj.coloresSableLuz}")

    if not encontrado:
        print("No se encontraron a Jedis que tengan colores de sable de luz amarillo o violeta.")





#CP
cargarSuperheroes(list_personajes, jedis)
# print("LISTA CARGADA DE PERSONAJES DE JEDI: ")
# list_personajes.show()
ordenarCriterios(list_personajes)
ordenarCriteriorSolicitados(list_personajes)
print()
print("Informacion de Ahsoka Tano y Kit Fisto (si es que estan): ")
mostrarInfoPJ(list_personajes)
print()
print("Maestros de Yoda y Luke Skywalker (si es que estan): ")
mostrarPadawan(list_personajes,"Yoda","Luke Skywalker")
print()
print("Jedis de especie humana y twi'lek: ")
mostrarJediEspecieHumana(list_personajes)
print()
print("Jedis que comienzan con A: ")
mostrarJedisA(list_personajes)  
print()
print("Personajes que usaron sable de luz de mas de un color: ")
mostrarJedisColor(list_personajes)
print()
print("Los Jedi que utilizaron sable de luz amarillo o violeta: ")
jedisSableLuzColores(list_personajes)
print()
print("Maestros de Qui-Gon Jin y Mace Windu (si es que estan): ")
mostrarPadawan(list_personajes,"Qui-Gon Jin","Mace Windu")