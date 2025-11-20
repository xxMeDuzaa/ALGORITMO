"""Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;

c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;

d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv."""

from graph import Graph
import math

g = Graph(is_directed=False)  # Grafo no dirigido

# ---A- cada vértice representar un ambiente de una casa
def crear_casa(g):

    ambientes = [
    "cocina", "comedor", "cochera", "quincho",
    "baño 1", "baño 2", "habitación 1", "habitación 2",
    "sala de estar", "terraza", "patio"
    ]

    for ambie in ambientes:
        g.insert_vertex(ambie) #cada ambiente es un vértice



    # ---B- ARISTAS (2 aristas con 5 conexiones, el resto con al menos 3)
    Conexiones = [

        ("cocina", "comedor", 5),
        ("cocina", "patio", 10),
        ("cocina", "baño 1", 7),
        ("cocina", "cochera", 15),
        ("cocina", "terraza", 9),

        ("comedor", "sala de estar", 4),
        ("comedor", "terraza", 8),
        ("comedor", "quincho", 6),
        ("comedor", "patio", 11),
        ("comedor", "baño 1", 12),

        ("cochera", "patio", 9),
        ("cochera", "baño 2", 14),
        ("cochera", "habitación 2", 11),

        ("quincho", "terraza", 3),
        ("quincho", "patio", 7),
        ("quincho", "sala de estar", 10),

        ("baño 1", "habitación 1", 4),
        ("baño 1", "baño 2", 6),
        ("baño 1", "sala de estar", 8),

        ("baño 2", "habitación 2", 5),
        ("baño 2", "sala de estar", 9),
        ("baño 2", "terraza", 12),

        ("habitación 1", "habitación 2", 7),
        ("habitación 1", "sala de estar", 6),
        ("habitación 1", "terraza", 10),

        ("habitación 2", "comedor", 5),
        ("habitación 2", "patio", 8),
        ("habitacion 2", "terraza", 4),

        ("sala de estar", "quincho", 5),
        ("sala de estar", "habitación 2", 8),
        ("sala de estar", "baño 1", 11),

        ("terraza", "patio", 4),
        ("terraza", "sala de estar", 2),
        ("terraza", "sala de estar", 7),

        ("patio", "sala de estar", 9),
        ("patio", "cochera", 13),
        ("patio", "quincho", 6),
    ]

    for a,b,metros in Conexiones:
        g.insert_edge(a, b, metros)

    return g




# ---C- árbol de expansión mínima (MST)
def mst_metros(g, vertice):
    print("Árbol de Expansión Mínima:")

    mst = g.kruskal(vertice)  # Obtener el árbol de expansión mínima usando el algoritmo de Kruskal
    total_metros = 0

    for edge in mst.split(";"):
        if edge:
            try:
                padre, destino, peso = edge.split("-")
                peso = int(peso)
                total_metros += peso
                print(f"{padre} -- {destino} : {peso} metros")
            except ValueError:
                print(f"Advertencia: Error de formato en la arista: '{edge}'.")

    print(f"\nTotal de metros de cable necesarios para conectar todos los ambientes: {total_metros} metros\n")


# ---D- camino más corto desde la habitación 1 hasta la sala de estar
def camino_mas_corto(g):
    inicio = "habitación 1"
    destino = "sala de estar"
    
    path_stack = g.dijkstra(inicio) # Pila con (vértice, distancia, predecesor)

    padres = {}
    distancia_final = math.inf
    
    # 1. Procesar la Pila para crear el mapa de padres y encontrar la distancia final
    while path_stack.size() > 0:
        value = path_stack.pop() # (vértice, distancia, predecesor)
        vertice, distan, padre = value[0], value[1], value[2]
        
        padres[vertice] = padre
        if vertice == destino:
            distancia_final = distan
            
    # 2. Reconstruir el camino
    camino_completo = []
    current_vertice = destino

    if distancia_final == math.inf:
        return {
            "camino": "No es posible conectar",
            "distancia_total_metros": math.inf
        }
        
    while current_vertice is not None:
        camino_completo.append(current_vertice)
        if current_vertice == inicio:
            break
        current_vertice = padres.get(current_vertice)

    camino_completo.reverse()

    return {
        "camino": " -> ".join(camino_completo),
        "distancia_total_metros": distancia_final
    }
    

#---MAIN---
g = crear_casa(g)
print()

mst_metros(g, "cocina")
print()

print("El camino más corto desde la habitación 1 hasta la sala es: ")
resultado_camino = camino_mas_corto(g)
if resultado_camino["distancia_total_metros"] != math.inf:  #distinto de infinito
    print(f"Camino: **{resultado_camino['camino'].replace('_', ' ')}**")
    print(f"Metros de cable de red necesarios: **{resultado_camino['distancia_total_metros']} metros**")
else:
    print(f"El camino es: {resultado_camino['camino']}")
    print(f"Distancia: {resultado_camino['distancia_total_metros']}")

print()
