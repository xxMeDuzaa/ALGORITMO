# 11. Dada una lista que contiene información de los personajes de la saga de Star Wars con la si-
# guiente información nombre, altura, edad, género, especie, planeta natal y episodios en los que

# apareció, desarrollar los algoritmos que permitan realizar las siguientes actividades:
# a. listar todos los personajes de género femenino;
# b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episo-
# dios de la saga;
# c. mostrar toda la información de Darth Vader y Han Solo;
# d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
# e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
# f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
# g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
# h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
# i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.

from list_ import List
from personaje import Personaje, order_by_nombre

list_personajes = List()

personajes = [
    Personaje("Leia Organa", 150, 19, "Femenino", "Humano", "Alderaan", ["IV", "V", "VI", "VII"]),
    Personaje("Luke Skywalker", 172, 19, "Masculino", "Humano", "Tatooine", ["IV", "V", "VI", "VII", "VIII"]),
    Personaje("R2-D2", 96, 66, "Ninguno", "Droide", "Naboo", ["I", "II", "III", "IV", "V", "VI", "VII"]),
    Personaje("C-3PO", 167, 112, "Ninguno", "Droide", "Tatooine", ["I", "II", "III", "IV", "V", "VI"]),
    Personaje("Darth Vader", 202, 45, "Masculino", "Humano", "Tatooine", ["III", "IV", "V", "VI"]),
    Personaje("Han Solo", 180, 32, "Masculino", "Humano", "Corellia", ["IV", "V", "VI", "VII"]),
    Personaje("Yoda", 66, 900, "Masculino", "Desconocida", "Desconocido", ["I", "II", "III", "V", "VI"]),
    Personaje("Chewbacca", 228, 965, "Masculino", "Wookiee", "Kashyyyk", ["III", "IV", "V", "VI", "VII"]),
    Personaje("Padmé Amidala", 165, 27, "Femenino", "Humano", "Naboo", ["I", "II", "III"]),
    Personaje("Rey", 170, 19, "Femenino", "Humasno", "Jakku", ["VII", "VIII", "IX"]),
    Personaje("Obi-Wan Kenobi", 182, 855, "Masculino", "Humano", "Stewjon", ["I", "II", "III", "IV"]),
    Personaje("Bail Organa", 180, 977, "Masculino", "Humano", "Alderaan", ["II", "III"]),
    Personaje("Jar Jar Binks", 190, 500, "Masculino", "Desconocido", "Tatooine", ["IV", "V", "VI"])
]


def cargar_personajes(list_pj, personajes):
    for pj in personajes:
        list_pj.append(pj)

def ordenarCriterios(list_pj):
    list_pj.add_criterion("nombre", order_by_nombre)
    
def ordenarNombre(list_pj):
    list_pj.sort_by_criterion("nombre")

#A
def mostrarPjFemenino(list_pj):
    for pj in list_pj:
        if pj.genero=="Femenino":
            print(f"{pj.nombre}")


#B
def mostrarPjDroide(list_pj):
    for pj in list_pj:
        if pj.especie == "Droide":
            for ep in pj.episodios:
                if ep in ["I", "II", "III", "IV", "V", "VI"]:
                    print(pj.nombre)
                    break  # si aparece una vez, no hace falta seguir ciclando

#C
def mostrarInfo(list_pj):
    indice1 = list_pj.search("Darth Vader", "nombre")
    indice2 = list_pj.search("Han Solo", "nombre")

    if indice1 and indice2:
        pj1 = list_pj[indice1]
        pj2 = list_pj[indice2]

        print("Información de Darth Vader:")
        print(f"{pj1}")

        print("Información de Han Solo:")
        print(f"{pj2}")
    else:
        print("No se encontraron los personajes Darth Vader o Han Solo.")

#D
def mostrarPjEpisodios(list_pj):
    episodios_necesarios = ["IV", "V", "VI", "VII"]
    for pj in list_pj:
        cumple_todos = True  # Suponemos que sí cumple
        for ep in episodios_necesarios:
            if ep not in pj.episodios:
                cumple_todos = False  # Si falta uno, no cumple
                break  # Ya no hace falta seguir revisando
        if cumple_todos:
            print(pj.nombre)
            
#E
def mostrarPjEdad(list_pj):
    edadMayor=0
    nombreMayor = ""
    for pj in list_pj:
        if pj.edad > 850:
            print(f"Nombre: {pj.nombre}, Edad: {pj.edad}")
            if pj.edad > edadMayor:
                nombreMayor = pj.nombre
                edadMayor = pj.edad
    if edadMayor > 0:
        print(f"El personaje que es el mayor de todos superando los 850 años es {nombreMayor} con una edad de {edadMayor}")
    else:
        print("No hay personajes que superen los 850 años.")

#F
def eliminarPj(list_pj):
    for pj in list_pj:
        # Verificamos que tenga solo esos tres episodios y no más
        if len(pj.episodios) == 3:
            if "IV" in pj.episodios and "V" in pj.episodios and "VI" in pj.episodios:
                list_pj.delete_value(pj.nombre, "nombre")
                
#G
def mostrarPjPlaneta(list_pj):
    for pj in list_pj:
        if pj.especie=="Humano" and pj.planetaNatal=="Alderaan":
            print(f"{pj.nombre}")

#H
def mostrarPjAltura(list_pj):
    for pj in list_pj:
        if pj.altura<70:
            print(f"{pj}")
            
# i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.
def episodiosPjEspecifico(list_pj):
    indice = list_pj.search("Chewbacca", "nombre")
    if indice:
        pj=list_pj[indice]
        print("Episodios en donde aparece Chewbacca: ")
        print(list_pj[indice].episodios)
        print("Toda su información: ")
        print(f"{pj}")
           
#CP
cargar_personajes(list_personajes,personajes)
ordenarCriterios(list_personajes)
ordenarNombre(list_personajes)
# print("Lista cargada de personajes: ")
# list_personajes.show()
print()
print("Personajes de genero femenino: ")
mostrarPjFemenino(list_personajes)
print()
print("Personajes de especie Droide que aparecieron en los primeros seis episodios de la saga:")
mostrarPjDroide(list_personajes)
print()
print("Información de personajes solicitados: ")
mostrarInfo(list_personajes)
print()
print("Personajes que aparecen en el episodio VII y en los tres anteriores: ")
mostrarPjEpisodios(list_personajes)
print()
print("Personajes con edad mayor a 850 años y de ellos el mayor: ")
mostrarPjEdad(list_personajes)
print()
eliminarPj(list_personajes)
print("Personajes de especie humana cuyo planeta de origen es Alderaan: ")
mostrarPjPlaneta(list_personajes)
print()
print("Personajes cuya altura es menor a 70 centímetros: ")
mostrarPjAltura(list_personajes)
print()
episodiosPjEspecifico(list_personajes)