# 21. Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recau-
# dación. Desarrolle los algoritmos necesarios para realizar las siguientes tareas:

from list_ import List
from pelicula import Pelicula, order_by_nombre, order_by_valoracion_publico, order_by_año_estreno, order_by_recaudacion

list_peliculas = List()

peliculas = [
    Pelicula("El Origen", 8.8, 2010, 830000000),
    Pelicula("Avatar", 7.9, 2009, 2847000000),
    Pelicula("Titanic", 7.8, 1997, 2195000000),
    Pelicula("Interstellar", 8.6, 2014, 677000000),
    Pelicula("Joker", 8.5, 2019, 1074000000),
    Pelicula("La La Land", 8.0, 2016, 446000000),
    Pelicula("Avengers: Endgame", 8.4, 2019, 2798000000),
    Pelicula("The Dark Knight", 9.0, 2008, 1005000000),
    Pelicula("Forrest Gump", 8.8, 1994, 678000000),
    Pelicula("The Shawshank Redemption", 9.3, 1994, 58000000),
    Pelicula("Gladiator", 8.5, 2000, 460000000),
    Pelicula("The Matrix", 8.7, 1999, 467000000),
]



def cargarPeliculas(list_peli, peliculas):
    for pelicula in peliculas:
        list_peli.append(pelicula)
    
# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determina-
# do año–;
def filtrarPeliculaAño(list_peli):
    encontrado=False
    año=int(input("Ingrese el año de las peliculas que quiere listar: "))
    print(f"Peliculas del año: {año}")
    for pelicula in list_peli:
        if pelicula.añoEstreno==año:
            encontrado=True
            print(f"{pelicula}")
    
    if not encontrado:
        print(f"No se encontro peliculas del año {año}.")
 
 
# b. mostrar los datos de la película que más recaudo;
def peliculaMayorRecaudacion(list_peli):
    max=0
    for pelicula in list_peli:
        if pelicula.recaudacion>max:
            max=pelicula.recaudacion
            peliculaMayor=pelicula
    
    print(f"La pelicula que mas recaudo es: {peliculaMayor}")       
     
# c. indicar las películas con mayor valoración del público, puede ser más de una;
def peliculaMayorValoracion(list_peli):
    max=0
    for pelicula in list_peli:
        if pelicula.valoracionPublico>max:
            max=pelicula.valoracionPublico
            peliculaMayor=pelicula
    
    print(f"La pelicula que mas valoracion tuvo es: {peliculaMayor}")   

# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
# lista auxiliar–:
def ordenarCriterios(list_peli):
    list_peli.add_criterion("apellido", order_by_nombre)
    list_peli.add_criterion("valoracionPublico", order_by_valoracion_publico)
    list_peli.add_criterion("añoEstreno", order_by_año_estreno)
    list_peli.add_criterion("recaudacion", order_by_recaudacion)
    
# I. por nombre,
def ordenarNombre(list_peli):
    list_peli.sort_by_criterion("apellido")
    
# II. por recaudación,
def ordenarRecaudacion(list_peli):
    list_peli.sort_by_criterion("recaudacion")

# III. por año de estreno,
def ordenarAñoEstreno(list_peli):
    list_peli.sort_by_criterion("añoEstreno")
    
# IV. por valoración del público.
def ordenarValoracionPublico(list_peli):
    list_peli.sort_by_criterion("valoracionPublico")
    
def ordenarCriteriorSolicitados(list_peli):
    print("I. Ordenado por nombre: ")
    ordenarNombre(list_peli)
    list_peli.show()
    print()

    print("II. Ordenado por recaudación: ")
    ordenarRecaudacion(list_peli)
    list_peli.show()
    print()
    
    print("III. Ordenado por año de estreno: ")
    ordenarAñoEstreno(list_peli)
    list_peli.show()
    print()
    
    print("IV. Ordenado por valoración del público: ")
    ordenarValoracionPublico(list_peli)
    list_peli.show()
    print()



   
#CP
cargarPeliculas(list_peliculas, peliculas)
# print("Lista peliculas: ")
# list_peliculas.show()
filtrarPeliculaAño(list_peliculas)
print()
peliculaMayorRecaudacion(list_peliculas)
print()
peliculaMayorValoracion(list_peliculas)
ordenarCriterios(list_peliculas)
print()
print("PELICULAS ORDENADAS POR CADA CRITERIO: ")
ordenarCriteriorSolicitados(list_peliculas)