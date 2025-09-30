#7. Implementar los algoritmos necesarios para resolver las siguientes tareas:


from Tp4.Tp4.list_ import List
from random import randint 

list_a= List()
list_b= List()
list_c= List()
list_d=List()

for i in range(5):
    list_a.insert_value(randint(1,50))
    list_b.insert_value(randint(1,50))

print("--------- Lista A: ---------")
list_a.show()
print()

print("--------Lista B: ----------")
list_b.show()

#a. concatenar dos listas, una atrás de la otra;
for valor in list_a:
    list_c.insert_value(valor)

for valor in list_b:
    list_c.insert_value(valor)

print()
print("----------- Lista C ------------")
list_c.show()

#b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
valores_vistos = set()
for valor in list_a:
    if valor not in valores_vistos:
        list_d.insert_value(valor)
        valores_vistos.add(valor)

for valor in list_b:
    if valor not in valores_vistos:
        list_d.insert_value(valor)
        valores_vistos.add(valor)

print("----------- Lista sin repetidos -----------")
list_d.show()

#c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;

#d. 


