# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:

from graph import Graph
import math

grafo = Graph(is_directed=False)

# D-cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2D2, BB8;
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C3PO", "Leia", 
    "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2D2", "BB8"
]

# A-cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
def insertar_personajes(graph):
    for pj in personajes:
        graph.insert_vertex(pj)

def insertar_interacciones(graph):
    graph.insert_edge("C3PO", "R2D2", 9) 
    graph.insert_edge("Luke Skywalker", "Leia", 6)
    graph.insert_edge("Luke Skywalker", "Han Solo", 6)
    graph.insert_edge("Chewbacca", "Han Solo", 6)
    graph.insert_edge("Yoda", "Luke Skywalker", 4)
    graph.insert_edge("R2D2", "BB8", 2) 
    graph.insert_edge("Darth Vader", "Luke Skywalker", 3)
    graph.insert_edge("C3PO", "Leia", 6)
    graph.insert_edge("Rey", "BB8", 3)
    graph.insert_edge("Rey", "Kylo Ren", 3)
    graph.insert_edge("Chewbacca", "Rey", 3)
    graph.insert_edge("Han Solo", "Rey", 1) 
    graph.insert_edge("Leia", "Rey", 3)
    graph.insert_edge("C3PO", "Rey", 3)
    graph.insert_edge("Darth Vader", "Yoda", 2)
    graph.insert_edge("Boba Fett", "Darth Vader", 2)

# B-hallar el árbol de expansión mínimo desde el vértice que contiene a: C3PO, Yoda y Leia;
def arbol_expansion_minima(grafo, vertice_inicio):
    resultado = grafo.kruskal(vertice_inicio)

    print(f"-------Árbol de expansión mínima desde {vertice_inicio}:")

    aristas = resultado.split(';')
    peso_total = 0

    for item in aristas:
        if '-' in item:
            origen, destino, peso = item.split('-')
            peso = int(peso)
            print(f"{origen}  ---->  {destino}")
            peso_total += peso

    print(f"---Peso total del árbol: {peso_total} ----")
    print()

# C-determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
def max_episodios(graph):
    max_peso = 0
    pares_maximos = []

    for vertex in graph:
        for edge in vertex.edges:
            peso = edge.weight

            if peso > max_peso:
                max_peso = peso
                pares_maximos = [(vertex.value, edge.value)]
            elif peso == max_peso:
                pares_maximos.append((vertex.value, edge.value))

    return max_peso, pares_maximos

# E-calcule el camino mas corto desde: C3PO a R2D2 y desde Yoda a Darth Vader;
def camino_corto(graph, origin, destino):
    path = graph.dijkstra(origin) 
    destination = destino
    peso_total = None
    camino_completo = []
    resultados = {}

    while path.size() > 0:
        value = path.pop()
        if value[0] == destination:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destination = value[2]

    camino_completo.reverse()

    resultados[origin] = {
        "camino": camino_completo,
        "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
    }

    return resultados

# F-indicar qué personajes aparecieron en los nueve episodios de la saga.
def personajes_en_nueve_episodios(graph):
    personajes_9 = []

    for vertex in graph:
        for edge in vertex.edges:
            if edge.weight == 9:
                if vertex.value not in personajes_9:
                    personajes_9.append(vertex.value)
                if edge.value not in personajes_9:
                    personajes_9.append(edge.value)

    return personajes_9


 
#MAIN:
insertar_personajes(grafo)
insertar_interacciones(grafo)
# grafo.show()
arbol_expansion_minima(grafo, "C3PO")
arbol_expansion_minima(grafo, "Yoda")
arbol_expansion_minima(grafo, "Leia")
print()

# C-determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
max_episodios(grafo)
maximo, pares = max_episodios(grafo)
print("Numero maximo de episodios que comparten dos personajes:", maximo)
print("Pares que comparten ese número:", pares)
print()

# E-calcule el camino mas corto desde: C3PO a R2D2 y desde Yoda a Darth Vader;
print("--Camino mas corto desde C3PO a R2D2: ")
print(camino_corto(grafo, "C3PO", "R2D2"))
print("--Camino mas corto desde Yoda a Darth Vader: ")
print(camino_corto(grafo,"Yoda", "Darth Vader"))
print()

# F-indicar qué personajes aparecieron en los nueve episodios de la saga.
print("Personajes que aparecieron en los nueve episodios de la saga: ")
print(personajes_en_nueve_episodios(grafo))