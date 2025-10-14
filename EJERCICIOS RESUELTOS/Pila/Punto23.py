# 23. Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
# obtener la siguiente información sin perder los datos:

# a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
# b. calcular el promedio de temperatura (o media) del total de valores;
# c. determinar la cantidad de valores por encima y por debajo de la media.

from stack import Stack
temperaturas_stack=Stack()

temperaturas=[18, 20, 21, 19, 17, 22, 23, 24, 18, 20, 19, 21, 22, 23, 19, 18, 20, 21, 22, 23, 24, 32, 20, 19, 18, 22, 23, 24, 22, 10] #dia 30 menor temp (10), dia 22 mayor temp (32)

def cargarPila(temp_stack,temperaturas):
    for temp in temperaturas:
        temp_stack.push(temp)

def rangoTemperatura(temp_stack):
    min=temp_stack.on_top()
    max=temp_stack.on_top()
    aux_stack=Stack() #pila auxiliar para reponer pila original
    while temp_stack.size()>0:
        temp=temp_stack.pop()
        aux_stack.push(temp)
        if temp>max:
            max=temp
        
        if temp<min:
            min=temp
    
    while aux_stack.size()>0: #restablezco la pila original
        temp_stack.push(aux_stack.pop())
        
    return max,min #devuelvo la max y min temperatura

def promedioTemperatura(temp_stack):
    c_temperaturas=0
    ac_temperatura=0
    aux_stack=Stack() #pila auxiliar para reponer pila original
    while temp_stack.size()>0:
        temp=temp_stack.pop()
        aux_stack.push(temp)
        c_temperaturas+=1
        ac_temperatura=ac_temperatura+temp
    
    while aux_stack.size()>0: #restablezco la pila original
        temp_stack.push(aux_stack.pop())

    return (ac_temperatura/c_temperaturas)
       
def cantidadValoresMedia(temp_stack,promTotal):
    c_encima=0
    c_debajo=0
    aux_stack=Stack() #pila auxiliar para reponer pila original
    while temp_stack.size()>0:
        temp=temp_stack.pop()
        aux_stack.push(temp)
        
        if temp>promTotal:
            c_encima+=1
        elif temp<promTotal:
            c_debajo+=1
    
    while aux_stack.size()>0: #restablezco la pila original
        temp_stack.push(aux_stack.pop())
        
    return c_encima,c_debajo
   
    

#CUERPO PRINCIPAL:
cargarPila(temperaturas_stack,temperaturas)
# print("Pila con todas las temperaturas de cada dia del mes de Abril: ")
# temperaturas_stack.show()
print()
max_temp,min_temp=rangoTemperatura(temperaturas_stack)
print(f"La temperatura maxima del mes de abril fue: {max_temp} y la temperatura minima fue de: {min_temp}")
print(f"El rango de la temperatura del mes es de: {max_temp-min_temp}")
print()
promedioTotal=promedioTemperatura(temperaturas_stack)
print(f"El promedio de las temperaturas es de: {promedioTotal}")
contadorEncima,contadorDebajo=cantidadValoresMedia(temperaturas_stack,promedioTotal)
print(f"La cantidad de temperatura que estan por encima de la media son: {contadorEncima} y los que estan por debajo: {contadorDebajo}")