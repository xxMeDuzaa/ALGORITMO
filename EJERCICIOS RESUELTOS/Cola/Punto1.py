#1. Eliminar de una cola de caracteres todas las vocales que aparecen.

from queue import Queue
from random import randint


letters_queue = Queue()

def cargar_cola(letter_queue):
    for i in range(15):
        letter_queue.arrive(chr(randint(65, 90)))

def eliminarVocalesCola(letter_queue):
    for i in range(letter_queue.size()):
        if letter_queue.on_front() in ["A", "E", "I", "O", "U"]:
            letter_queue.attention()
        else:
            letter_queue.move_to_end()

cargar_cola(letters_queue)
print("Cola original: ")
letters_queue.show()
print()
print("Cola sin vocales: ")
eliminarVocalesCola(letters_queue)
letters_queue.show()