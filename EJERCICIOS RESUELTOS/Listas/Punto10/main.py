# 10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artis-
# ta, duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que
# permita realizar las siguientes actividades:
# a. obtener la información de la canción más larga;
# b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
# c. obtener todas las canciones de la banda Arctic Monkeys;
# d. mostrar los nombres de las bandas o artistas que solo son de una palabra.

from list_ import List
from cancion import Cancion, order_by_duracion, order_by_cantReproducciones

list_canciones = List()

canciones = [
    Cancion("Do I Wanna Know?", "Arctic Monkeys", 272, 14500000),
    Cancion("Bohemian Rhapsody", "Queen", 354, 13200000),
    Cancion("Blinding Lights", "The Weeknd", 200, 19800000),
    Cancion("Imagine", "John Lennon", 183, 8700000),
    Cancion("505", "Arctic Monkeys", 268, 9400000),
    Cancion("Yellow", "Coldplay", 266, 7400000),
    Cancion("Lose Yourself", "Eminem", 326, 12800000),
    Cancion("Let It Be", "The Beatles", 243, 8900000),
    Cancion("Rolling in the Deep", "Adele", 228, 11300000),
    Cancion("Shape of You", "Ed Sheeran", 234, 21000000),
    Cancion("I Wanna Be Yours", "Arctic Monkeys", 183, 10400000),
    Cancion("Stairway to Heaven", "Led Zeppelin", 482, 9200000),
    Cancion("Smells Like Teen Spirit", "Nirvana", 301, 11900000),
    Cancion("Uptown Funk", "Bruno Mars", 269, 11700000),
    Cancion("Chandelier", "Sia", 216, 8700000),
    Cancion("Hey Jude", "The Beatles", 431, 10000000),
    Cancion("One", "U2", 276, 8200000),
    Cancion("Zombie", "Cranberries", 306, 8900000),
    Cancion("Thunderstruck", "ACDC", 292, 9900000),
    Cancion("Happier", "Marshmello", 214, 8600000),
    Cancion("Radioactive", "Imagine Dragons", 186, 9800000),
    Cancion("Believer", "Imagine Dragons", 204, 10300000),
    Cancion("Someone Like You", "Adele", 285, 9500000),
    Cancion("Numb", "Linkin Park", 186, 10200000),
    Cancion("Wonderwall", "Oasis", 258, 9100000),
    Cancion("Bad Guy", "Billie Eilish", 194, 12100000),
    Cancion("Shallow", "Lady Gaga", 215, 11400000),
    Cancion("Counting Stars", "OneRepublic", 257, 10000000),
    Cancion("Take On Me", "a-ha", 225, 9600000),
    Cancion("Perfect", "Ed Sheeran", 263, 11500000),
    Cancion("Creep", "Radiohead", 238, 9700000),
    Cancion("Back in Black", "ACDC", 255, 8800000),
    Cancion("Stay", "Rihanna", 245, 8500000),
    Cancion("Royals", "Lorde", 211, 8300000),
    Cancion("Havana", "Camila Cabello", 217, 11100000),
    Cancion("Halo", "Beyoncé", 261, 8900000),
    Cancion("Circles", "Post Malone", 215, 10500000),
    Cancion("Senorita", "Shawn Mendes", 190, 10900000),
    Cancion("Dance Monkey", "Tones and I", 210, 10700000),
    Cancion("Faded", "Alan Walker", 212, 9700000),
    Cancion("Savage Love", "Jawsh 685", 202, 9100000),
]

def cargarCanciones(list_song, canciones):
    for song in canciones:
        list_song.append(song)
        
def ordenarCriterios(list_song):
    list_song.add_criterion("duracion", order_by_duracion)
    list_song.add_criterion("cantReproducciones", order_by_cantReproducciones)
    
def ordenarDuracion(list_song):
    list_song.sort_by_criterion("duracion")

def ordenarReproduccion(list_song):
    list_song.sort_by_criterion("cantReproducciones")
    list_song.reverse()  # invierte el orden para mayor a menor

#A
def cancionMasLarga(list_song):
    cancionLarga= list_song[-1]
    print("Información de la canción más larga: ")
    print(cancionLarga)

#B
def mostrar_top(list_song,n):
    limite = n
    if len(list_song) < n:
        limite = len(list_song)

    print(f"TOP {n} de canciones mas escuchadas: ")
    for i in range(limite):
        print(list_song[i])

#C
def obtenerCanciones(list_song):
    encontrado=False
    for song in list_song:
        if song.banda_artista=="Arctic Monkeys":
            encontrado=True
            print(f"{song.nombre}")
    
    if encontrado==False:
        print("No se encontro canciones de la banda Arctic Monkeys.")
        
#D
def obtenerSoloPalabra(list_song):
    nombres_mostrados = []

    for cancion in list_song:
        artista = cancion.banda_artista
        palabras = artista.split() #sirve para dividir la cadena en una lista de palabras (para detectar nombres de artistas que solo tienen una palabra.)

        if len(palabras) == 1 and (artista not in nombres_mostrados):
            print(artista)
            nombres_mostrados.append(artista)

    if len(nombres_mostrados) == 0:
        print("No se encontraron nombres de bandas o artistas con una sola palabra.")


            
    
#CP
cargarCanciones(list_canciones,canciones)
ordenarCriterios(list_canciones)
ordenarDuracion(list_canciones)
# print("Listas de canciones ordenadas por duracion: ")
# list_canciones.show()
print()
cancionMasLarga(list_canciones)
print()
ordenarReproduccion(list_canciones)
# print("Listas de canciones ordenadas por reproducciones: ")
# list_canciones.show()
mostrar_top(list_canciones, 5)
print()
mostrar_top(list_canciones, 10)
print()
mostrar_top(list_canciones, 40)
print()
print("Todas las canciones de la banda Arctic Monkeys: ")
obtenerCanciones(list_canciones)
print()
print("Nombres de las bandas o artistas que solo son de una palabra: ")
obtenerSoloPalabra(list_canciones)