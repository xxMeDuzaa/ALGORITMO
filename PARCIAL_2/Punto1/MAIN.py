#Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) 
# de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene 
# mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles 
# para acceder de manera eficiente a los datos contemplando lo siguiente:

from tree import BinaryTree
from lista_pokemons import pokemons


# A-los índices de cada uno de los árboles deben ser nombre, número y tipo;
arbol_nombre = BinaryTree()

arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

def cargar_pokemons(arbol_nom, arbol_num, arbol_tip, pokemons):
    for pokemon in pokemons:
        arbol_nom.insert(pokemon.nombre, pokemon)
        # por número
        arbol_num.insert(pokemon.numero, pokemon)
        # por tipo (si tiene 2 tipos lo insertamos en ambos)
        for tipo in pokemon.tipos:
            arbol_tip.insert(tipo, pokemon)
            
# B-mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad,
# es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;   
def buscar_pokemon_numero(arbol, numero):
    nodo = arbol.search(numero)
    if nodo:
        print(f"Se encontro el pokemon {numero}, sus datos: ")
        print(nodo.other_values)
    else:
        print(f"No se encontro el numero {numero} de pokemon.")

def buscar_pokemon_nombre(arbol, nombre_parcial):
    print(f"Pokémons que contienen '{nombre_parcial}':")
    arbol.proximity_search(nombre_parcial)
# C-mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
def mostrar_por_tipo(arbol, tipo):
    def __buscar(root):
        if root is not None:
            __buscar(root.left)
            if root.value == tipo:
                print(root.other_values.nombre)
            __buscar(root.right)
            
    if arbol.root is not None:
        __buscar(arbol_tipo.root)
        
# E-mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
def pokemones_debiles(arbol):
    def inOrder(node):
        if node is not None:
            inOrder(node.left)
            
            for debilidad in node.other_values.debilidades:
                if debilidad in ["Jolteon", "Lycanroc", "Tyrantrum"]:
                    print(f"- {node.other_values}")
                    break #necesito si o si usar el break porque sino no lo corta
            inOrder(node.right)

    if arbol.root is not None:
        inOrder(arbol.root)

# F-mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
def contar_tipos_pokemon(arbol):
    conteo_tipos = {}
    
    # Recorremos el árbol para llenar el diccionario con los conteos
    def in_orden(node):
        if node is not None:
            in_orden(node.left)
            
            tipo = node.value
            if tipo in conteo_tipos:
                conteo_tipos[tipo] += 1
            else:
                conteo_tipos[tipo] = 1
                
            in_orden(node.right)
            
    if arbol.root is not None:
        in_orden(arbol.root)

    # Ahora mostramos los resultados del diccionario
    print("Conteo de Pokémons por tipo:")
    
    for tipo in conteo_tipos:
        cantidad = conteo_tipos[tipo]
        print(f"- Tipo {tipo}: {cantidad}")

# G-determinar cuantos Pokémons tienen megaevolucion.
def contar_megaevolucion(arbol):
    contador = 0

    def inOrder(node):
        nonlocal contador
        if node is not None:
            inOrder(node.left)
            if node.other_values.mega_evolucion:
                contador += 1
            inOrder(node.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    print(f"Cantidad de Pokémons con megaevolución: {contador}")

# H-determinar cuantos Pokémons tiene forma gigamax.
def contar_gigamax(arbol):
    contador = 0

    def inOrder(node):
        nonlocal contador
        if node is not None:
            inOrder(node.left)
            if node.other_values.forma_gigamax:
                contador += 1
            inOrder(node.right)

    if arbol.root is not None:
        inOrder(arbol.root)

    print(f"Cantidad de Pokémons con forma Gigamax: {contador}")




#MAIN:
cargar_pokemons(arbol_nombre, arbol_numero, arbol_tipo, pokemons)
print()
# D-realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print("---------Arbol en orden de nombre: ")
arbol_nombre.in_order()
print()

print("---------Arbol en orden de numero: ")
arbol_numero.in_order()
print()

print("--------Arbol por nivel de Nombre: ")
arbol_tipo.by_level()
print()

num=int(input("Busqueda de pokemon por numero: "))
buscar_pokemon_numero(arbol_numero, num)
print()

nom=str(input("Ingrese un nombre a buscar (por proximidad): "))
buscar_pokemon_nombre(arbol_nombre, nom)
print("--------Pokemones por tipo------------: ")
print("---Tipo acero: ")
mostrar_por_tipo(arbol_tipo, "Acero")
print("---Tipo fantasma: ")
mostrar_por_tipo(arbol_tipo, "Fantasma") 
print("---Tipo electrico: ")
mostrar_por_tipo(arbol_tipo, "Eléctrico")
print("---Tipo fuego: ")
mostrar_por_tipo(arbol_tipo, "Fuego")
input()


print("----Todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum: ---------")
pokemones_debiles(arbol_nombre)
input()

contar_tipos_pokemon(arbol_tipo)
input()

contar_megaevolucion(arbol_nombre)
print()

contar_gigamax(arbol_nombre)
print()