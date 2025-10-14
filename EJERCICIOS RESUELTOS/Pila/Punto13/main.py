# 13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
# las siguientes actividades:

#a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
#demás mostrar el nombre de dichas películas;

#b. mostrar los modelos que quedaron dañados, sin perder información de la pila.

#c. eliminar los modelos de los trajes destruidos mostrando su nombre;

# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
# más de un modelo de traje, estos deben cargarse por separado;

#e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
#repetidos en una misma película;

#f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
#“Capitan America: Civil War”.

from stack import Stack
from trajeIronMan import TrajeIronMan

trajes_stack = Stack()

# Crear objetos
traje1 = TrajeIronMan("Mark I", "Iron Man (2008)", "Dañado")
traje2 = TrajeIronMan("Mark XLIV (Hulkbuster)", "Iron Man 2 (2010)", "Impecable")
traje3 = TrajeIronMan("Mark XLIV (Hulkbuster)", "Avengers Infinity War (2018)", "Destruido")
traje4 = TrajeIronMan("Spider Man X1000", "Spider-Man: Homecoming", "Dañado")
traje5 = TrajeIronMan("Capitan America F250", "Capitan America: Civil War", "Impecable")

trajes=[traje1, traje2, traje3, traje4, traje5]

def cargarPila (traje_stack,trajes):
    for traje in trajes:
        traje_stack.push(traje)

#a)
def verificarModelo(traje_stack):
    encontrado = False
    aux_stack = Stack()

    while traje_stack.size() > 0:
        elemento = traje_stack.pop()
        aux_stack.push(elemento)
        if elemento.modelo == "Mark XLIV (Hulkbuster)":
            print(f"El modelo {elemento.modelo} fue utilizado en la película: \033[95m{elemento.pelicula}\033[0m")
            encontrado = True
            
    if encontrado==False:
        print("El modelo Mark XLIV (Hulkbuster) no fue utilizado en ninguna película.")

    # Restauro la pila original
    while aux_stack.size() > 0:
        traje_stack.push(aux_stack.pop())

#b)      
def modelosDañados(traje_stack):
    encontrado = False
    aux_stack = Stack()

    while traje_stack.size() > 0:
        elemento = traje_stack.pop()
        aux_stack.push(elemento)
        if elemento.estado == "Dañado":
            print(f"\033[95m{elemento.modelo}\033[0m")
            encontrado = True
            
    if encontrado==False:
        print("Ninguno, no hay modelos que quedaron dañados.")

    # Restauro la pila original
    while aux_stack.size() > 0:
        traje_stack.push(aux_stack.pop())

#c)     
def eliminarModelosTrajes(traje_stack):
    encontrado = False
    aux_stack = Stack()

    while traje_stack.size() > 0:
        elemento = traje_stack.pop()
        if elemento.estado == "Destruido":
            print(f"\033[95m{elemento.modelo}\033[0m de la pelicula: \033[95m{elemento.pelicula}\033[0m")
            encontrado = True
        else:
            aux_stack.push(elemento) #solamente guardo aquellos modelos que no esten destruidos
            
    if encontrado==False:
        print("Ninguno, no hay modelos de traje destruidos: ")

    # Restauro la pila con modelos que no estan destruidos
    while aux_stack.size() > 0:
        traje_stack.push(aux_stack.pop())
        
#e)
def agregarModelo(traje_stack):
    aux_stack = Stack()
    modelo_duplicado=False
    
    while traje_stack.size() > 0:
        elemento = traje_stack.pop()
        aux_stack.push(elemento)
        # Verificar si ya existe el modelo y la película
        if elemento.modelo == "Mark LXXXV" and elemento.pelicula == "Avengers Endgame (2019)":
            modelo_duplicado=True
        
    
    # Si el modelo y la película no están en la pila, agregar el nuevo modelo
    if not modelo_duplicado:
        model = "Mark LXXXV"
        peli = "Avengers Endgame (2019)"
        est = "Impecable"
        nuevo_traje = TrajeIronMan(model, peli, est)
        aux_stack.push(nuevo_traje)
    
    # Restaurar la pila original
    while aux_stack.size() > 0:
        traje_stack.push(aux_stack.pop())

#f)
def mostrarModelosEspecificos(traje_stack):
    encontrado = False
    aux_stack = Stack()

    while traje_stack.size() > 0:
        elemento = traje_stack.pop()
        aux_stack.push(elemento)
        if elemento.pelicula == "Spider-Man: Homecoming" or elemento.pelicula == "Capitan America: Civil War":
            print(f"\033[95m{elemento.modelo}\033[0m")
            encontrado = True
            
    if encontrado==False:
        print("Ninguno, ya que no se encontro peliculas Spider-Man: Homecoming y Capitan America: Civil War.")

    # Restauro la pila original
    while aux_stack.size() > 0:
        traje_stack.push(aux_stack.pop())

    
#CUERPO PRINCIPAL 
cargarPila(trajes_stack,trajes)
# print("Trajes en la pila original:")
# trajes_stack.show()
print()
print("\033[92mModelos de Mark XLIV (Hulkbuster) que fueron utilizados en alguna de las películas:\033[0m")
verificarModelo(trajes_stack)
print()
print("\033[92mLos modelos que quedaron dañados fueron:\033[0m")
modelosDañados(trajes_stack)
print()
print("\033[92mLos modelos que quedaron destruidos fueron:\033[0m")
eliminarModelosTrajes(trajes_stack)
print()
print("\033[92mTrajes en la pila despues de excluir los modelos destruidos:\033[0m")
trajes_stack.show()
print()
agregarModelo(trajes_stack)
print()
print("\033[92mTrajes en la pila despues de agregar el nuevo modelo Mark LXXXV:\033[0m")
trajes_stack.show()
print()
print("\033[92mTrajes utilizados en las películas Spider-Man: Homecoming y Capitan America: Civil War\033[0m")
mostrarModelosEspecificos(trajes_stack)
print()
print("\033[96mTrabajo realizado por: \033[34mAxel Sandillú\033[0m")