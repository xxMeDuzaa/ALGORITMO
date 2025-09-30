"Diseñar un algoritmo que permita contar la cantidad de nodos de una lista."

from Tp4.Tp4.list_ import List 

list_nodos = List ()
nodos = [1, 22, 96, 85, 45, 78, 52]

for nodo in nodos:
    list_nodos.insert_value(nodo)


contador=0
for i in list_nodos:
    contador+=1



list_nodos.show()
msj= (f"La cantidad de nodos es de {contador}")
print(msj)



