# #Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonantes
# y otros caracteres que no sean letras (signos de puntuación números, espacios, etc.). Luego
# utilizando las operaciones de pila resolver las siguientes consignas:

# a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);

# b. cantidad de espacios en blanco;

# c. porcentaje que representan las vocales respecto de las consonantes sobre el total de caracteres del párrafo;

# d. cantidad de números;

# e. determinar si la cantidad de vocales y otros caracteres son iguales;

# f. determinar si existe al menos una z en la pila de consonantes.

from stack import Stack

parrafo_stack = Stack()
vocales_stack = Stack()
consonantes_stack = Stack()
caracteres_stack = Stack()

parrafo = "en 2024, la ciencia avanzó rápidamente: se descubrieron tres nuevos elementos, y 15 científicos ganaron premios."

def cargarPila(parra_stack,parrafo):
    for parra in parrafo:
        parra_stack.push(parra)
        
def separarPilas(parra_stack,voca_stack,conso_stack,carac_stack):
    aux_stack= Stack()
    while parra_stack.size()>0:
        element=parra_stack.pop()
        if element.lower() in "aeiou": #compara si el elemento (pasado en minuscula) esta en las vocales
            voca_stack.push(element)
        elif element.lower() in "bcdfghjklmnñpqrstvwxyz":
            conso_stack.push(element)
        else:
            carac_stack.push(element)
        aux_stack.push(element)
    
    while aux_stack.size()>0:
        parra_stack.push(aux_stack.pop()) #restauro la pila original
        
        
def contadorPilas(voca_stack,conso_stack,carac_stack):
    c_voca=voca_stack.size()
    c_conso=conso_stack.size()
    c_carac=carac_stack.size()
    return c_voca, c_conso, c_carac

def contadorEspacios(carac_stack):
    c_espacios=0
    while carac_stack.size()>0:
        elemento=carac_stack.pop()
        if elemento==" ":
            c_espacios+=1
    return c_espacios

def porcentajeVC(c_voca,c_conso,c_carac):
    sumatoriaTotal=0
    sumatoriaVC=0
    porcentaje_=0
    sumatoriaTotal=c_voca+c_conso+c_carac
    sumatoriaVC=c_voca+c_conso
    porcentaje_=(sumatoriaVC/sumatoriaTotal)*100
    return porcentaje_

def cantidadNumeros(parra_stack):
    c_numeros=0
    while parra_stack.size()>0:
        element=parra_stack.pop()
        if element in "0123456789":
            c_numeros+=1
    return c_numeros
    
def cantidadIguales(c_voca,c_carac):
    if c_voca==c_carac:
        print("La cantidad de vocales y otros caracteres son iguales.")
    else:
        print("La cantidad de vocales y otros caracteres no son iguales.")
    
def existeLetraZ(conso_stack):
    encontradoZ=False
    while conso_stack.size()>0:
        element=conso_stack.pop()
        if element.lower()=="z":
            encontradoZ=True
    return encontradoZ
            
    

       
contador_vocales=0 
contador_consonantes=0
contador_caracteres=0 
cargarPila(parrafo_stack,parrafo)
parrafo_stack.show()
separarPilas(parrafo_stack,vocales_stack,consonantes_stack,caracteres_stack)
print("Pila cargada de vocales: ")
vocales_stack.show()
print("Pila cargada de consonantes: ")
consonantes_stack.show()
print("Pila cargada de caracteres que no son letras: ")
caracteres_stack.show()
print()
contador_vocales, contador_consonantes, contador_caracteres=contadorPilas(vocales_stack,consonantes_stack,caracteres_stack)
print(f"La cantidad de vocales es: {contador_vocales}")
print(f"La canidad de consonantes es: {contador_consonantes}")
print(f"La cantidad de caracteres que no son letras es: {contador_caracteres}")
print()
contador_espacios=contadorEspacios(caracteres_stack)
print(f"La cantidad de espacios en blanco es: {contador_espacios}")
porcentaje=porcentajeVC(contador_vocales,contador_consonantes,contador_caracteres)
print(f"El porcenrta que representan las vocales respecto de las consonantes sobre el total de caracteres del párrafo es de: {porcentaje}%")
contador_numeros=cantidadNumeros(parrafo_stack)
print(f"La cantidad de numeros es de: {contador_numeros}")
cantidadIguales(contador_vocales,contador_caracteres)
encontrado=existeLetraZ(consonantes_stack)
print(f"Existe al menos una z en la pila de consonantes?: {encontrado}")