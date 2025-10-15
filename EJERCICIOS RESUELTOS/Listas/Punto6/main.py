# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,

# casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
# rias para poder realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from list_ import List
from superHeroe import Superheroe, order_by_nombre

list_superheroes = List()

super_heroe = [
    Superheroe("Linterna Verde", 1940, "DC", "Usa un anillo de poder y un traje especial."),
    Superheroe("Wolverine", 1974, "Marvel", "Mutante con garras de adamantium y factor curativo."),
    Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con armadura y lazo de la verdad."),
    Superheroe("Capitana Marvel", 1968, "Marvel", "Poderosa heroína con traje especial."),
    Superheroe("Spider-Man", 1962, "Marvel", "Joven héroe con traje arácnido."),
    Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo, usa una capa y un traje místico."),
    Superheroe("Flash", 1940, "DC", "Velocista escarlata con traje rojo."),
    Superheroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia, usa una armadura espacial."),
    Superheroe("Batman", 1939, "DC", "Vigilante de Gotham con traje y gadgets."),
]

def cargarSuperheroes(list_SH, super_heroe):
    for Sh in super_heroe:
        list_SH.append(Sh)
        
def ordenarCriterios(list_SH):
    list_SH.add_criterion("nombre", order_by_nombre)
    
def ordenarNombres(list_SH):
    list_SH.sort_by_criterion("nombre")
    
def eliminarNodo(list_SH):
    list_SH.delete_value("Linterna Verde", key_value="nombre")
    
def buscarAñoAparicion(list_SH):
    indice=list_SH.search("Wolverine","nombre")
    if indice:
        añoAparicion=list_superheroes[indice].año
        print(f"El año de aparicion de Wolwerine es: {añoAparicion}")
    else:
        print("Wolverine no a sido encontrado.")
        
def cambiarCasa(list_SH):
    indice=list_SH.search("Dr. Strange", "nombre")
    if indice:
        list_SH[indice].casaComic="Marvel"
    else:
        print("No se encontro a el superheroe Dr. Strange.")
    

def mostrarNombre(list_SH):
    for heroe in list_SH: #ACA SI ES NECESARIO HACER UN RECORRIDO ENTRE SUPERHEROES
        biografia = heroe.biografia
        if ("traje" in biografia) or ("armadura" in biografia):
            print(heroe.nombre)
        
def mostrarNombreCasa(list_SH):
    for heroe in list_SH: #ACA SI ES NECESARIO HACER UN RECORRIDO ENTRE SUPERHEROES
        if heroe.año<1963:
            print(f"{heroe.nombre}, {heroe.casaComic}")

def mostrarCasa(list_SH):
    indice1=list_SH.search("Capitana Marvel", "nombre")
    indice2=list_SH.search("Mujer Maravilla", "nombre")
    
    if indice1 or indice2:
        print(f"{list_SH[indice1].nombre}: {list_SH[indice1].casaComic}")
        print(f"{list_SH[indice2].nombre}: {list_SH[indice2].casaComic}")
    else:
        print("No se encontraron las Superheroes Capitana Marvel o Mujer Maravilla.")
            
        
def mostrarInformacion(list_SH):
    indice1=list_SH.search("Flash", "nombre")
    indice2=list_SH.search("Star-Lord", "nombre")
    
    if indice1 or indice2:
        print(f"{list_SH[indice1].nombre}, {list_SH[indice1].año}, {list_SH[indice1].casaComic}, {list_SH[indice1].biografia}")
        print(f"{list_SH[indice2].nombre}, {list_SH[indice2].año}, {list_SH[indice2].casaComic}, {list_SH[indice2].biografia}")
    else:
        print("No se encontraron los personajes Flash y Star-Lord. ")
            
        
def listarSuperheroes(list_SH):
    for heroe in list_SH: 
        if heroe.nombre.startswith(("B","M","S")):
            print(f"{heroe.nombre}")
        
def contadorSuperheroesCasas(list_SH):
    conteo = {}  # Diccionario para guardar casa: cantidad
    for heroe in list_SH:
        casa = heroe.casaComic
        if casa in conteo:
            conteo[casa] += 1  # Si ya está la casa, sumo 1
        else:
            conteo[casa] = 1   # Si no está, la creo y pongo 1
    
    for casa in conteo:
        print("Casa:", casa, ", Cantidad de héroes:", conteo[casa])

    
# CUERPO PRINCIPAL
cargarSuperheroes(list_superheroes, super_heroe)
ordenarCriterios(list_superheroes)
print("Lista cargada de SuperHeroes:")
list_superheroes.show()
print()
ordenarNombres(list_superheroes)
eliminarNodo(list_superheroes)
print("La lista sin el nodo que contenga información de Linterna Verde:")
list_superheroes.show()
print()
buscarAñoAparicion(list_superheroes)
print()
cambiarCasa(list_superheroes)
print("Lista despues de cambiarle la casa a Dr. Strange (si es que esta): ")
list_superheroes.show()
print()
print("Nombres de superheroes donde en su bibliografia menciona la palabra (traje o armadura): ")
mostrarNombre(list_superheroes)
print()
print("Nombre y casa de los superhéroes cuya fecha de aparición es anterior a 1963: ")
mostrarNombreCasa(list_superheroes)
print()
print("Casas de las superheroes Capitana Marvel y Mujer Maravilla (si es que estan): ")
mostrarCasa(list_superheroes)
print()
print("Toda la informacion de los Superheroes Flash y Star-Lord (si es que estan): ")
mostrarInformacion(list_superheroes)
print()
print("Nombre de superheroes que comienzan con las letras (B, M y S): ")
listarSuperheroes(list_superheroes)
print()
print("Determino cuántos superhéroes hay de cada casa de comic: ")
contadorSuperheroesCasas(list_superheroes)