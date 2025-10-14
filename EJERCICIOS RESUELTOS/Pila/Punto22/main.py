# 22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
# Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
# misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,
# "costo" de la recompensa. Resolver las siguientes actividades:

# a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno de los cazzarrecompensas;
# b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos quien obtuvo mayor fortuna;
# c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
# d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

from mision import Mision
from stack import Stack

misionBF_stack= Stack() #Pila para la nave del cazarrecompensas Boba Fett (BF)
misionDD_stack=Stack() #Pila para la nave del cazarrecompensas Din Djarin (DD)

#Cargo las variables de cada uno:
mision1BF = Mision("Kamino", "Cad Bane", 4000)
mision2BF = Mision("Tatooine", "Han Solo", 5000)
mision3BF = Mision("Mustafar", "Bossk", 4500)
mision1DD = Mision("Geonosis", "Fenn Rau", 3000)
mision2DD = Mision("Nevarro", "Migs Mayfeld", 3500)
mision3DD = Mision("Lothal", "Paz Vizsla", 3200)


misionesBF=[mision1BF,mision2BF,mision3BF]
misionesDD=[mision1DD,mision2DD,mision3DD]

def cargarPila(pila_stack,misiones):
    for mision in misiones:
        pila_stack.push(mision)
        
def mostrarPlanetas(pila_stack):
    aux_stack=Stack() #pila auxiliar para posteriormente restablecer pila original
    while pila_stack.size()>0:
        mision=pila_stack.pop()
        aux_stack.push(mision)
        print(f"{mision.planeta}")
    
    while aux_stack.size()>0: #restablezco la pila original de cada uno
        pila_stack.push(aux_stack.pop())
        
def creditosTotal(pila_stack):
    aux_stack=Stack() #pila auxiliar para posteriormente restablecer pila original
    c_capturas=0
    while pila_stack.size()>0:
        mision=pila_stack.pop()
        aux_stack.push(mision)
        c_capturas=c_capturas + mision.costo
    
    while aux_stack.size()>0: #restablezco la pila original de cada uno
        pila_stack.push(aux_stack.pop())
        
    return c_capturas

def posicionMision(pila_stack):
    aux_stack=Stack() #pila auxiliar para restaurar la pila original
    pos=0
    for i in range(pila_stack.size()):
        pos+=1
        mision=pila_stack.pop()
        aux_stack.push(mision)
        
        if mision.captura=="Han Solo":
            print(f"La posicion en la que Boba Fett capturo a Han Solo es: {pos}")
            
            
    while aux_stack.size()>0: #restauro la pila original
        pila_stack.push(aux_stack.pop())

def cantidadCapturas(pila_stack):
    aux_stack=Stack() #pila auxiliar para posteriormente restablecer pila original
    c_capturas=0
    while pila_stack.size()>0:
        c_capturas+=1
        mision=pila_stack.pop()
        aux_stack.push(mision)
    
    while aux_stack.size()>0: #restablezco la pila original de cada uno
        pila_stack.push(aux_stack.pop())
        
    return c_capturas


#CUERPO PRINCIPAL:
cargarPila(misionBF_stack,misionesBF)
cargarPila(misionDD_stack,misionesDD)
# print("Pila cargada de misiones del cazarrecompenzas Boba Fett: ")
# misionBF_stack.show()
# print()
# print("Pila cargada de misiones del cazarrecompenzas Din Djarin: ")
# misionDD_stack.show()
print("Planetas visitados por Boba Fett: ")
mostrarPlanetas(misionBF_stack)
print()
print("Planetas visitados por Din Djarin: ")
mostrarPlanetas(misionDD_stack)
print()
ac_creditosBF=creditosTotal(misionBF_stack)
ac_creditosDD=creditosTotal(misionDD_stack)
print(f"Los créditos galácticos totales que recaudo Boba Fett es de: {ac_creditosBF}")
print(f"Los créditos galácticos totales que recaudo Din Djarin es de: {ac_creditosDD}")
print("El cazarrecompensas que obtuvo mas fortuna es: ")
if ac_creditosBF>ac_creditosDD:
    print("Boba Fett")
else:
    print("Din Djarin")
print()
posicionMision(misionBF_stack)
print()
cantidadCapturasBF=cantidadCapturas(misionBF_stack)
cantidadCapturasDD=cantidadCapturas(misionDD_stack)
print(f"La cantidad de capturas que hizo Boba Fett es de: {cantidadCapturasBF}")
print(f"La cantidad de capturas que hizo Din Djarin es de: {cantidadCapturasDD}")