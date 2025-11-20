"""
Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
sarios para resolver las tareas, listadas a continuación:

a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
dor, router, switch, impresora;

b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
Red Hat, Debian, Arch;

c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
Red Hat, Fedora hasta la impresora;

d. encontrar el árbol de expansión mínima;

e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;

f. indicar desde que computadora del switch 01 es el camino más corto
al servidor “MongoDB”;

g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;

h. debe utilizar un grafo no dirigido.
"""

from graph import Graph
from Tarea_ejer5 import Tarea
import math

# --- H- GRAFO NO DIRIGIDO ---
g = Graph(is_directed=False)


# --- A- NODOS CON TIPO ---
def crear_red():
    
    g.insert_vertex("Manjaro", Tarea("Manjaro", "pc"))
    g.insert_vertex("Ubuntu", Tarea("Ubuntu", "pc"))
    g.insert_vertex("Fedora", Tarea("Fedora", "pc"))
    g.insert_vertex("Red Hat", Tarea("Red Hat", "notebook"))
    g.insert_vertex("Debian", Tarea("Debian", "notebook"))
    g.insert_vertex("Arch", Tarea("Arch", "notebook"))
    g.insert_vertex("Guaraní", Tarea("Guaraní", "servidor"))
    g.insert_vertex("MongoDB", Tarea("MongoDB", "servidor"))
    g.insert_vertex("Router 01", Tarea("Router 01", "router"))
    g.insert_vertex("Router 02", Tarea("Router 02", "router"))
    g.insert_vertex("Switch 01", Tarea("Switch 01", "switch"))
    g.insert_vertex("Switch 02", Tarea("Switch 02", "switch"))
    g.insert_vertex("Impresora", Tarea("Impresora", "impresora"))
    g.insert_vertex("Servidor Web", Tarea("Servidor Web", "impresora"))

    Conexines = [
        ("Manjaro", "Router 01", 4),
        ("Red Hat", "Router 01", 2),
        ("Debian", "Router 02", 1),
        ("Arch", "Router 02", 3),
        ("Fedora", "Router 02", 2),
        ("Router 01", "Switch 01", 2),
        ("Router 02", "Switch 01", 3),
        ("Router 02", "Switch 02", 2),
        ("Switch 01", "Guaraní", 5),
        ("Switch 01", "MongoDB", 6),
        ("Switch 02", "MongoDB", 4),
        ("Switch 02", "Impresora", 3)
    ]

    for origen, destino, peso in Conexines:
        g.insert_edge(origen, destino, peso)    

    return g


#--- B- BARRIDO EN PROFUNDIDAD Y AMPLITUD DESDE 3 NOTEBOOKS ---
#notebooks = ["Red Hat", "Debian", "Arch"]
def barrido_notebooks(g):
    notebooks = ["Red Hat", "Debian", "Arch"]

    for notebook in notebooks:
        print(f"\nBarrido en profundidad desde {notebook}:")
        g.deep_sweep(notebook)
        print()
        print(f"\nBarrido en amplitud desde {notebook}:")
        g.amplitude_sweep(notebook)
        print()


#--- C- CAMINO MÁS CORTO HASTA IMPRESORA DESDE 3 PCS ---
def camino_mas_corto_impresora(grafo):
    compus = ["Manjaro", "Red Hat", "Fedora"]
    resultados = {}

    for pc in compus:
        path = grafo.dijkstra(pc) #todos los caminos mas cortos a pc
        destino = "Impresora"
        peso_total = None
        camino_total = []

        while path.size() > 0: #mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destino: #si el destino es igual al nodo actual
                if peso_total is None:
                    peso_total = value[1] #añade el peso
                camino_total.append(value[2]) #añade la impresora al camino
                destino = value[2] #añade el predecesor de la impresora
        
        camino_total.reverse() #invierte el camino para que vaya desde el origen al destino

        resultados[pc] = {
            "camino": camino_total,
            "peso_total": peso_total if peso_total is not None and peso_total != math.inf else math.inf
        }

    return resultados


#--- D- ÁRBOL DE EXPANSIÓN MÍNIMA ---
def arbol_expansion_minima(g, vertice):
    mst = g.kruskal(vertice)
    peso_total = 0
    for edge in mst.split(";"):
        origen, destino, peso = edge.split("-")
        print(f"{origen} -- {destino} (Peso: {peso})")
        peso_total += int(peso)
    print(f"Peso total del árbol de expansión mínima: {peso_total}")


#--- E- CAMINO MÁS CORTO HASTA SERVIDOR GUARANÍ DESDE PCS (NO NOTEBOOKS) ---
def camino_mas_corto_guarani(grafo):
    compus = ["Manjaro", "Ubuntu", "Fedora"]  # PCs (no notebooks)
    compu_cercana = None
    mejor_resultado = {}
    distancia_minima = math.inf

    for pc in compus:
        path = grafo.dijkstra(pc)  # todos los caminos más cortos a pc
        destino = "Guaraní"
        peso_total = None
        camino_total = []

        while path.size() > 0:  # mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destino:  # si el destino es igual al nodo actual
                if peso_total is None:
                    peso_total = value[1]  # añade el peso
                camino_total.append(value[0])  # añade Guaraní al camino
                destino = value[2]  # añade el predecesor de Guaraní

        camino_total.reverse()  # invierte el camino para que vaya desde el origen al destino

        if peso_total is not None and peso_total < distancia_minima:
            distancia_minima = peso_total
            compu_cercana = pc
            mejor_resultado = {
                pc : {
                    "camino": camino_total,
                    "peso_total": peso_total
                }
            }
    return mejor_resultado if compu_cercana else False


#--- F- CAMINO MÁS CORTO HASTA SERVIDOR MONGODB DESDE COMPUTADORAS DEL SWITCH 01 ---
def camino_mas_corto_mongodb(grafo):
    conexiones_switch_01 = ["Manjaro", "Red Hat", "Debian"]
    compu_cercana = None
    mejor_resultado = {}
    distancia_minima = math.inf

    for pc in conexiones_switch_01:
        path = grafo.dijkstra(pc)  # todos los caminos más cortos a pc
        destino = "MongoDB"
        peso_total = None
        camino_total = []

        while path.size() > 0:  # mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destino:  # si el destino es igual al nodo actual
                if peso_total is None:
                    peso_total = value[1]  # añade el peso
                camino_total.append(value[0])  # añade MongoDB al camino
                destino = value[2]  # añade el predecesor de MongoDB

        camino_total.reverse()  # invierte el camino para que vaya desde el origen al destino

        if peso_total is not None and peso_total < distancia_minima:
            distancia_minima = peso_total
            compu_cercana = pc
            mejor_resultado = {
                pc: {
                    "camino": camino_total,
                    "peso_total": peso_total
                }
            }
    return mejor_resultado if compu_cercana else False


#--- G- CAMBIO DE CONEXIÓN DE LA IMPRESORA AL ROUTER 02 Y REBARRIDO ---
def cambiar_conexion_impresora(grafo):
    # Elimina la conexión actual de la impresora al Switch 01
    g.delete_edge("Impresora", "Switch 01",'value')
    # Inserta la nueva conexión de la impresora al Router 02
    g.insert_edge("Impresora", "Router 02", 3)

    print("\nDespués de cambiar la conexión de la impresora al Router 02:")
    barrido_notebooks(g)


#--- MAIN ---
crear_red()
print()

print("=== BARRIDO DESDE NOTEBOOKS ===")
barrido_notebooks(g)
print()

print("=== CAMINO MÁS CORTO HASTA IMPRESORA DESDE TODAS LAS PCS ===")
print(camino_mas_corto_impresora(g))
print()

print("=== ÁRBOL DE EXPANSIÓN MÍNIMA ===")
arbol_expansion_minima(g, "Manjaro")
print()

print("=== CAMINO MÁS CORTO HASTA SERVIDOR GUARANÍ DESDE PCS (NO NOTEBOOKS) ===")
resultado_guarani = camino_mas_corto_guarani(g)
print(f"El camino mas corto es: {resultado_guarani}")
print()

print("=== CAMINO MÁS CORTO HASTA SERVIDOR MONGODB DESDE COMPUTADORAS DEL SWITCH 01 ===")
resultado_mongodb = camino_mas_corto_mongodb(g)
print(f"El camino mas corto es: {resultado_mongodb}")
print()

print("=== CAMBIO DE CONEXIÓN DE LA IMPRESORA AL ROUTER 02 Y REBARRIDO ===")
cambiar_conexion_impresora(g)
print()
