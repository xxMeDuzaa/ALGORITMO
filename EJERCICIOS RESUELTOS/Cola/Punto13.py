# 13. Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes actividades:
# a. separarla en dos colas una con dígitos y otra con el resto de los caracteres.
# b. determinar cuántas letras hay en la segunda cola.
# c. determinar además si existen los caracteres “?” y “#”.


from queue import Queue

caracteres_queue=Queue()
digitos_queue=Queue()
otrosCarac_queue=Queue()

caracteres=["a", "9", "#", "B", "!", "2", "?", "z", "5", "@"] #aca serian 50mil caracteres
letras= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cargarCola(carac_queue,caracteres):
    for carac in caracteres:
        carac_queue.arrive(carac)
        
def separarCola(carac_queue,dig_queue,otroCarac_queue):
    while carac_queue.size():
        element=carac_queue.attention()
        if element in "0123456789":
            dig_queue.arrive(element)
        else:
            otroCarac_queue.arrive(element)
        
def determinarLetras(otroCarac_queue,letras):
    aux_queue=Queue()
    c_letras=0
    while otroCarac_queue.size()>0:
        element=otroCarac_queue.attention()
        aux_queue.arrive(element)
        if element.lower() in letras:
            c_letras+=1
    
    while aux_queue.size()>0:
        otroCarac_queue.arrive(aux_queue.attention())
        
    return c_letras #returno la cantidad de letras
    
def existenCaracteres(otroCarac_queue): #no es necesario que restablezca la cola original
    encontrado=False
    while otroCarac_queue.size()>0:
        element=otroCarac_queue.attention()
        if element=="?" or element=="#":
            encontrado=True
     
    if encontrado==True:
        print("Si, se encontraron los caracteres “?” y “#”.")       
    if encontrado==False:
        print("No, no se encontraron los caracteres “?” y “#”.")
    
#CUERPO PRINCIPAL
cargarCola(caracteres_queue,caracteres)
print("Cola original con todos los caracteres: ")
caracteres_queue.show()
separarCola(caracteres_queue,digitos_queue,otrosCarac_queue)
print("Cola de digitos: ")
digitos_queue.show()
print()
print("Cola de otros caracteres: ")
otrosCarac_queue.show()
print()
cantidad_letras=determinarLetras(otrosCarac_queue,letras)
print(f"La cantidad de letras que hay en la Cola de otros caracteres es de: {cantidad_letras}")
print()
print("¿Se encontraron los caracteres “?” y “#”?: ")
existenCaracteres(otrosCarac_queue)