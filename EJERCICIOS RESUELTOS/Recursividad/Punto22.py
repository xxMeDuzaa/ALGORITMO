# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

# c. Utilizar un vector para representar la mochila.

def usarLaFuerza(mochi, indice=0):
    if indice >= len(mochi):
        return indice, False

    if mochi[indice] == "sable de luz":
        return indice, True

    return usarLaFuerza(mochi, indice + 1)


mochila = ["rifles", "comida", "sable de luz", "botella", "libro"]
objetosSacados, encontrado = usarLaFuerza(mochila) #esto es para guardar segun lo que salga del return.

if encontrado==True:
    print(f"Se encontró el sable de luz sacando {objetosSacados} objetos")
else:
 print("No se encontro el sable de luz")