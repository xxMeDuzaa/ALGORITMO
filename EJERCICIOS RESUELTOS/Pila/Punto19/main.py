# 19. Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
# treno, desarrollar las funciones necesarias para resolver las siguientes actividades:

# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

from pelicula import Pelicula
from stack import Stack

peliculas_stack=Stack()

peli1 = Pelicula("Spiderman X", "Marvel Studios", 2014)
peli2 = Pelicula("Avengers: Infinity War", "Marvel Studios", 2018)
peli3 = Pelicula("Doctor Strange", "Marvel Studios", 2016)
peli4 = Pelicula("Interstellar", "Paramount Pictures", 2014)
                      
peliculas=[peli1,peli2,peli3,peli4]

def cargarPila(peli_stack,peliculas):
    for peli in peliculas:
        peli_stack.push(peli)
        
        
def estreno2014(peli_stack):
    aux_stack=Stack() #auxiliar para restaurar la pila original
    encontrado=False
    while peli_stack.size()>0:
        peli=peli_stack.pop()
        aux_stack.push(peli)
        if peli.año==2014:
            encontrado=True
            print(f"{peli.titulo}")
    
    if encontrado==False:
        print("Ninguna, no se encontraron peliculas estrenadas en el año 2014. ")
        
    while aux_stack.size()>0: #restauro la pila original
        peli_stack.push(aux_stack.pop())
  

def estreno2018(peli_stack):
    aux_stack=Stack() #auxiliar para restaurar la pila original
    c_peliculas=0
    while peli_stack.size()>0:
        peli=peli_stack.pop()
        aux_stack.push(peli)
        if peli.año==2018:
            c_peliculas+=1
        
    while aux_stack.size()>0: #restauro la pila original
        peli_stack.push(aux_stack.pop())  
    
    return c_peliculas        

def peliculasMostrar(peli_stack):
    aux_stack=Stack() #auxiliar para restaurar la pila original
    encontrado=False
    while peli_stack.size()>0:
        peli=peli_stack.pop()
        aux_stack.push(peli)
        if peli.estudio=="Marvel Studios" and peli.año==2016:
            encontrado=True
            print(f"{peli.titulo}")
    
    if encontrado==False:
        print("Ninguna, no se encontraron peliculas estrenadas en el año 2016 de Marvel Studios.")
        
    while aux_stack.size()>0: #restauro la pila original
        peli_stack.push(aux_stack.pop())
  
    
#CUERPO PRINCIPAL
cargarPila(peliculas_stack,peliculas)
print("Pila con peliculas cargadas: ")
peliculas_stack.show()
print()
print("Estrenos de peliculas en el año 2014: ")
estreno2014(peliculas_stack)
print()
contador_peliculas=estreno2018(peliculas_stack)
print(f"La cantidad de peliculas que se estrenaron en el 2018 fueron: {contador_peliculas}")
print()
print("Estrenos de peliculas en el año 2016 de Marvel Studios: ")
peliculasMostrar(peliculas_stack)