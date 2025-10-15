# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

from list_ import List
from entrenadores_pokemon import Entrenador, Pokemon, order_by_nombre

list_entrenadores = List()

entrenadores = [
    Entrenador("Lucia", 5, 10, 30),
    Entrenador("Carlos", 3, 7, 25),
    Entrenador("Laura", 4, 5, 20),
    Entrenador("Luis", 2, 12, 15),
    Entrenador("Ana", 6, 8, 40),
    Entrenador("Pedro", 1, 6, 10),
]

pokemons = [
    Pokemon("Pikachu", 50, "Eléctrico", "Ninguno", "Lucia"),
    Pokemon("Blastoise", 80, "Fuego", "Volador", "Lucia"),
    Pokemon("Squirtle", 35, "Agua", "Ninguno", "Carlos"),
    Pokemon("Bulbasaur", 40, "Planta", "Veneno", "Laura"),
    Pokemon("Bulbasaur", 70, "Fantasma", "Veneno", "Laura"),
    Pokemon("Machamp", 65, "Lucha", "Ninguno", "Luis"),
    Pokemon("Tyrantrum", 25, "Normal", "Hada", "Ana"),
    Pokemon("Eevee", 30, "Normal", "Ninguno", "Ana"),
    Pokemon("Pikachu", 55, "Roca", "Tierra", "Pedro"),
    Pokemon("Dragonite", 90, "Dragón", "Volador", "Pedro"),
]

def cargarEntrenador(list_coach, entrenadores):
    for coach in entrenadores:
        list_coach.append(coach)
    
def cargarPokemon(list_coach, pokemons):
    for pokemon in pokemons:
        for coach in list_coach:
            if coach.nombre == pokemon.nombreEntrenador:
                coach.pokemones.append(pokemon)
                
def ordenarCriterios(list_coach):
    list_coach.add_criterion("nombre", order_by_nombre)

def ordenarNombres(list_coach):
    list_coach.sort_by_criterion("nombre")
                
  
#A. obtener la cantidad de Pokémons de un determinado entrenador;
def cantidadPokemons(list_coach):
    c_contador=0
    for coach in list_coach:
        for pokemon in coach.pokemones:
            if coach.nombre=="Luis": #elijo a Luis por ejemplo
                c_contador+=1
    return c_contador

#B. listar los entrenadores que hayan ganado más de tres torneos;       
def mostrarCoachTorneos(list_coach):
    print("Entrenadores que hayan ganado mas de tres torneos: ")
    for coach in list_coach:
        if coach.TGanados>3:
            print(f"{coach.nombre}")

#C. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def PokemonCoachMayor(list_coach):
    max_nivel=0
    max_torneos=0
    for coach in list_coach:
        if coach.TGanados>max_torneos:
            max_torneos=coach.TGanados
            nombreMayor=coach #Guardo el objeto entrenador, no el nombre.
            
    for pokemons in nombreMayor.pokemones:
        if pokemons.nivel>max_nivel:
            max_nivel=pokemons.nivel
            pokemonMayor=pokemons.nombre
                           
    print("El Pokemon de mayor nivel del entrenador con mayor cantidad de torneos ganados: ")
    print(f"Entrenador {nombreMayor.nombre}, Pokemon: {pokemonMayor}")

#D. mostrar todos los datos de un entrenador y sus Pokémons;      
def mostrarDatosEntrenador(list_coach):
    
    for coach in list_coach:
        if coach.nombre=="Pedro": #elijo a pedro por ejemplo
            print(f"T.ganados: {coach.TGanados}, B.perdidas: {coach.BPerdidas}, B.ganadas: {coach.Bganadas}")
            for pokemons in coach.pokemones:
                print("Pokemones: ")
                print(f"Nombre: {pokemons.nombre}, Nivel: {pokemons.nivel}, Tipo: {pokemons.tipo}, SubTipo: {pokemons.subtipo}")

#E. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def entrenadoresPorcentaje79(list_coach):
    for coach in list_coach:
        totalBatallas=coach.BPerdidas + coach.Bganadas
        Porcentaje=(coach.Bganadas/totalBatallas)* 100
        if Porcentaje>79:
            print(f"{coach.nombre}, porcentaje: {Porcentaje}")
            
#F. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#(tipo y subtipo);
def entrenadorTiposSubtipos(list_coach):
    for coach in list_coach:
        for pokemons in coach.pokemones:
            if pokemons.tipo=="Fuego" or pokemons.tipo=="Planta" or pokemons.tipo=="Agua":
                print(f"{coach.nombre}")
                
# g. el promedio de nivel de los Pokémons de un determinado entrenador;  
def promedioCoach(list_coach):
    totalNiveles=0
    c_cont=0
    for coach in list_coach:
        for pokemons in coach.pokemones:
            if coach.nombre=="Ana": #elijo a Ana por ejemplo
                c_cont+=1
                totalNiveles=totalNiveles + pokemons.nivel
                promedio=(totalNiveles/c_cont)  
    return promedio      
   
# h. determinar cuántos c;
def determinadoPokemon(list_coach):
    for coach in list_coach:
        for pokemons in coach.pokemones:
            if pokemons.nombre=="Pikachu": #elijo a Pikachu
                    print(f"{coach.nombre}")
            
# i. mostrar los entrenadores que tienen Pokémons repetidos;
def CoachPokemonesRepetidos(list_coach):
    for coach in list_coach:
        nombres_vistos = []  # lista para controlar los nombres ya vistos
        tiene_repetidos = False

        for pokemon in coach.pokemones:
            if pokemon.nombre in nombres_vistos:
                tiene_repetidos = True
            else:
                nombres_vistos.append(pokemon.nombre)

        if tiene_repetidos:
            print(coach.nombre)

#j. determinar los entrenadores que tengan uno de los siguientes Pokémons: "Tyrantrum, Te-rrakion o Wingull";                  
def determinarEntrenadores(list_coach):
    buscados=["Tyrantrum","Te-rrakion","Wingull"]
    for coach in list_coach:
        for nombre in buscados:
            index=coach.pokemones.search(nombre,"nombre")
            if index: 
                print(f"{coach.nombre} tiene a {nombre}")

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
def buscarPokemonDeEntrenador(list_coach):
    nombre_entrenador = input("Ingrese el nombre del entrenador: ")
    nombre_pokemon = input("Ingrese el nombre del Pokémon: ")
    encontrado = False
    
    for coach in list_coach:
        if coach.nombre == nombre_entrenador:
            for pokemon in coach.pokemones:
                if pokemon.nombre == nombre_pokemon:
                    print("Entrenador encontrado:")
                    print(f"{coach}")
                    print("Datos del Pokémon:")
                    print(f"{pokemon}")
                    encontrado = True

    if not encontrado:
        print("El entrenador no tiene ese Pokémon.")
        
#CP
cargarEntrenador(list_entrenadores, entrenadores)
cargarPokemon(list_entrenadores,pokemons)
ordenarCriterios(list_entrenadores)
ordenarNombres(list_entrenadores)
# print("Lista de entrenadores con sus respectivos pokemones: ")
# list_entrenadores.show_list_of_list()
cant_pokemones=cantidadPokemons(list_entrenadores)
print(f"La cantidad de Pokémons de Luis es: {cant_pokemones}")
print()
mostrarCoachTorneos(list_entrenadores)
print()
PokemonCoachMayor(list_entrenadores)
print()
print("Todos los datos de Pedro y sus pokemones: ")
mostrarDatosEntrenador(list_entrenadores)
print()
print("Entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %: ")
entrenadoresPorcentaje79(list_entrenadores)
print()
print("Entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador: ")
entrenadorTiposSubtipos(list_entrenadores)
print()
promedioTotal=promedioCoach(list_entrenadores)
print(f"El promedio de nivel de los Pokémons de Ana es de: {promedioTotal}")
print()
print("Entrenadores que tienen a Pikachu: ")
determinadoPokemon(list_entrenadores)
print()
print("Entrenadores que tienen Pokémons repetidos: ")
CoachPokemonesRepetidos(list_entrenadores)
print()
print("Entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-rrakion o Wingull")
determinarEntrenadores(list_entrenadores)
print()
buscarPokemonDeEntrenador(list_entrenadores)