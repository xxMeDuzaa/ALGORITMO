#Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

from list_ import List

list_vocales=List()

letras= ["A", "B", "G", "F", "O", "M", "u", "j"]

for letra in letras:
    list_vocales.insert_value(letra)

print("Lista original:")
list_vocales.show()

for letra in list_vocales:
    if letra in "aAeEiIoOuU":
        print(f"Se estan eliminando las vocal: {letra}")
        list_vocales.delete_value(letra)

print("Lista sin vocales: ")
list_vocales.show()
